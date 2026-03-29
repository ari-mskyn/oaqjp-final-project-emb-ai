import json
from emotion_detection import emotion_detector

response = emotion_detector("I love this new technology")
formatted_response = json.loads(response)
emotion_predictions = formatted_response.get('emotionPredictions', [])
first_prediction = emotion_predictions[0]
emotions_dict = first_prediction['emotion']
dominant_emotion = max(emotions_dict, key=emotions_dict.get)
dominant_score = emotions_dict[dominant_emotion]

print(f"Dominant Emotion: {dominant_emotion} with score {dominant_score}")
