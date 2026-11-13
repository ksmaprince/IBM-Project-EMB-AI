import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json=myobj, headers=header)
    status_code = response.status_code
    if status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    fromatted_response = json.loads(response.text)

    anger = fromatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = fromatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = fromatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = fromatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = fromatted_response['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(
        anger, disgust, fear, joy, sadness)

    if dominant_emotion == anger:
        dominant_emotion = 'anger'
    elif dominant_emotion == disgust:
        dominant_emotion = 'disgust'
    elif dominant_emotion == fear:
        dominant_emotion = 'fear'
    elif dominant_emotion == joy:
        dominant_emotion = 'joy'
    else:
        dominant_emotion = 'sadness'

    return {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
        "dominant_emotion": dominant_emotion
    }
