import unittest
import joblib

from threat_detector import detect_threat


class TestAIIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = joblib.load("threat_detection_model.pkl")

    def test_multiple_network_inputs(self):
        test_cases = [
            [30000, 500],
            [5000, 50],
            [25000, 400],
            [12000, 100]
        ]

        for bytes_value, packets_value in test_cases:
            result = detect_threat(
                self.model,
                bytes_value,
                packets_value
            )

            self.assertIn(
                result,
                ["Threat Detected", "Normal Activity"]
            )


if __name__ == "__main__":
    unittest.main()