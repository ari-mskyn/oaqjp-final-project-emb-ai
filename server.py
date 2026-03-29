"""Flask server for the Emotion Detection application."""
import json
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector


app=Flask(__name__)
@app.route('/emotionDetector')

def sent_emotion_detector():
    '''Function for detecting the emotion given a string from the user '''
    text_to_analyze = request.args.get('textToAnalyze')
    output_json_str = emotion_detector(text_to_analyze)
    output = json.loads(output_json_str)
    dominant_emotion = output.get('dominant_emotion', 'unknown')
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    scores = {k: v for k, v in output.items() if k!= 'dominant_emotion'}
    formatted_scores = [f"'{emotion}' : {score:.7f}" for emotion, score in scores.items()]

    if len(formatted_scores) > 1:
        response_scores = ', '.join(formatted_scores[:-1]) + ' and ' + formatted_scores[-1]
    else:
        response_scores = formatted_scores[0]

    return (f"For the given statement, the system response is {response_scores}. "
            f"The dominant emotion is {dominant_emotion}.")   
@app.route('/')
def render_index_page():
    '''Function that builds the index.html from the template'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
