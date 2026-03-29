import unittest
import json
from emotion_detection import emotion_detector

class EmotionDetector(unittest.TestCase):
    def emotion_detector(self):
        # Test 1
        result_1 = emotion_detector("I love this new technology")
        result_json_1 = json.loads(result_1)
        emotions_1 = result_json_1['emotionPredictions'][0]['emotion']
        dominant_emotion_1 = max(emotions_1, key=emotions_1.get)
        self.assertEqual(dominant_emotion_1, 'joy')

        # Test 2
        result_2 = sentiment_analyzer("I hate working with Python")
        result_json_2 = json.loads(result_2)
        emotions_2 = result_json_2['emotionPredictions'][0]['emotion']
        dominant_emotion_2 = max(emotions_2, key=emotions_2.get)
        self.assertEqual(dominant_emotion_2, 'disgust')

        # Test 3
        result_3 = sentiment_analyzer("I am neutral on Python")
        result_json_3 = json.loads(result_3)
        emotions_3 = result_json_3['emotionPredictions'][0]['emotion']
        dominant_emotion_3 = max(emotions_3, key=emotions_3.get)
        self.assertIsInstance(dominant_emotion_3, str)  # just check it returns a string

if __name__ == '__main__':
    unittest.main()