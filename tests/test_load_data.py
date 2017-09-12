from unittest import TestCase


class TestLoad_data(TestCase):
    def test_load_data(self):
        from build import load_data
        import numpy as np

        X, y = load_data()

        self.assertTrue(X.shape, (442,10))
        self.assertTrue(np.sum((y[:20] == np.array([151., 75., 141., 206., 135., 97., 138.,
                                                    63., 110., 310., 101., 69., 179., 185.,
                                                    118., 171., 166., 144., 97., 168.
                                                    ]))), 20)