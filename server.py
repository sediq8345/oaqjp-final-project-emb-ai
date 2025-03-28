"""
This is the server file for the emotion detection application.
It exposes a POST endpoint `/emotionDetector` to analyze emotions from text input.
"""
from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route('/emotionDetector', methods=['POST'])
def analyze_emotion():
    """
    This function handles the POST request to the /emotionDetector endpoint.
    It receives text input, analyzes the emotions using the emotion_detector function,
    and returns the emotion analysis as a JSON response.
    If no dominant emotion is found, it returns an error message.
    """
    text_to_analyze = request.json.get('text', '')
    # Get the emotion analysis result from the emotion_detector function
    result = emotion_detector(text_to_analyze)
    # Check if dominant_emotion is None
    if result['dominant_emotion'] is None:
        return jsonify({'message': 'Invalid text! Please try again!'}), 400
    # If the dominant emotion is not None, return the analysis result
    return jsonify({
        'anger': result['anger'],
        'disgust': result['disgust'],
        'fear': result['fear'],
        'joy': result['joy'],
        'sadness': result['sadness'],
        'dominant_emotion': result['dominant_emotion']
    }), 200
if __name__ == '__main__':
    app.run(debug=True)
