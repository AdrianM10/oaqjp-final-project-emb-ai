import requests
import logging
import json


def emotion_detector(text_to_analyze: str) -> str:

    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input, headers=header)

    # Check if response code is 200
    if response.status_code == 200:


        response_dictionary = response.json()

        anger = response_dictionary["emotionPredictions"][0]["emotion"]["anger"]
        disgust = response_dictionary["emotionPredictions"][0]["emotion"]["disgust"]
        fear = response_dictionary["emotionPredictions"][0]["emotion"]["fear"]
        joy = response_dictionary["emotionPredictions"][0]["emotion"]["joy"]
        sadness = response_dictionary["emotionPredictions"][0]["emotion"]["sadness"]
        
        
        emotions_payload_response = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
        }
    elif response.status_code == 400 or response.status_code == 500:
        emotions_payload_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
        }
    
    # retreive the most dominant emotion

    dominant_emotion_name = ""
    dominant_emotion_score = 0
    for key, value in emotions_payload_response.items():
        if (value >= dominant_emotion_score):
            dominant_emotion_name = key
            dominant_emotion_score = value

    # print(dominant_emotion_name) 
    emotions_payload_updated =  {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        "dominant_emotion": dominant_emotion_name
    }

    return emotions_payload_updated


