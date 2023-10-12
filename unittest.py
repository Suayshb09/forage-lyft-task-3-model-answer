import unittest
from your_module import SpindlerBattery  # Replace 'your_module' with the actual module where the class is defined

class TestSpindlerBattery(unittest.TestCase):
    def test_check_service(self):
        # Create an instance of the SpindlerBattery class
        battery = SpindlerBattery()

        # Test with valid parameters
        self.assertTrue(battery.check_service(2))  # Service required every 2 years

        # Test with valid parameters
        self.assertFalse(battery.check_service(1))  # Service not required within 1 year

    def test_service_required(self):
        # Create an instance of the SpindlerBattery class
        battery = SpindlerBattery()

        # Test with valid parameters
        self.assertTrue(battery.service_required())

if __name__ == '__main__':
    unittest.main()
