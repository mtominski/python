# Zestaw 3 - Miłosz Tomiński

## Zadanie 3.1

### Fragment 1 - poprawny

```python
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
```

Kod jest poprawny składniowo i daje `result = 3`. Średnik oddziela instrukcje
w jednej linii, a średnik na końcu linii jest dozwolony. Nawiasy wokół warunku
też nie przeszkadzają.

### Fragment 2 - niepoprawny

```python
for i in "axby": if ord(i) < 100: print (i)
```

`SyntaxError`. Po dwukropku w tej samej linii mogą stać tylko instrukcje
proste, a `if` jest instrukcją złożoną. Poprawny zapis:

```python
for i in "axby":
    if ord(i) < 100:
        print(i)
```

### Fragment 3 - poprawny

```python
for i in "axby": print (ord(i) if ord(i) < 100 else i)
```

Kod jest poprawny składniowo, bo po dwukropku jest jedna instrukcja prosta
(`print`), a `... if ... else ...` to wyrażenie warunkowe, a nie instrukcja.
Wypisuje kolejno `97`, `x`, `98`, `y` (kody znaków `a` i `b` są mniejsze
od 100, a `x` i `y` nie).

## Zadanie 3.2

### Linia 1

```python
L = [3, 5, 4] ; L = L.sort()
```

Python nie zgłasza błędu, ale `L` ma potem wartość `None`. Metoda `sort()`
sortuje listę w miejscu i zwraca `None`, więc przypisanie gubi listę.
Poprawnie: samo `L.sort()` albo `L = sorted(L)`.

### Linia 2

```python
x, y = 1, 2, 3
```

`ValueError: too many values to unpack`. Po prawej stronie są trzy wartości,
a po lewej tylko dwie zmienne.

### Linia 3

```python
X = 1, 2, 3 ; X[1] = 4
```

`TypeError: 'tuple' object does not support item assignment`. `X` jest
krotką, a krotek nie można zmieniać.

### Linia 4

```python
X = [1, 2, 3] ; X[3] = 4
```

`IndexError: list assignment index out of range`. Lista ma indeksy od 0 do 2,
więc `X[3]` nie istnieje. Nowy element dodaje się przez `X.append(4)`.

### Linia 5

```python
X = "abc" ; X.append("d")
```

`AttributeError: 'str' object has no attribute 'append'`. Napisy nie mają
metody `append` i nie można ich zmieniać. Poprawnie: `X += "d"`
(albo `X = X + "d"`). Oba zapisy tworzą nowy napis `"abcd"` i przypisują go
do `X`.

### Linia 6

```python
L = list(map(pow, range(8)))
```

`TypeError: pow() missing required argument 'exp'`. Funkcja `pow` potrzebuje
dwóch argumentów (podstawy i wykładnika), a `map` podaje jej tylko jeden.
Poprawnie: `list(map(pow, range(8), [2] * 8))` albo
`[x ** 2 for x in range(8)]`.

Dodatkowo w liniach 1 i 3-5 średnik łączy dwie instrukcje, co w Pythonie
jest dozwolone, ale niezalecane.
