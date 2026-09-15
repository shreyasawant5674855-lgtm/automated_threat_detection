import unittest
import pandas as pd
import joblib


class TestAIModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = joblib.load("threat_detection_model.pkl")

    def test_model_loaded(self):
        self.assertIsNotNone(self.model)

    def test_model_prediction(self):
        data = pd.DataFrame(
            [[30000, 500]],
            columns=["bytes", "packets"]
        )

        prediction = self.model.predict(data)

        self.assertIn(prediction[0], [0, 1])

    def test_prediction_probability(self):
        data = pd.DataFrame(
            [[30000, 500]],
            columns=["bytes", "packets"]
        )

        probability = self.model.predict_proba(data)

        self.assertGreaterEqual(probability[0][0], 0)
        self.assertLessEqual(probability[0][0], 1)


if __name__ == "__main__":
    unittest.main()