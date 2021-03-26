import numpy as np
import MeasuringnObservables as mo
import unittest

class test(unittest.TestCase):

    def testProb(self):
        ket = np.array([[1j], [2+3j], [5+1j]])
        pos = 1
        expected = 0.32
        self.assertTrue(
            np.testing.assert_almost_equal(mo.prob(ket, pos), expected) is None
        )

    def testTransitionProb(self):
        ket1 = np.array([[2 + 1j], [1 + 2j], [0], [-1 + 1j]])
        ket2 = np.array([[0], [1 - 3j], [2 - 1j], [1 + 2j]])
        expected = 80.0
        self.assertTrue(
            np.testing.assert_almost_equal(mo.transitionProb(ket1, ket2), expected) is None
        )

    def testVariance(self):
        obs = np.array([[0, -1j], [1j, 0]])
        ket = np.array([[1j], [-1j]])
        expected = 2
        self.assertTrue(
            np.testing.assert_almost_equal(mo.variance(obs, ket), expected) is None
        )

    def testEigenValues(self):
        obs = np.array([[0, -1j], [1j, 0]])
        expected = np.array([1+0j, -1+0j])
        self.assertTrue(
            np.testing.assert_almost_equal(mo.measures(obs), expected) is None
        )

    def testFinalStates(self):
        transformations = np.array([np.array([[(1 + 1j) / 2, (1 - 1j) / 2], [(1 - 1j) / 2, (1 + 1j) / 2]]),
                                    np.array([[1, 0], [0, 1j]])])
        ket = np.array([1j, 2j])
        expected = [0.5+1.5j, -1.5-0.5j]
        self.assertTrue(
            np.testing.assert_almost_equal(mo.finalStateDin(ket, transformations), expected) is None
        )

if __name__ == '__main__':
    unittest.main()
