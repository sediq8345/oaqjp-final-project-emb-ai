import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Check for blank input
    if not text_to_analyze.strip():  # If the input is blank
        # Return a dictionary with None values for all emotions
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Construct the payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Send the request to Watson NLP EmotionPredict API
        response = requests.post(url, headers=headers, json=payload)
        # Check for status_code 400 for blank or invalid input
        if response.status_code == 400:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        # Parse the response
        response_json = response.json()
        # Extract emotions from the response
        emotions = response_json['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)  # Get the dominant emotion

        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    except Exception as e:
        # If any error occurs in making the request or parsing the response
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }