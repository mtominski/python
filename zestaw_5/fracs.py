#!/usr/bin/env python3
# coding=utf-8

"""Zestaw 5 - Milosz Tominski

Zadanie 5.2: modul fracs, dzialania na ulamkach [licznik, mianownik].
"""

from collections.abc import Callable
from functools import wraps
from math import gcd
import doctest
import unittest

__all__ = ["add_frac", "sub_frac", "mul_frac", "div_frac",
           "is_positive", "is_zero", "cmp_frac", "frac2float"]

Frac = list[int]


def _check_frac(frac: Frac) -> None:
    """Zadanie 5.2: sprawdza typ i poprawnosc ulamka, rzuca wyjatek.

    >>> _check_frac([1, 2])
    >>> _check_frac([1, 0])
    Traceback (most recent call last):
        ...
    ValueError: mianownik nie moze byc zerem
    """
    if not isinstance(frac, (list, tuple)):
        raise TypeError("ulamek musi byc lista [licznik, mianownik]")
    if len(frac) != 2:
        raise ValueError("ulamek musi miec dokladnie dwa elementy")
    if not all(isinstance(x, int) and not isinstance(x, bool) for x in frac):
        raise TypeError("licznik i mianownik musza byc liczbami calkowitymi")
    if frac[1] == 0:
        raise ValueError("mianownik nie moze byc zerem")


