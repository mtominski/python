#!/usr/bin/env python3
# coding=utf-8

"""
Zestaw 6 - Milosz Tominski

Zadanie 6.5: testy modulu fracs.
"""

import copy
import doctest
import math
import operator
import unittest

import fracs
from fracs import Frac


class TestFrac(unittest.TestCase):

    def setUp(self):
        self.zero = Frac()
        self.half = Frac(1, 2)
        self.third = Frac(1, 3)

    def check_cases(self, func, cases):
        for *args, expected in cases:
            with self.subTest(func=func.__name__, args=args):
                self.assertEqual(func(*args), expected)

    def test_init(self):
        self.check_cases(lambda frac: (frac.x, frac.y), [
            (self.zero, (0, 1)),
            (Frac(5), (5, 1)),
            (Frac(6, 4), (3, 2)),
            (Frac(1, -2), (-1, 2)),
            (Frac(-6, -4), (3, 2)),
            (Frac(0, -7), (0, 1)),
        ])

    def test_print(self):
        self.check_cases(str, [
            (self.half, "1/2"),
            (Frac(-6, 4), "-3/2"),
            (Frac(4, 2), "2"),
            (self.zero, "0"),
        ])
        self.check_cases(repr, [
            (self.half, "Frac(1, 2)"),
            (Frac(4, 2), "Frac(2, 1)"),
            (self.zero, "Frac(0, 1)"),
        ])
        for frac in (self.half, Frac(-3, 2), self.zero):
            with self.subTest(frac=frac):
                self.assertEqual(eval(repr(frac), {"Frac": Frac}), frac)

    def test_cmp(self):
        self.check_cases(operator.eq, [
            (self.half, Frac(2, 4), True),
            (Frac(-1, 2), Frac(1, -2), True),
            (self.zero, Frac(0, 5), True),
            (Frac(6, 2), 3, True),
            (3, Frac(6, 2), True),
            (self.half, self.third, False),
            (self.half, 0.5, False),
            (self.half, "1/2", False),
        ])
        self.check_cases(operator.ne, [
            (self.half, self.third, True),
            (self.half, Frac(2, 4), False),
            (Frac(2), 2, False),
        ])
        self.check_cases(operator.lt, [
            (self.third, self.half, True),
            (self.half, self.third, False),
            (self.half, self.half, False),
            (self.half, 1, True),
            (0, self.half, True),
        ])
        self.check_cases(operator.le, [
            (self.third, self.half, True),
            (self.half, Frac(2, 4), True),
            (self.half, self.third, False),
            (1, self.half, False),
        ])
        self.check_cases(operator.gt, [
            (self.half, self.third, True),
            (self.third, self.half, False),
            (self.half, Frac(2, 4), False),
            (self.half, 0, True),
            (1, self.half, True),
        ])
        self.check_cases(operator.ge, [
            (self.half, Frac(2, 4), True),
            (self.half, self.third, True),
            (self.third, self.half, False),
            (Frac(-1, 2), 0, False),
        ])

    def test_add(self):
        self.check_cases(operator.add, [
            (self.half, self.third, Frac(5, 6)),
            (self.half, Frac(-1, 2), self.zero),
            (self.half, 1, Frac(3, 2)),
            (1, self.half, Frac(3, 2)),
        ])
        self.assertEqual(sum([self.half, self.third, Frac(1, 6)]), 1)

    def test_sub(self):
        self.check_cases(operator.sub, [
            (self.half, self.third, Frac(1, 6)),
            (self.third, self.half, Frac(-1, 6)),
            (self.half, 1, Frac(-1, 2)),
            (1, self.third, Frac(2, 3)),
        ])

    def test_mul(self):
        self.check_cases(operator.mul, [
            (self.half, Frac(2, 3), self.third),
            (Frac(-1, 2), Frac(1, -2), Frac(1, 4)),
            (self.half, self.zero, self.zero),
            (self.half, 4, Frac(2)),
            (4, self.half, Frac(2)),
        ])

    def test_div(self):
        self.check_cases(operator.truediv, [
            (self.half, self.third, Frac(3, 2)),
            (self.half, Frac(-1, 4), Frac(-2)),
            (self.zero, self.half, self.zero),
            (self.half, 2, Frac(1, 4)),
            (2, self.half, Frac(4)),
        ])
        self.assertEqual(self.half.__div__(self.third), Frac(3, 2))
        for divisor in (self.zero, Frac(0, 5), 0):
            with self.subTest(divisor=divisor):
                self.assertRaisesRegex(ZeroDivisionError, "zerowy",
                                       operator.truediv, self.half, divisor)
        self.assertRaises(ZeroDivisionError, operator.truediv, 1, self.zero)

    def test_floordiv_mod(self):
        self.check_cases(operator.floordiv, [
            (Frac(7, 2), self.third, 10),
            (Frac(-7, 2), 1, -4),
            (3, Frac(2, 3), 4),
        ])
        self.check_cases(operator.mod, [
            (Frac(7, 2), self.third, Frac(1, 6)),
            (Frac(-7, 2), 1, self.half),
            (Frac(7, 2), -1, Frac(-1, 2)),
            (3, Frac(2, 3), self.third),
        ])
        self.assertRaises(ZeroDivisionError, operator.mod, self.half, 0)

    def test_unary(self):
        self.check_cases(operator.pos, [(self.half, self.half)])
        self.check_cases(operator.neg, [
            (self.half, Frac(-1, 2)),
            (Frac(-1, 2), self.half),
            (self.zero, self.zero),
        ])
        self.check_cases(operator.invert, [
            (Frac(2, 3), Frac(3, 2)),
            (Frac(-2, 3), Frac(-3, 2)),
            (Frac(5), Frac(1, 5)),
        ])
        self.assertRaises(ZeroDivisionError, operator.invert, self.zero)

    def test_float_bool(self):
        self.check_cases(float, [
            (self.half, 0.5),
            (Frac(-1, 4), -0.25),
            (Frac(6, 2), 3.0),
        ])
        self.assertEqual(str(float(Frac(0, -5))), "0.0")
        self.assertAlmostEqual(float(self.third), 0.3333333)
        self.check_cases(bool, [
            (self.zero, False),
            (Frac(0, -3), False),
            (self.half, True),
            (Frac(-1, 2), True),
        ])

    def test_hash(self):
        self.assertEqual({2}, {Frac(2)})
        self.assertEqual({2, 2.0}, {Frac(4, 2)})
        self.assertEqual(len({self.half, Frac(2, 4), self.third}), 2)
        self.assertEqual({self.half: "a"}[Frac(-2, -4)], "a")
        big = 2 ** 53 + 1
        self.assertEqual(hash(Frac(big)), hash(big))
        self.assertEqual(len({Frac(10 ** 400), Frac(10 ** 400, 3)}), 2)

    def test_sorting(self):
        fracs = [Frac(1, 2), Frac(-1, 3), 1, Frac(1, 3), 0]
        self.assertEqual(sorted(fracs), [Frac(-1, 3), 0, Frac(1, 3),
                                         Frac(1, 2), 1])
        self.assertEqual(max(fracs), 1)
        self.assertEqual(min(fracs), Frac(-1, 3))

    def test_pow(self):
        self.check_cases(operator.pow, [
            (Frac(2, 3), 2, Frac(4, 9)),
            (Frac(2, 3), -2, Frac(9, 4)),
            (Frac(-1, 2), 3, Frac(-1, 8)),
            (Frac(5, 7), 0, 1),
            (self.zero, 0, 1),
            (self.zero, 3, self.zero),
        ])
        self.assertRaises(ZeroDivisionError, operator.pow, self.zero, -1)
        for exponent in (0.5, Frac(2), True, "2"):
            with self.subTest(exponent=exponent):
                self.assertRaises(TypeError, operator.pow, self.half, exponent)
        self.assertRaises(TypeError, operator.pow, 2, self.half)

    def test_floor_ceil_trunc(self):
        big = 2 ** 53 + 1
        cases = [
            (Frac(7, 2), 3, 4, 3),
            (Frac(-7, 2), -4, -3, -3),
            (Frac(4, 2), 2, 2, 2),
            (Frac(-1, 3), -1, 0, 0),
            (Frac(big), big, big, big),
            (Frac(2 * big + 1, 3), (2 * big + 1) // 3, (2 * big + 1) // 3 + 1,
             (2 * big + 1) // 3),
        ]
        for frac, floor, ceil, trunc in cases:
            with self.subTest(frac=frac):
                results = (math.floor(frac), math.ceil(frac), math.trunc(frac))
                self.assertEqual(results, (floor, ceil, trunc))
                self.assertTrue(all(type(r) is int for r in results))

    def test_format(self):
        self.check_cases(format, [
            (self.third, "", "1/3"),
            (Frac(2), "", "2"),
            (self.third, ".3f", "0.333"),
            (Frac(-7, 2), ".1f", "-3.5"),
            (self.half, ".2e", "5.00e-01"),
            (self.half, "%", "50.000000%"),
            (self.half, ">6", "   1/2"),
            (self.half, "*^7", "**1/2**"),
        ])
        self.assertEqual(f"{self.half} = {self.half:.2f}", "1/2 = 0.50")
        self.assertRaises(ValueError, format, self.half, "d")

    def test_abs_int_divmod(self):
        self.check_cases(abs, [
            (Frac(-1, 2), self.half),
            (self.half, self.half),
            (self.zero, self.zero),
        ])
        self.check_cases(int, [
            (Frac(7, 2), 3),
            (Frac(-7, 2), -3),
            (Frac(4, 2), 2),
            (Frac(-1, 3), 0),
        ])
        self.assertIs(type(int(Frac(7, 2))), int)
        self.check_cases(divmod, [
            (Frac(7, 2), 1, (3, self.half)),
            (Frac(-7, 2), 1, (-4, self.half)),
            (Frac(7, 2), self.third, (10, Frac(1, 6))),
            (3, Frac(2, 3), (4, self.third)),
        ])
        self.assertRaises(ZeroDivisionError, divmod, self.half, 0)

    def test_immutable(self):
        fracs = {self.half}
        alias = +self.half
        for name, value in (("x", 2), ("y", 0), ("z", 1), ("X", 1)):
            with self.subTest(name=name):
                self.assertRaisesRegex(AttributeError, "niezmienny",
                                       setattr, self.half, name, value)
        for name in ("x", "y"):
            with self.subTest(name=name):
                self.assertRaisesRegex(AttributeError, "niezmienny",
                                       delattr, self.half, name)
        self.assertEqual((self.half.x, self.half.y), (1, 2))
        self.assertEqual(alias, Frac(1, 2))
        self.assertIn(Frac(2, 4), fracs)
        self.assertEqual(copy.copy(self.half), self.half)
        self.assertEqual(copy.deepcopy(self.half), self.half)

    def test_arguments_unchanged(self):
        frac1, frac2 = Frac(1, 2), Frac(1, 3)
        frac1 + frac2
        frac1 / frac2
        -frac1
        self.assertEqual((frac1.x, frac1.y, frac2.x, frac2.y), (1, 2, 1, 3))

    def test_invalid_arguments(self):
        for x, y in (("1", 2), (1.5, 2), (1, 2.0), (None, 1), (True, 2),
                     (1, False), ([1], 2), (Frac(1, 2), 3)):
            with self.subTest(x=x, y=y):
                self.assertRaisesRegex(TypeError, "typu int", Frac, x, y)
        self.assertRaisesRegex(ZeroDivisionError, "mianownik", Frac, 1, 0)
        operations = (operator.add, operator.sub, operator.mul,
                      operator.truediv, operator.floordiv, operator.mod,
                      operator.pow, divmod,
                      operator.lt, operator.le, operator.gt, operator.ge)
        for func in operations:
            for other in (0.5, "1/2", None, [1, 2], True):
                with self.subTest(func=func.__name__, other=other):
                    self.assertRaises(TypeError, func, self.half, other)
                    self.assertRaises(TypeError, func, other, self.half)

    def test_all(self):
        self.assertEqual(fracs.__all__, ["Frac"])

    def tearDown(self):
        pass


def load_tests(loader, tests, ignore):
    """Zadanie 6.5: dolacza doctesty modulu fracs do testow unittest."""
    tests.addTests(doctest.DocTestSuite(fracs))
    return tests


if __name__ == "__main__":
    # uruchamia wszystkie testy
    unittest.main(verbosity=2)
