import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url,json=data,headers=headers)
    fmt_response = json.loads(response.text)

    emotion_predictions = fmt_response['emotionPredictions']
    emotion_scores = emotion_predictions[0]['emotion']
    dominant_emotion = max_key = max(emotion_scores, key=emotion_scores.get)

    fmt_output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return fmt_output
