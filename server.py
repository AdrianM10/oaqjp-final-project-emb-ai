

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render HTML template"""
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_emotion():
    """
    Process input from user and return a custom message with scores
    for each emotion and the dominant emotion
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Check if values in dictionary are None
    for key, value in response.items():
        if value is None:
            return "Invalid text! Please try again!."
        else:
            message = f"For the given statement, the system response is 'anger':"
            message += f"{response['anger']}, 'disgust': {response['disgust']},"
            message += f" 'fear': {response['fear']},"
            message += f"'joy': {response['joy']} and 'sadness': {response['sadness']}."
            message += f"The dominant emotion is {response['dominant_emotion']}."
            return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)