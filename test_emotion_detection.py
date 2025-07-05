from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test if joy is dominant emotion
        response_joy = emotion_detector("I am glad this happened")
        self.assertEqual(response_joy["dominant_emotion"], "joy")

        # Test if anger is dominant emotion
        response_anger = emotion_detector("I am really mad about this")
        self.assertEqual(response_anger["dominant_emotion"], "anger")

        # Test if disgust is dominant emotion
        response_disgust = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response_disgust["dominant_emotion"], "disgust")

        # Test if sadness is dominant emotion
        response_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(response_sadness["dominant_emotion"], "sadness")

        # Test if fear is dominant emotion
        response_fear = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response_fear["dominant_emotion"], "fear")        
       
      
if __name__ == '__main__':
    unittest.main()
