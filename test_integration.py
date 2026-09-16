import unittest
import joblib

from threat_detector import detect_threat


class TestSystemIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = joblib.load("threat_detection_model.pkl")

    def test_threat_detection_integration(self):
        result = detect_threat(
            self.model,
            30000,
            500
        )

        self.assertEqual(result, "Threat Detected")

    def test_system_returns_valid_result(self):
        result = detect_threat(
            self.model,
            5000,
            50
        )

        self.assertIn(
            result,
            ["Threat Detected", "Normal Activity"]
        )


if __name__ == "__main__":
    unittest.main()