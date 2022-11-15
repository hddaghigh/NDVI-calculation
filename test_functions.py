import unittest

class TestNDVI(unittest.TestCase):
    def test_ndviCalculation(self):
        from calculate import calculate

        # Test NDVI calculation when NIR and Red bands are equal
        self.assertAlmostEqual(calculate(band_nir,band_red), 0)
        self.assertAlmostEqual(calculate(1,1), 0)
        self.assertAlmostEqual(calculate(-1,-1), 0)






if __name__ == '__main__':
    unittest.main()

