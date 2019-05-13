# norm_spec.py
import unittest
from normal_distribution import *


class TestNorm(unittest.TestCase):
  def test_get_samples(self):
    mu, sigma = 0., 1.
    sample_size = (100,)
    samples = get_samples(mu, sigma, sample_size)

    print(samples.shape)


if __name__ == '__main__':
  unittest.main()

