from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
import json

app = Flask(__name__)

EXPECTED_KEYS = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']

@app.route('/emotionDetector')
def sent_emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze or text_to_analyze.strip() == "":
        none_response = {key: None for key in EXPECTED_KEYS}
        return jsonify(none_response), 400

    try:
        output_json_str = emotion_detector(text_to_analyze)
        output = json.loads(output_json_str)

        dominant_emotion = output.get('dominant_emotion', 'unknown')
        scores = {k: v for k, v in output.items() if k != 'dominant_emotion'}
        formatted_scores = [f"'{emotion}': {score:.7f}" for emotion, score in scores.items()]

        if len(formatted_scores) > 1:
            response_scores = ', '.join(formatted_scores[:-1]) + ' and ' + formatted_scores[-1]
        else:
            response_scores = formatted_scores[0]

        response_text = (f"For the given statement, the system response is {response_scores}. "
                         f"The dominant emotion is {dominant_emotion}.")

        # Return the formatted response text in JSON so it can be shown to the user
        return jsonify({"response": response_text}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse emotion detector output"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)