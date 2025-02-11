import json
import requests

def emotion_detector(text_to_analyze) :
    """
    Detect the main emotion of a given text using 
    Emotion Predict Function of Watson NLP Library
    
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_text = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input_text, headers = header, timeout=30)
    if response.status_code == 400:
        emotion = {"anger": None, "disgust": None, "fear": None, 
                    "joy": None, "sadness": None, "dominant_emotion":None}
        return emotion
    formatted_response = json.loads(response.text)
    emotion = formatted_response["emotionPredictions"][0]["emotion"]
    emotion["dominant_emotion"] = max(emotion, key=emotion.get)
    return emotion