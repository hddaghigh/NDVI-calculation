import unittest
import numpy as np


class TestNDVI(unittest.TestCase):
    def test_calculate(self):
        from calculate import ndvi_calculation

        # Test NDVI calculation when NIR and Red bands are equal
        #self.assertAlmostEqual(calculate(band_nir,band_red), 0)
        self.assertAlmostEqual(ndvi_calculation(np.array([1.0]),np.array([1.0])), np.array([0.0]))
        self.assertAlmostEqual(ndvi_calculation(np.array([-1.0]),np.array([-1.0])), np.array([0.0]))

if __name__ == '__main__':
    unittest.main()

## comment