"""
Mamy następujący kod Pythona, który przechowuje napis w zmiennej text:
text = 'X-DSPAM-Confidence: 0.8475'
Użyj find() i wycinków napisów, tak aby wyodrębnić część tekstu po znaku dwukropka, a następnie użyj funkcji float(), żeby przekształcić wyodrębniony fragment
na liczbę zmiennoprzecinkową.
"""
text = 'X-DSPAM-Confidence: 0.8475'
start_index = text.find(":") + 1
print(start_index)
sliced_text = text[start_index:]
number = float(sliced_text)
print(number)
print(type(number))
