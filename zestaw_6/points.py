#!/usr/bin/env python3
# coding=utf-8

"""
Zestaw 6 - Milosz Tominski

Zadanie 6.2: modul points, klasa Point reprezentujaca punkty na plaszczyznie.
"""

import doctest
import math

__all__ = ["Point"]


class Point:
    """Klasa reprezentujaca punkty na plaszczyznie.

    >>> p, q = Point(1, 2), Point(3, 4)
    >>> print(p, repr(q))
    (1, 2) Point(3, 4)
    >>> p + q, p - q, -p, p == Point(1.0, 2.0), p != q
    (Point(4, 6), Point(-2, -2), Point(-1, -2), True, True)
    >>> p * q, p.cross(q), q.length(), abs(q)
    (11, -2, 5.0, 5.0)
    >>> x, y = p
    >>> x, y, len({p, Point(1, 2), q})
    (1, 2, 2)
    >>> p.x = 5
    Traceback (most recent call last):
        ...
    AttributeError: punkt jest niezmienny
    """

    def __init__(self, x, y):  # konstruktor
        """Zadanie 6.2: tworzy punkt (x, y), wspolrzedne to int lub float."""
        for value in (x, y):
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise TypeError("wspolrzedne punktu musza byc liczbami")
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError("wspolrzedne punktu musza byc skonczone")
        self.x = x
        self.y = y

    def __setattr__(self, name, value):
        """Zadanie 6.2: pozwala ustawic x i y tylko raz, w __init__."""
        if name not in ("x", "y") or hasattr(self, name):
            raise AttributeError("punkt jest niezmienny")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        """Zadanie 6.2: blokuje usuwanie atrybutow punktu."""
        raise AttributeError("punkt jest niezmienny")

    def __str__(self):  # zwraca string "(x, y)"
        """Zadanie 6.2: zwraca napis "(x, y)"."""
        return f"({self.x}, {self.y})"

    def __repr__(self):  # zwraca string "Point(x, y)"
        """Zadanie 6.2: zwraca napis "Point(x, y)"."""
        return f"Point({self.x!r}, {self.y!r})"

    def __eq__(self, other):  # obsluga point1 == point2
        """Zadanie 6.2: sprawdza, czy punkty maja te same wspolrzedne."""
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):  # obsluga point1 != point2
        """Zadanie 6.2: sprawdza, czy punkty sa rozne."""
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        """Zadanie 6.2: zwraca sume wektorow."""
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        """Zadanie 6.2: zwraca roznice wektorow."""
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbe
        """Zadanie 6.2: zwraca iloczyn skalarny wektorow."""
        if not isinstance(other, Point):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D, zwraca liczbe
        """Zadanie 6.2: zwraca iloczyn wektorowy 2D."""
        if not isinstance(other, Point):
            raise TypeError("iloczyn wektorowy wymaga drugiego punktu")
        return self.x * other.y - self.y * other.x

    def length(self):  # dlugosc wektora
        """Zadanie 6.2: zwraca dlugosc wektora."""
        return math.hypot(self.x, self.y)

    def __neg__(self):  # -v
        """Zadanie 6.2: zwraca wektor przeciwny."""
        return Point(-self.x, -self.y)

    def __abs__(self):  # abs(v), to samo co length()
        """Zadanie 6.2: zwraca dlugosc wektora."""
        return self.length()

    def __iter__(self):  # x, y = v
        """Zadanie 6.2: pozwala rozpakowac punkt na wspolrzedne."""
        return iter((self.x, self.y))

    def __hash__(self):
        """Zadanie 6.2: zwraca hash punktu, punkty sa niezmienne."""
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points


if __name__ == "__main__":
    # przyklady z docstringow, pelne testy sa w pliku test_points.py
    print(doctest.testmod())
