from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test if joy is dominant emotion
        response_joy = emotion_detector("I am glad this happened")
        self.assertEqual(response_joy['dominant_emotion'], 'joy')
       
      
if __name__ == '__main__':
    unittest.main()
