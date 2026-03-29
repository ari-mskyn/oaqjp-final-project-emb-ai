import unittest
import json
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test 1
        result_1 = emotion_detector("I am glad this happened")
        result_json_1 = json.loads(result_1)
        expected_dominant_emotion_1 = 'joy'  
        self.assertEqual(result_json_1.get('dominant_emotion'), expected_dominant_emotion_1)

        # Test 2
        result_2 = emotion_detector("I am really mad about this")
        result_json_2 = json.loads(result_2)
        expected_dominant_emotion_2 = 'anger'  
        self.assertEqual(result_json_2.get('dominant_emotion'), expected_dominant_emotion_2)


        # Test 3
        result_3 = emotion_detector("I feel disgusted just hearing about this")
        result_json_3 = json.loads(result_3)
        expected_dominant_emotion_3 = 'disgust'  
        self.assertEqual(result_json_3.get('dominant_emotion'), expected_dominant_emotion_3)


        # Test 4
        result_4 = emotion_detector("I am so sad about this")
        result_json_4 = json.loads(result_4)
        expected_dominant_emotion_4 = 'sadness'  
        self.assertEqual(result_json_4.get('dominant_emotion'), expected_dominant_emotion_4)

        # Test 5
        result_5 = emotion_detector("I am really afraid that this will happen")
        result_json_5 = json.loads(result_5)
        expected_dominant_emotion_5 = 'fear'  
        self.assertEqual(result_json_5.get('dominant_emotion'), expected_dominant_emotion_5)

    
if __name__ == '__main__':
    unittest.main()