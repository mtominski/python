#!/usr/bin/env python3
# coding=utf-8

"""
Zestaw 6 - Milosz Tominski

Zadanie 6.2: testy modulu points.
"""

import copy
import doctest
import math
import operator
import unittest

import points
from points import Point


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 4)

    def check_cases(self, func, cases):
        for *args, expected in cases:
            with self.subTest(func=func.__name__, args=args):
                self.assertEqual(func(*args), expected)

    def test_print(self):
        self.check_cases(str, [
            (self.p1, "(1, 2)"),
            (Point(1.5, -2), "(1.5, -2)"),
        ])
        self.check_cases(repr, [
            (self.p1, "Point(1, 2)"),
            (Point(0.1, -3), "Point(0.1, -3)"),
        ])
        for point in (self.p1, Point(0.1, -2.5)):
            with self.subTest(point=point):
                self.assertEqual(eval(repr(point), {"Point": Point}), point)

    def test_eq_ne(self):
        self.check_cases(operator.eq, [
            (self.p1, Point(1, 2), True),
            (self.p1, Point(1.0, 2.0), True),
            (self.p1, Point(2, 1), False),
            (self.p1, (1, 2), False),
            (self.p1, None, False),
        ])
        self.check_cases(operator.ne, [
            (self.p1, Point(2, 1), True),
            (self.p1, Point(1, 2), False),
            (self.p1, (1, 2), True),
        ])

    def test_add(self):
        self.check_cases(operator.add, [
            (self.p1, self.p2, Point(4, 6)),
            (self.p1, Point(-1, -2), Point(0, 0)),
            (Point(0.5, 1), Point(0.25, 2), Point(0.75, 3)),
        ])

    def test_sub(self):
        self.check_cases(operator.sub, [
            (self.p1, self.p2, Point(-2, -2)),
            (self.p2, self.p1, Point(2, 2)),
            (self.p1, self.p1, Point(0, 0)),
        ])

    def test_mul(self):
        self.check_cases(operator.mul, [
            (self.p1, self.p2, 11),
            (Point(1, 0), Point(0, 1), 0),
            (Point(-2, 3), Point(4, 5), 7),
        ])

    def test_cross(self):
        self.check_cases(Point.cross, [
            (Point(1, 0), Point(0, 1), 1),
            (Point(0, 1), Point(1, 0), -1),
            (self.p1, Point(2, 4), 0),
            (self.p1, self.p2, -2),
        ])

    def test_length(self):
        self.check_cases(Point.length, [
            (self.p2, 5.0),
            (Point(-3, -4), 5.0),
            (Point(0, 0), 0.0),
        ])
        self.assertAlmostEqual(Point(1, 1).length(), math.sqrt(2))

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash(Point(1, 2)))
        self.assertEqual(len({self.p1, Point(1, 2), Point(2, 1)}), 2)
        self.assertEqual({self.p1: "a"}[Point(1.0, 2.0)], "a")

    def test_neg_abs_iter(self):
        self.check_cases(operator.neg, [
            (self.p1, Point(-1, -2)),
            (Point(-1.5, 0), Point(1.5, 0)),
        ])
        self.check_cases(abs, [
            (self.p2, 5.0),
            (Point(-3, -4), 5.0),
        ])
        x, y = self.p1
        self.assertEqual((x, y), (1, 2))
        self.assertEqual(tuple(self.p2), (3, 4))
        self.assertEqual(Point(*self.p1), self.p1)

    def test_immutable(self):
        points = {self.p1}
        for name, value in (("x", 5), ("y", 5), ("z", 5), ("X", 5)):
            with self.subTest(name=name):
                self.assertRaisesRegex(AttributeError, "niezmienny",
                                       setattr, self.p1, name, value)
        for name in ("x", "y"):
            with self.subTest(name=name):
                self.assertRaisesRegex(AttributeError, "niezmienny",
                                       delattr, self.p1, name)
        self.assertEqual(self.p1, Point(1, 2))
        self.assertIn(Point(1, 2), points)
        self.assertEqual(copy.copy(self.p1), self.p1)
        self.assertEqual(copy.deepcopy(self.p1), self.p1)

    def test_arguments_unchanged(self):
        self.p1 + self.p2
        self.p1 - self.p2
        self.assertEqual((self.p1, self.p2), (Point(1, 2), Point(3, 4)))

    def test_invalid_arguments(self):
        for x, y in (("1", 2), (None, 1), ([1], 2), (True, 1), (1, 1j)):
            with self.subTest(x=x, y=y):
                self.assertRaisesRegex(TypeError, "liczbami", Point, x, y)
        for x, y in ((math.nan, 1), (1, math.inf), (-math.inf, 0)):
            with self.subTest(x=x, y=y):
                self.assertRaisesRegex(ValueError, "skonczone", Point, x, y)
        for func in (operator.add, operator.sub, operator.mul):
            with self.subTest(func=func.__name__):
                self.assertRaises(TypeError, func, self.p1, (1, 2))
                self.assertRaises(TypeError, func, self.p1, 2)
        self.assertRaisesRegex(TypeError, "drugiego punktu",
                               self.p1.cross, (1, 2))

    def test_all(self):
        self.assertEqual(points.__all__, ["Point"])

    def tearDown(self):
        pass


def load_tests(loader, tests, ignore):
    """Zadanie 6.2: dolacza doctesty modulu points do testow unittest."""
    tests.addTests(doctest.DocTestSuite(points))
    return tests


if __name__ == "__main__":
    # uruchamia wszystkie testy
    unittest.main(verbosity=2)
