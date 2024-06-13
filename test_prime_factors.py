from unittest import TestCase

from prime_factors import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_calc(self):
        pf = PrimeFactor()
        self.assertEqual(pf.of(1), 1)
