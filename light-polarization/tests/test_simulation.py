import unittest
from src.simulation import generate_circularly_polarized_light, generate_elliptically_polarized_light

class TestLightPolarization(unittest.TestCase):

    def test_generate_circularly_polarized_light(self):
        amplitude = 1.0
        frequency = 1.0
        phase_shift = 0.0
        result = generate_circularly_polarized_light(amplitude, frequency, phase_shift)
        self.assertEqual(len(result), 100)  # Assuming the function returns 100 samples
        # Additional assertions can be added based on expected properties of the output

    def test_generate_elliptically_polarized_light(self):
        amplitude_x = 1.0
        amplitude_y = 0.5
        frequency = 1.0
        phase_shift_x = 0.0
        phase_shift_y = 1.57  # 90 degrees in radians
        result = generate_elliptically_polarized_light(amplitude_x, amplitude_y, frequency, phase_shift_x, phase_shift_y)
        self.assertEqual(len(result), 100)  # Assuming the function returns 100 samples
        # Additional assertions can be added based on expected properties of the output

if __name__ == '__main__':
    unittest.main()