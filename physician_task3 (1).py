# -*- coding: utf-8 -*-
"""Physician_Task3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F6gbKWPwRtAKmrY-EHxIUdUYTvwH8_hx
"""

import spacy

nlp=spacy.load("en_core_web_sm")

import json
import re

def extract_soap(transcript):

    # Preprocessing: Splitting physician and patient dialogues
    lines = transcript.strip().split("\n")
    subjective = {
        "Chief_Complaint": "",
        "History_of_Present_Illness": ""
    }
    objective = {
        "Physical_Exam": "",
        "Observations": ""
    }
    assessment = {
        "Diagnosis": "",
        "Severity": ""
    }
    plan = {
        "Treatment": "",
        "Follow-Up": ""
    }

    # Extracting information from transcript
    for line in lines:
        line = line.strip()
        if line.startswith("Patient:"):
            doc = nlp(line)
            text = line.replace("Patient:", "").strip()
            # Identifying chief complaints
            if "pain" in text.lower() or "discomfort" in text.lower():
                subjective["Chief_Complaint"] = text
            # Extracting history
            if "accident" in text.lower():
                subjective["History_of_Present_Illness"] = text
        elif line.startswith("Physician:"):
            text = line.replace("Physician:", "").strip()

            if "full range of movement" in text.lower() or "no tenderness" in text.lower():
                objective["Physical_Exam"] = text

            if "diagnosis" in text.lower() or "injury" in text.lower():
                assessment["Diagnosis"] = text

            if "treatment" in text.lower() or "physiotherapy" in text.lower():
                plan["Treatment"] = text

            if "follow-up" in text.lower() or "return if" in text.lower():
                plan["Follow-Up"] = text

    soap_note = {
        "Subjective": subjective,
        "Objective": objective,
        "Assessment": assessment,
        "Plan": plan
    }

    return json.dumps(soap_note, indent=4)

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

soap_output = extract_soap(transcript)
print(soap_output)

