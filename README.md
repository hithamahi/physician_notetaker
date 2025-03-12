# physician_notetaker
This repository contains an AI-driven system for medical transcription, NLP-based summarization, and sentiment analysis of clinical notes and patient interactions. The project automates key aspects of clinical documentation and insights extraction using advanced natural language processing (NLP) techniques.

Features:
TASK 1: MEDICAL INFORMATION EXTRACTION
In this task, the system processes medical transcripts to automatically extract symptoms, diagnosis, treatment, and prognosis using an NLP-based approach. It leverages spaCy’s NLP pipeline along with phrase matching techniques to identify key medical terms and structured information from doctor-patient conversations. The extracted details are then formatted into a structured JSON medical report, ensuring clear and organized documentation of the patient's condition and treatment history. This automation helps streamline medical documentation and enhances efficiency in clinical workflows.

TASK 2: SENTIMENT AND INTENT ANALYSIS
In this task, patient responses from medical transcripts are analyzed using sentiment detection and intent classification techniques. Sentiment detection is performed using a fine-tuned DistilBERT model, which classifies patient statements as either reassured or anxious based on their emotional tone. Additionally, intent classification is implemented using zero-shot learning with BART, allowing the system to categorize patient responses without requiring labeled training data. The extracted intents include categories such as seeking reassurance, reporting symptoms, expressing concerns, describing an event, and general conversation, providing deeper insights into patient interactions and their emotional state.

TASK 3: SOAP NOTE GENERATION
In this task, the system automatically extracts Subjective, Objective, Assessment, and Plan (SOAP) notes from medical transcripts. It leverages rule-based NLP processing to identify key clinical details, such as patient symptoms, history, physical examination findings, diagnosis, treatment, and follow-up recommendations. The extracted data is structured into a JSON-formatted SOAP note, making it easier for healthcare professionals to review and document patient cases. Additionally, this approach can be further enhanced using transformer-based summarization models, such as T5, BART, or BioBERT, to improve accuracy and generate more comprehensive SOAP notes.

PRE-REQUISITES: 
-The provided code can be executed in Google Colab or Jupyter Notebook without any modifications. Both platforms offer an interactive environment for running the scripts, visualizing results, and making modifications as needed. Google Colab provides the added advantage of cloud-based execution with access to GPUs, while Jupyter Notebook allows for seamless local development and debugging.

TECH STACK:
NLP Models: spaCy, Transformers (DistilBERT)
Frameworks: Hugging Face
Data Processing: Regular expressions, phrase matching
Output Format: JSON-based structured medical reports

FUTURE ENHANCEMENTS:
To further improve the system's accuracy and efficiency, future enhancements will include fine-tuning ClinicalBERT and BioBERT for more precise medical summarization and information extraction. Additionally, integrating speech-to-text models will enable real-time transcription, allowing seamless conversion of doctor-patient conversations into structured medical records. The system will also be deployed as a FastAPI or Flask web service, facilitating easy integration with electronic health record (EHR) systems and enabling real-time access to generated medical reports.

