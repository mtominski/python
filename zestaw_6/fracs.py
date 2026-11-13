#!/usr/bin/env python3
# coding=utf-8

"""
Zestaw 6 - Milosz Tominski

Zadanie 6.5: modul fracs, klasa Frac reprezentujaca ulamek.
"""

from functools import wraps
from math import gcd
import doctest

__all__ = ["Frac"]


def _frac_other(method):
    """Zadanie 6.5: dekorator zamieniajacy argument other z int na Frac.

    Dla typow innych niz Frac i int metoda zwraca NotImplemented,
    wiec Python sprobuje dzialania po stronie drugiego argumentu.
    """
    @wraps(method)
    def wrapper(self, other):
        if isinstance(other, int) and not isinstance(other, bool):
            other = Frac(other)
        elif not isinstance(other, Frac):
            return NotImplemented
        return method(self, other)
    return wrapper


class Frac:
    """Klasa reprezentujaca ulamek.

    >>> a, b = Frac(1, 2), Frac(1, 3)
    >>> a + b, a - b, a * b, a / b
    (Frac(5, 6), Frac(1, 6), Frac(1, 6), Frac(3, 2))
    >>> a // b, a % b, divmod(a, b), a ** -2
    (1, Frac(1, 6), (1, Frac(1, 6)), Frac(4, 1))
    >>> 1 + a, 1 - b, 3 * b, 1 / a
    (Frac(3, 2), Frac(2, 3), Frac(1, 1), Frac(2, 1))
    >>> a > b, a == Frac(2, 4), Frac(6, 2) == 3, sorted([a, 0, b])
    (True, True, True, [0, Frac(1, 3), Frac(1, 2)])
    >>> import math
    >>> -a, abs(-a), ~a, int(Frac(-7, 2)), math.floor(Frac(-7, 2))
    (Frac(-1, 2), Frac(1, 2), Frac(2, 1), -3, -4)
    >>> print(Frac(6, -4), Frac(4, 2), f"{b:.3f}", float(a), bool(Frac()))
    -3/2 2 0.333 0.5 False
    >>> {2} == {Frac(2)}
    True
    >>> a.x = 5
    Traceback (most recent call last):
        ...
    AttributeError: ulamek jest niezmienny
    """

    def __init__(self, x=0, y=1):
        """Zadanie 6.5: tworzy skrocony ulamek x/y z dodatnim mianownikiem."""
        for value in (x, y):
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError("licznik i mianownik musza byc typu int")
        if y == 0:
            raise ZeroDivisionError("mianownik nie moze byc zerem")
        divisor = gcd(x, y) if y > 0 else -gcd(x, y)
        self.x = x // divisor
        self.y = y // divisor

    def __setattr__(self, name, value):
        """Zadanie 6.5: pozwala ustawic x i y tylko raz, w __init__."""
        if name not in ("x", "y") or hasattr(self, name):
            raise AttributeError("ulamek jest niezmienny")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        """Zadanie 6.5: blokuje usuwanie atrybutow ulamka."""
        raise AttributeError("ulamek jest niezmienny")

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        """Zadanie 6.5: zwraca napis "x/y" albo "x" dla y = 1."""
        return str(self.x) if self.y == 1 else f"{self.x}/{self.y}"

    def __repr__(self):  # zwraca "Frac(x, y)"
        """Zadanie 6.5: zwraca napis "Frac(x, y)"."""
        return f"Frac({self.x}, {self.y})"

    @_frac_other
    def __eq__(self, other):
        """Zadanie 6.5: sprawdza rownosc ulamkow, takze z int."""
        return (self.x, self.y) == (other.x, other.y)

    def __ne__(self, other):
        """Zadanie 6.5: sprawdza, czy ulamki sa rozne."""
        return not self == other

    @_frac_other
    def __lt__(self, other):
        """Zadanie 6.5: sprawdza, czy ulamek jest mniejszy."""
        return self.x * other.y < other.x * self.y

    @_frac_other
    def __le__(self, other):
        """Zadanie 6.5: sprawdza, czy ulamek jest mniejszy lub rowny."""
        return self.x * other.y <= other.x * self.y

    @_frac_other
    def __gt__(self, other):
        """Zadanie 6.5: sprawdza, czy ulamek jest wiekszy (potrzebne z int)."""
        return self.x * other.y > other.x * self.y

    @_frac_other
    def __ge__(self, other):
        """Zadanie 6.5: sprawdza, czy ulamek jest wiekszy lub rowny."""
        return self.x * other.y >= other.x * self.y

    @_frac_other
    def __add__(self, other):  # frac1 + frac2
        """Zadanie 6.5: zwraca sume ulamkow."""
        return Frac(self.x * other.y + other.x * self.y, self.y * other.y)

    __radd__ = __add__

    @_frac_other
    def __sub__(self, other):  # frac1 - frac2
        """Zadanie 6.5: zwraca roznice ulamkow."""
        return Frac(self.x * other.y - other.x * self.y, self.y * other.y)

    @_frac_other
    def __rsub__(self, other):  # int - frac
        """Zadanie 6.5: odejmowanie z liczba int po lewej stronie."""
        return other - self

    @_frac_other
    def __mul__(self, other):  # frac1 * frac2
        """Zadanie 6.5: zwraca iloczyn ulamkow."""
        return Frac(self.x * other.x, self.y * other.y)

    __rmul__ = __mul__

    def __div__(self, other):  # frac1 / frac2, Py2
        """Zadanie 6.5: dzielenie z Pythona 2, to samo co __truediv__."""
        return self.__truediv__(other)

    @_frac_other
    def __truediv__(self, other):  # frac1 / frac2, Py3
        """Zadanie 6.5: zwraca iloraz ulamkow."""
        if other.x == 0:
            raise ZeroDivisionError("dzielenie przez ulamek zerowy")
        return self * ~other

    @_frac_other
    def __rtruediv__(self, other):  # int / frac
        """Zadanie 6.5: dzielenie z liczba int po lewej stronie."""
        return other / self

    @_frac_other
    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        """Zadanie 6.5: zwraca czesc calkowita ilorazu (int)."""
        quotient = self / other
        return quotient.x // quotient.y

    @_frac_other
    def __rfloordiv__(self, other):  # int // frac
        """Zadanie 6.5: dzielenie calkowite z liczba int po lewej stronie."""
        return other // self

    @_frac_other
    def __mod__(self, other):  # frac1 % frac2, opcjonalnie
        """Zadanie 6.5: zwraca reszte z dzielenia, znak jak u dzielnika."""
        return self - other * (self // other)

    @_frac_other
    def __rmod__(self, other):  # int % frac
        """Zadanie 6.5: reszta z dzielenia z liczba int po lewej stronie."""
        return other % self

    @_frac_other
    def __divmod__(self, other):  # divmod(frac1, frac2)
        """Zadanie 6.5: zwraca pare (frac1 // frac2, frac1 % frac2)."""
        return self // other, self % other

    @_frac_other
    def __rdivmod__(self, other):  # divmod(int, frac)
        """Zadanie 6.5: divmod z liczba int po lewej stronie."""
        return divmod(other, self)

    def __pow__(self, n):  # frac ** n, n calkowite
        """Zadanie 6.5: zwraca potege ulamka o wykladniku calkowitym."""
        if not isinstance(n, int) or isinstance(n, bool):
            return NotImplemented
        if n < 0:
            return (~self) ** -n
        return Frac(self.x ** n, self.y ** n)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        """Zadanie 6.5: zwraca ten sam ulamek."""
        return self

    def __neg__(self):  # -frac = (-1)*frac
        """Zadanie 6.5: zwraca ulamek przeciwny."""
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        """Zadanie 6.5: zwraca odwrotnosc ulamka."""
        return Frac(self.y, self.x)

    def __abs__(self):  # abs(frac)
        """Zadanie 6.5: zwraca wartosc bezwzgledna ulamka."""
        return Frac(abs(self.x), self.y)

    def __int__(self):  # int(frac), obcina w strone zera
        """Zadanie 6.5: zamienia ulamek na int, obcinajac w strone zera."""
        whole = abs(self.x) // self.y
        return whole if self.x >= 0 else -whole

    def __trunc__(self):  # math.trunc(frac)
        """Zadanie 6.5: obcina ulamek w strone zera, tak jak int()."""
        return int(self)

    def __floor__(self):  # math.floor(frac)
        """Zadanie 6.5: zwraca podloge ulamka, dokladnie, bez float."""
        return self.x // self.y

    def __ceil__(self):  # math.ceil(frac)
        """Zadanie 6.5: zwraca sufit ulamka, dokladnie, bez float."""
        return -(-self.x // self.y)

    def __format__(self, spec):  # f"{frac:.3f}"
        """Zadanie 6.5: formaty liczbowe jak dla float, pozostale dla "x/y"."""
        if spec and spec[-1] in "eEfFgGn%":
            return format(float(self), spec)
        return format(str(self), spec)

    def __float__(self):  # float(frac)
        """Zadanie 6.5: zamienia ulamek na float."""
        return self.x / self.y

    def __bool__(self):  # bool(frac), if frac:
        """Zadanie 6.5: zero jest falszem, jak dla innych liczb."""
        return self.x != 0

    def __hash__(self):
        """Zadanie 6.5: zwraca hash zgodny z int dla ulamkow calkowitych."""
        return hash(self.x) if self.y == 1 else hash((self.x, self.y))
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])


if __name__ == "__main__":
    # przyklady z docstringow, pelne testy sa w pliku test_fracs.py
    print(doctest.testmod())
