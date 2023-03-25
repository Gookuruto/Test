"""
Przeczytaj dokumentację metod związanych z tekstowym typem
danych na stronie https://docs.python.org/library/stdtypes.html#string-methods. Możesz poeksperymentować z niektórymi z nich, aby upewnić się, że rozumiesz, jak
one działają. Szczególnie przydatne są strip() i replace().
Dokumentacja używa składni, która może być nieco myląca. Na przykład w find
֒→ (sub[, start[, end]]) nawiasy kwadratowe wskazują opcjonalne argumenty.
Tak więc sub jest wymagany, ale start jest opcjonalny, a jeśli dodasz start, to end
jest opcjonalny
"""

use_strip = "        mam tekst i dużo spacji                   "
print(use_strip)
print(use_strip.strip())

use_replace = "Owocowy kosz: Jabłko||Gruszka||Truskawka||Winogron" # użyj funkcji replace aby zamienic znaki "||" na coś innego np. przecinki lub średniki

replaced_string = use_replace.replace("||", ",")

print(use_replace)
print(replaced_string)