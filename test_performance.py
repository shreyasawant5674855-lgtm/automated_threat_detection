import unittest
import joblib
import time

from threat_detector import detect_threat


class TestSystemPerformance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = joblib.load("threat_detection_model.pkl")

    def test_multiple_scenarios(self):
        scenarios = [
            [5000, 50],
            [12000, 100],
            [25000, 400],
            [30000, 500]
        ]

        start_time = time.time()

        for bytes_value, packets_value in scenarios:
            result = detect_threat(
                self.model,
                bytes_value,
                packets_value
            )

            self.assertIn(
                result,
                ["Threat Detected", "Normal Activity"]
            )

        end_time = time.time()

        total_time = end_time - start_time

        print("\nPerformance Test")
        print("----------------")
        print("Scenarios tested:", len(scenarios))
        print("Total time:", round(total_time, 6), "seconds")

        self.assertLess(total_time, 5)


if __name__ == "__main__":
    unittest.main()