def _check_args(func: Callable) -> Callable:
    """Zadanie 5.2: dekorator sprawdzajacy wszystkie argumenty-ulamki."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for frac in (*args, *kwargs.values()):
            _check_frac(frac)
        return func(*args, **kwargs)
    return wrapper


def _normalize(frac: Frac) -> Frac:
    """Zadanie 5.2: skraca ulamek, mianownik dodatni, zero jako [0, 1].

    >>> _normalize([6, -4])
    [-3, 2]
    >>> _normalize([0, -7])
    [0, 1]
    """
    num, den = frac
    divisor = gcd(num, den) if den > 0 else -gcd(num, den)
    return [num // divisor, den // divisor]


@_check_args
def add_frac(frac1: Frac, frac2: Frac) -> Frac:   # frac1 + frac2
    """Zadanie 5.2: zwraca sume ulamkow frac1 + frac2.

    >>> add_frac([1, 2], [1, 3])
    [5, 6]
    """
    (a, b), (c, d) = _normalize(frac1), _normalize(frac2)
    return _normalize([a * d + c * b, b * d])


@_check_args
def sub_frac(frac1: Frac, frac2: Frac) -> Frac:   # frac1 - frac2
    """Zadanie 5.2: zwraca roznice ulamkow frac1 - frac2.

    >>> sub_frac([1, 2], [1, 3])
    [1, 6]
    """
    num, den = frac2
    return add_frac(frac1, [-num, den])


@_check_args
def mul_frac(frac1: Frac, frac2: Frac) -> Frac:   # frac1 * frac2
    """Zadanie 5.2: zwraca iloczyn ulamkow frac1 * frac2.

    >>> mul_frac([1, 2], [2, 3])
    [1, 3]
    """
    (a, b), (c, d) = _normalize(frac1), _normalize(frac2)
    return _normalize([a * c, b * d])


@_check_args
def div_frac(frac1: Frac, frac2: Frac) -> Frac:   # frac1 / frac2
    """Zadanie 5.2: zwraca iloraz ulamkow frac1 / frac2.

    >>> div_frac([1, 2], [1, 3])
    [3, 2]
    >>> div_frac([1, 2], [0, 5])
    Traceback (most recent call last):
        ...
    ZeroDivisionError: dzielenie przez ulamek zerowy
    """
    (a, b), (c, d) = _normalize(frac1), _normalize(frac2)
    if c == 0:
        raise ZeroDivisionError("dzielenie przez ulamek zerowy")
    return _normalize([a * d, b * c])


@_check_args
def is_positive(frac: Frac) -> bool:   # bool, czy dodatni
    """Zadanie 5.2: sprawdza, czy ulamek jest dodatni.

    >>> is_positive([-1, -2])
    True
    """
    num, den = frac
    return num != 0 and (num > 0) == (den > 0)


@_check_args
def is_zero(frac: Frac) -> bool:   # bool, typu [0, x]
    """Zadanie 5.2: sprawdza, czy ulamek jest zerem.

    >>> is_zero([0, 5])
    True
    """
    return frac[0] == 0


@_check_args
def cmp_frac(frac1: Frac, frac2: Frac) -> int:   # -1 | 0 | +1
    """Zadanie 5.2: porownuje ulamki, zwraca -1, 0 albo +1.

    >>> cmp_frac([1, 2], [2, 4])
    0
    """
    num = sub_frac(frac1, frac2)[0]
    return (num > 0) - (num < 0)


@_check_args
def frac2float(frac: Frac) -> float:   # konwersja do float
    """Zadanie 5.2: zamienia ulamek na liczbe float.

    >>> frac2float([1, 4])
    0.25
    >>> frac2float([0, -5])
    0.0
    """
    num, den = _normalize(frac)
    return num / den


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def check_cases(self, func, cases):
        for *args, expected in cases:
            with self.subTest(func=func.__name__, args=args):
                self.assertEqual(func(*args), expected)

    def test_add_frac(self):
        self.check_cases(add_frac, [
            ([1, 2], [1, 3], [5, 6]),
            ([1, 2], [1, 2], [1, 1]),
            ([1, 2], [-1, 2], self.zero),
            ([1, -2], [1, 3], [-1, 6]),
            (self.zero, [3, 4], [3, 4]),
            ([6, 2], [0, 2], [3, 1]),
        ])

    def test_sub_frac(self):
        self.check_cases(sub_frac, [
            ([1, 2], [1, 3], [1, 6]),
            ([1, 3], [1, 2], [-1, 6]),
            ([3, 4], [3, 4], self.zero),
            ([-1, 2], [1, -2], self.zero),
            (self.zero, [2, 5], [-2, 5]),
        ])

    def test_mul_frac(self):
        self.check_cases(mul_frac, [
            ([1, 2], [2, 3], [1, 3]),
            ([-1, 2], [1, -2], [1, 4]),
            ([5, 7], self.zero, self.zero),
            ([6, 2], [1, 3], [1, 1]),
        ])

    def test_div_frac(self):
        self.check_cases(div_frac, [
            ([1, 2], [1, 3], [3, 2]),
            ([1, 2], [-1, 4], [-2, 1]),
            (self.zero, [5, 7], self.zero),
            ([3, 1], [6, 2], [1, 1]),
        ])
        for zero in (self.zero, [0, 2], [0, -5]):
            with self.subTest(divisor=zero):
                self.assertRaisesRegex(ZeroDivisionError, "ulamek zerowy",
                                       div_frac, [1, 2], zero)

    def test_is_positive(self):
        self.check_cases(is_positive, [
            ([1, 2], True),
            ([-1, -2], True),
            ([-1, 2], False),
            ([1, -2], False),
            (self.zero, False),
            ([0, -3], False),
        ])

    def test_is_zero(self):
        self.check_cases(is_zero, [
            (self.zero, True),
            ([0, 2], True),
            ([0, -5], True),
            ([1, 2], False),
            ([-1, 2], False),
        ])

    def test_cmp_frac(self):
        self.check_cases(cmp_frac, [
            ([1, 2], [1, 3], 1),
            ([1, 3], [1, 2], -1),
            ([1, 2], [2, 4], 0),
            ([-1, 2], [1, -2], 0),
            (self.zero, [0, 2], 0),
            ([3, 1], [6, 2], 0),
            ([-1, 2], self.zero, -1),
        ])

    def test_frac2float(self):
        self.check_cases(frac2float, [
            ([1, 2], 0.5),
            ([-1, 2], -0.5),
            ([1, -2], -0.5),
            ([6, 2], 3.0),
            (self.zero, 0.0),
        ])
        self.assertAlmostEqual(frac2float([1, 3]), 0.3333333)
        self.assertEqual(str(frac2float([0, -5])), "0.0")
        self.assertRaises(OverflowError, frac2float, [10 ** 400, 1])

    def test_decorator(self):
        self.assertEqual(add_frac.__name__, "add_frac")
        self.assertIn("Zadanie 5.2", add_frac.__doc__)
        self.assertEqual(add_frac(frac1=[1, 2], frac2=[1, 3]), [5, 6])
        self.assertEqual(sub_frac([1, 2], frac2=[1, 3]), [1, 6])
        self.assertRaisesRegex(TypeError, "liczbami calkowitymi",
                               add_frac, [1, 2], frac2=[1.5, 3])
        self.assertRaisesRegex(TypeError, "missing", add_frac, [1, 2])
        frac1, frac2 = [2, 4], [-3, -6]
        add_frac(frac1, frac2)
        self.assertEqual((frac1, frac2), ([2, 4], [-3, -6]))

    def test_tuples(self):
        self.check_cases(add_frac, [((1, 2), (1, 3), [5, 6])])
        self.check_cases(div_frac, [((1, 2), [1, 3], [3, 2])])
        self.check_cases(is_zero, [((0, 5), True)])
        self.check_cases(frac2float, [((3, 4), 0.75)])

    def test_all(self):
        self.assertEqual(len(__all__), 8)
        for name in __all__:
            with self.subTest(name=name):
                self.assertTrue(callable(globals()[name]))

    def test_invalid_arguments(self):
        binary = (add_frac, sub_frac, mul_frac, div_frac, cmp_frac)
        unary = (is_positive, is_zero, frac2float)
        good = [1, 2]
        cases = [
            (TypeError, "musi byc lista",
             [{1: "a", 2: "b"}, {3, 4}, "12", 5, None]),
            (TypeError, "liczbami calkowitymi",
             [[1.5, 2], [1.0, 2.0], ["1", "2"], [None, 2], [[1, 2], 3],
              [True, 2], [1, True]]),
            (ValueError, "dokladnie dwa elementy", [[], [1], [1, 2, 3]]),
            (ValueError, "mianownik nie moze byc zerem", [[1, 0], [0, 0]]),
        ]
        for error, message, bad_fracs in cases:
            for bad in bad_fracs:
                calls = [(func, (bad, good)) for func in binary]
                calls += [(func, (good, bad)) for func in binary]
                calls += [(func, (bad,)) for func in unary]
                for func, args in calls:
                    with self.subTest(func=func.__name__, args=args):
                        self.assertRaisesRegex(error, message, func, *args)

    def tearDown(self):
        pass


def load_tests(loader, tests, ignore):
    """Zadanie 5.2: dolacza doctesty z docstringow do testow unittest."""
    tests.addTests(doctest.DocTestSuite())
    return tests


if __name__ == '__main__':
    # uruchamia wszystkie testy
    unittest.main(verbosity=2)
