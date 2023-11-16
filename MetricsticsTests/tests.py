import unittest
from Metricstics import Metricstics


class MetricsticsTest(unittest.TestCase):

    def initialSetUp(self):
        # Create test data for each test case
        self.data = [1, 2, 3, 4, 5]
        self.metrics = Metricstics(self.data)

    def testing_mean(self):
        self.assertEqual(self.metrics.mean(), 3.0)

    def testing_median(self):
        self.assertEqual(self.metrics.median(), 3)

    def testing_mode(self):
        self.assertEqual(self.metrics.mode(), [1, 2, 3, 4, 5])

    def testing_standard_deviation(self):
        self.assertAlmostEqual(self.metrics.standard_deviation(), 1.5811, places=4)

    def testing_mean_absolute_deviation(self):
        self.assertEqual(self.metrics.mean_absolute_deviation(), 1.2)

    def testing_min(self):
        self.assertEqual(self.metrics.minimum(), (1, 5))

    def testing_max(self):
        self.assertEqual(self.metrics.maximum(), (2, 3))

    def testing_empty_data(self):
        metrics = Metricstics([])
        self.assertEqual(metrics.mean(), 0)
        self.assertIsNone(metrics.median())
        self.assertEqual(metrics.mode(), [])
        self.assertEqual(metrics.standard_deviation(), 0)
        self.assertEqual(metrics.mean_absolute_deviation(), 0)
        self.assertEqual(metrics.minimum(), (None, None))
        self.assertEqual(metrics.maximum(), (None, None))

    def testing_single_data_point(self):
        metrics = Metricstics([5])
        self.assertEqual(metrics.mean(), 5)
        self.assertEqual(metrics.median(), 5)
        self.assertEqual(metrics.mode(), [5])
        self.assertEqual(metrics.standard_deviation(), 0)
        self.assertEqual(metrics.mean_absolute_deviation(), 0)
        self.assertEqual(metrics.minimum(), (5, 5))
        self.assertEqual(metrics.maximum(), (5, 5))

    def testing_negative_numbers(self):
        metrics = Metricstics([-1, -2, -3, -4, -5])
        self.assertEqual(metrics.mean(), -3.0)
        self.assertEqual(metrics.median(), -3)
        self.assertEqual(metrics.mode(), [-5, -4, -3, -2, -1])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.5811, places=4)
        self.assertEqual(metrics.mean_absolute_deviation(), 1.2)
        self.assertEqual(metrics.minimum(), (-5, -1))
        self.assertEqual(metrics.maximum(), (-5, -3))

    def testing_floating_point_numbers(self):
        metrics = Metricstics([1.5, 2.5, 3.5])
        self.assertAlmostEqual(metrics.mean(), 2.5, places=4)
        self.assertAlmostEqual(metrics.median(), 2.5, places=4)
        self.assertEqual(metrics.mode(), [1.5, 2.5, 3.5])
        self.assertAlmostEqual(metrics.standard_deviation(), 0.8165, places=4)
        self.assertAlmostEqual(metrics.mean_absolute_deviation(), 0.6667, places=4)
        self.assertEqual(metrics.minimum(), (1.5, 3.5))
        self.assertEqual(metrics.maximum(), (2.5, 3.5))

    def testing_duplicate_values(self):
        metrics = Metricstics([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5])
        self.assertAlmostEqual(metrics.mean(), 3.0)
        self.assertEqual(metrics.median(), 3)
        self.assertEqual(metrics.mode(), [3, 4, 5])
        self.assertAlmostEqual(metrics.standard_deviation(), 1.0, places=4)
        self.assertAlmostEqual(metrics.mean_absolute_deviation(), 0.8, places=4)
        self.assertEqual(metrics.minimum(), (1, 5))
        self.assertEqual(metrics.maximum(), (1, 5))

    def testing_large_data_set(self):
        data = list(range(1, 10001))
        metrics = Metricstics(data)
        self.assertEqual(metrics.mean(), 5000.5)
        self.assertEqual(metrics.median(), 5000)
        self.assertEqual(metrics.mode(), [1])
        self.assertAlmostEqual(metrics.standard_deviation(), 2886.8956, places=4)
        self.assertAlmostEqual(metrics.mean_absolute_deviation(), 2886.5, places=4)
        self.assertEqual(metrics.minimum(), (1, 10000))
        self.assertEqual(metrics.maximum(), (1, 10000))

    def testing_mixed_data_types(self):
        metrics = Metricstics([1, 2, 3, 4, "5"])
        with self.assertRaises(TypeError):
            metrics.mean()
        with self.assertRaises(TypeError):
            metrics.median()
        with self.assertRaises(TypeError):
            metrics.mode()
        with self.assertRaises(TypeError):
            metrics.standard_deviation()
        with self.assertRaises(TypeError):
            metrics.mean_absolute_deviation()
        with self.assertRaises(TypeError):
            metrics.minimum()
        with self.assertRaises(TypeError):
            metrics.maximum()


if __name__ == '__main__':
    unittest.main()
