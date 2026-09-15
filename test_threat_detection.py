import unittest
import pandas as pd
import joblib


class TestThreatDetection(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = joblib.load("threat_detection_model.pkl")

    def test_threat_detection(self):
        data = pd.DataFrame(
            [[30000, 500]],
            columns=["bytes", "packets"]
        )

        prediction = self.model.predict(data)

        self.assertEqual(prediction[0], 1)

    def test_prediction_output(self):
        data = pd.DataFrame(
            [[5000, 50]],
            columns=["bytes", "packets"]
        )

        prediction = self.model.predict(data)

        self.assertIn(prediction[0], [0, 1])


if __name__ == "__main__":
    unittest.main()