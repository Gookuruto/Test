"""
Stwórz słownik który w przyszłości pozwoli w łatwy sposób zamienić litere na liczbe. według wzoru:
a:1
b:2
...
l:12
...
"""
letters = [(chr(i), i - 96) for i in range(ord("a"), ord("z") + 1)]
print(letters)
test_dict = {letter: number for (letter, number) in letters}
print(test_dict)
test_dict2 = {}
for (letter, number) in letters:
    test_dict2[letter] = number

print(test_dict2)
