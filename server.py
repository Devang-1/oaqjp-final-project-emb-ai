"""
Flask server for Emotion Detection Web Application.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the main input page.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Process emotion detection request and display formatted results.
    """
    statement = request.form.get("statement", "")
    result = emotion_detector(statement)

    if result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 400

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == '__main__':
    app.run(debug=True)
