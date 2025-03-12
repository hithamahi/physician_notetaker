# -*- coding: utf-8 -*-
"""Physician_task2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LiH3bo_3TGO4Tfo00rWDw3q2CQY_QWMO
"""

import spacy

nlp=spacy.load("en_core_web_sm")

# Sample transcript
transcript = """
Physician: Good morning, Ms. Jones. How are you feeling today?
Patient: Good morning, doctor. I’m doing better, but I still have some discomfort now and then
Physician: I understand you were in a car accident last September. Can you walk me through what happened?
Patient: Yes, it was on September 1st, around 12:30 in the afternoon. I was driving from Cheadle Hulme to Manchester when I had to stop in traffic. Out of nowhere, another car hit me from behind, which pushed my car into the one in front
Physician: That sounds like a strong impact. Were you wearing your seatbelt?
Patient: Yes, I always do
Physician: What did you feel immediately after the accident?
Patient: At first, I was just shocked. But then I realized I had hit my head on the steering wheel, and I could feel pain in my neck and back almost right away
Physician: Did you seek medical attention at that time?
Patient: Yes, I went to Moss Bank Accident and Emergency. They checked me over and said it was a whiplash injury, but they didn’t do any X-rays. They just gave me some advice and sent me home
Physician: How did things progress after that?
Patient: The first four weeks were rough. My neck and back pain were really bad—I had trouble sleeping and had to take painkillers regularly. It started improving after that, but I had to go through ten sessions of physiotherapy to help with the stiffness and discomfort
Physician: That makes sense. Are you still experiencing pain now?
Patient: It’s not constant, but I do get occasional backaches. It’s nothing like before, though
Physician: That’s good to hear. Have you noticed any other effects, like anxiety while driving or difficulty concentrating?
Patient: No, nothing like that. I don’t feel nervous driving, and I haven’t had any emotional issues from the accident
Physician: And how has this impacted your daily life? Work, hobbies, anything like that?
Patient: I had to take a week off work, but after that, I was back to my usual routine. It hasn’t really stopped me from doing anything
Physician: That’s encouraging. Let’s go ahead and do a physical examination to check your mobility and any lingering pain
Physician: Everything looks good. Your neck and back have a full range of movement, and there’s no tenderness or signs of lasting damage. Your muscles and spine seem to be in good condition
Patient: That’s a relief!
Physician:Yes, your recovery so far has been quite positive. Given your progress, I’d expect you to make a full recovery within six months of the accident. There are no signs of long-term damage or degeneration.
Patient:That’s great to hear. So, I don’t need to worry about this affecting me in the future?
Physician:That’s right. I don’t foresee any long-term impact on your work or daily life. If anything changes or you experience worsening symptoms, you can always come back for a follow-up. But at this point, you’re on track for a full recovery.
Patient:Thank you, doctor. I appreciate it.
Physician:You’re very welcome, Ms. Jones. Take care, and don’t hesitate to reach out if you need anything.
"""

# Extract patient statements
patient_statements = [line.replace("Patient: ", "").strip() for line in transcript.split("\n") if line.startswith("Patient:")]

from transformers import pipeline

# Load sentiment analysis pipeline using DistiBert
sentiment_pipeline = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Load intent classification pipeline
intent_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Define possible intents
intent_labels = ["Seeking reassurance", "Reporting symptoms", "Expressing concern", "Describing an event", "General conversation"]

# Analyze each patient statement
results = []
for statement in patient_statements:
    # Sentiment Analysis
    sentiment_result = sentiment_pipeline(statement)[0]
    sentiment_label = "Reassured" if sentiment_result["label"] == "POSITIVE" else "Anxious"

    # Intent Detection
    intent_result = intent_pipeline(statement, intent_labels)
    intent_label = intent_result["labels"][0]  # Top intent

    # Store result
    results.append({"Statement": statement, "Sentiment": sentiment_label, "Intent": intent_label})

import json

print(json.dumps(results, indent=2))

#Answers for the Questions

print("1. How would you fine-tune BERT for sentimental detection?\n ANSWER:To fine-tune BERT for medical sentiment detection, I would start with a pre-trained BERT model, such as bert-base-uncased or a healthcare-specific variant \n like BioBERT or ClinicalBERT. The fine-tuning process involves supervised learning on labeled medical sentiment data, where patient statements are categorized into classes \n like Anxious, Neutral, or Reassured. I would prepare a dataset by tokenizing patient statements using WordPiece Tokenization, padding/truncating them to a fixed length, and feeding them into BERT.\n The model's classification head is then trained using cross-entropy loss with an optimizer like AdamW. TensorFlow/Keras can be used to fine-tune BERT efficiently, leveraging GPU acceleration.\n After training, evaluation on a test set using metrics like F1-score, accuracy, and recall ensures performance is clinically reliable.")

print("2. What datasets would you use for training a healthcare-specific sentiment model? \n ANSWER: For training a healthcare-specific sentiment model, I would need datasets containing patient-doctor dialogues, clinical notes, or patient feedback labeled with sentiment categories.\n I found Some relevant datasets include the n2c2 (National NLP Clinical Challenges) datasets, which consist of clinical narratives but may require additional labeling for sentiment analysis.\n Another valuable resource is CADEC (Corpus of Adverse Drug Event Conversations), a collection of patient forum discussions focused on drug effects, making it useful for understanding sentiment in medical contexts.\n Additionally, the i2b2 Clinical Text dataset contains de-identified patient records, which can be leveraged for training NLP models in the healthcare domain.\n These datasets provide a strong foundation for developing sentiment analysis models tailored to medical applications.")

