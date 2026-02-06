# Project Charter

## Business background

* Who is the client, what business domain the client is in.
* Film studios, writers, and producers can use these findings to make informed decisions about content development and understand market dynamics between original storytelling and established formulas.
* What business problems are we trying to address?
* We aim to help clients understand whether movie storytelling is becoming repetitive or more diverse over time. We also aim to find insights on how narrative trends relate to audience engagement and performance of the film financially.

## Scope
* What data science solutions are we trying to build?
* We are building supervised and unsupervised machine learning models to analyze movie scripts, classify narrative patterns, and identify storytelling trends.
* What will we do?
* We will collect movie scripts and popularity data, preprocess text, extract features, train models, and analyze the changes in narrative diversity over time.
* How is it going to be consumed by the customer?
* Results will be delivered through reports, visualizations, and summary dashboards that studios and creators can use to guide content decisions.

## Personnel
* Who are on this project:
	* Microsoft:
		* Project lead
		* PM
		* Data scientist(s): Micah Hertzler, Ankur Sinha, Vishrut Kannan, Dmitry Bolshak, Vishwa Patel
		* Account manager
	* Client:
		* Data administrator
		* Business contact
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)
* Improve understanding of storytelling trends and support data-driven creative decision-making.
* What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
* Classification accuracy of narrative models and stability of detected themes over time.
* Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%)
* Achieve at least 85% classification accuracy and improve topic coherence scores by 15%.
* What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
* Initial supervised model accuracy of approximately 70% and baseline topic coherence from preliminary models.
* How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
* We will use cross-validation, historical comparisons, and performance evaluation on test datasets.

## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.
* Literature Review and Planning (Weeks 1–2):
Review related work and finalize methodology.

Data Collection and Preprocessing (Weeks 3–5):
Gather scripts and popularity data and clean text.

Feature Engineering and Modeling (Weeks 6–8):
Train supervised and unsupervised models.

Evaluation and Analysis (Weeks 9–10):
Assess performance and interpret results.

Reporting and Presentation (Weeks 11–12):
Prepare final report and presentation.

## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
    
  * Movie scripts (text files or PDFs), box office data, ratings, and metadata stored in CSV files or databases.

* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
 
  * Data will be collected from online sources and stored in cloud-based storage. Preprocessed and sampled data will be used for modeling.


* What tools and data storage/analytics resources will be used in the solution e.g.,
  * Python, Pandas, and NLP libraries for preprocessing
  * Scikit-learn, TensorFlow, and PyTorch for modeling
  * Azure Machine Learning for training and deployment
  * Azure Blob Storage for data storage
    
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
  
  * Studios will use model outputs to evaluate script originality and predict audience response.

## Communication
* How will we keep in touch? Weekly meetings?
* We will hold weekly progress meetings and share updates through discord and project management tools.
* Who are the contact persons on both sides?
