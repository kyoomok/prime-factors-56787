from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def setUp(self):
        super().setUp()
        self.pf = PrimeFactor()

    def test_prime_factor_of_1(self):
        self.assertEqual([], self.pf.of(1))

    def test_prime_factor_of_2(self):
        self.assertEqual([2], self.pf.of(2))

    def test_prime_factor_of_3(self):
        self.assertEqual([3], self.pf.of(3))
