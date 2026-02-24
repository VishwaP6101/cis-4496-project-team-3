import os
import re
import shutil
import fitz  # PyMuPDF
import pandas as pd

# -----------------------
# SETTINGS
# -----------------------

INPUT_DIR = "./downloaded_pdfs"                    # Current folder
OUTPUT_DIR = "./sorted_output"      # New organized folder

TEXT_MIN_CHARS = 500                # Minimum characters to count as selectable
GIBBERISH_THRESHOLD = 0.30          # Higher = more tolerant

YEAR_REGEX = re.compile(r"(19\d{2}|20\d{2})")

# -----------------------
# HELPER FUNCTIONS
# -----------------------

def extract_text(pdf_path, max_pages=5):
    """Extract text from first few pages for speed."""
    try:
        doc = fitz.open(pdf_path)
        text = []
        pages = min(len(doc), max_pages)
        for i in range(pages):
            text.append(doc[i].get_text("text"))
        doc.close()
        return "\n".join(text).strip()
    except:
        return ""

def looks_joinable(filename):
    """Basic guess: filename contains a year."""
    return bool(YEAR_REGEX.search(filename))

def gibberish_ratio(text):
    """Estimate OCR quality."""
    if not text:
        return 1.0

    tokens = re.findall(r"\b[\w']+\b", text.lower())
    if len(tokens) < 50:
        return 1.0

    weird = 0
    sample = tokens[:2000]

    for t in sample:
        letters = sum(c.isalpha() for c in t)
        if len(t) <= 1:
            weird += 1
        elif len(t) >= 25:
            weird += 1
        elif letters / max(len(t), 1) < 0.6:
            weird += 1

    return weird / len(sample)

def clean_filename(name):
    name = re.sub(r"[^\w\s\-.]", "", name)
    name = re.sub(r"\s+", "_", name)
    return name

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# -----------------------
# MAIN SORTING LOGIC
# -----------------------

def main():

    # Create folder structure
    paths = {
        "selectable_joinable": os.path.join(OUTPUT_DIR, "Selectable", "Joinable"),
        "selectable_not_joinable": os.path.join(OUTPUT_DIR, "Selectable", "Not_Joinable"),
        "ocr_clear": os.path.join(OUTPUT_DIR, "OCR", "Clear_OCR"),
        "ocr_obscured": os.path.join(OUTPUT_DIR, "OCR", "Obscured_OCR"),
    }

    for p in paths.values():
        ensure_dir(p)

    log_data = []

    pdf_files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".pdf")]

    print(f"Found {len(pdf_files)} PDF files.")

    for file in pdf_files:
        src_path = os.path.join(INPUT_DIR, file)

        print(f"Processing: {file}")

        text = extract_text(src_path)
        text_length = len(text)

        # Determine Selectable vs OCR
        if text_length >= TEXT_MIN_CHARS:
            file_type = "Selectable"
            joinable = "Yes" if looks_joinable(file) else "No"

            if joinable == "Yes":
                dest_folder = paths["selectable_joinable"]
            else:
                dest_folder = paths["selectable_not_joinable"]

            ocr_quality = ""

        else:
            file_type = "OCR"
            joinable = "Unknown"

            if text_length == 0:
                ocr_quality = "Obscured_OCR"
                dest_folder = paths["ocr_obscured"]
            else:
                ratio = gibberish_ratio(text)
                if ratio <= GIBBERISH_THRESHOLD:
                    ocr_quality = "Clear_OCR"
                    dest_folder = paths["ocr_clear"]
                else:
                    ocr_quality = "Obscured_OCR"
                    dest_folder = paths["ocr_obscured"]

        # Clean filename
        new_name = clean_filename(file)
        dest_path = os.path.join(dest_folder, new_name)

        # Move file
        shutil.move(src_path, dest_path)

        log_data.append({
            "original_file": file,
            "new_location": dest_path,
            "type": file_type,
            "joinable_guess": joinable,
            "ocr_quality_guess": ocr_quality,
            "text_characters_extracted": text_length
        })

    # Save log
    df = pd.DataFrame(log_data)
    log_path = os.path.join(OUTPUT_DIR, "script_sort_log.csv")
    df.to_csv(log_path, index=False)

    print("\nDone.")
    print(f"Log saved to: {log_path}")

if __name__ == "__main__":
    main() 