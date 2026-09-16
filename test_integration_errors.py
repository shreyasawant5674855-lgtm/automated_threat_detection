import unittest


class TestIntegrationErrors(unittest.TestCase):

    def test_invalid_input(self):
        bytes_value = "abc"
        packets_value = "xyz"

        with self.assertRaises(ValueError):
            float(bytes_value)
            float(packets_value)


if __name__ == "__main__":
    unittest.main()