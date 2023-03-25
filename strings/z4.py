"""
napisz program który stworzy napis skladający sie z pierwszej, środkowej oraz ostatniej litery innego napisu.
przykład:
Wejście:
text = "James"
Wyjście:
Jms
"""

text = "Jamesas"
middle_letter_index = len(text) // 2
print(middle_letter_index)
print(text[0], text[middle_letter_index], text[-1], sep="")
