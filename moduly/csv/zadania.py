"""
- Napisz program w Pythonie, który odczyta i wyświetli zawartość podanego pliku CSV. Użyj csv.reader
- Napisz program w Pythonie, który policzy liczbę wierszy w danym pliku CSV. Użyj csv.reader
- Napisz program w Pythonie, który przeanalizuje(sparsuje) podany ciąg CSV i otrzyma listę list wartości ciągu
    przykład:
        Original string:
            1,2,3
            4,5,6
            7,8,9

        List of CSV formatted strings:
            ['1,2,3', '4,5,6', '7,8,9']
        List representation of the CSV file:
            [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
"""

import csv

with open("employees.csv", "r") as lines:
    reader = csv.reader(lines)
    parsed_csv = list(reader)
    # print("List of lists")
    # print(parsed_csv)

headers = parsed_csv[0]
list_of_dicts = []
for employee in parsed_csv[1:]:
    temp_employe = {}
    for index, value in enumerate(headers):
        temp_employe[value] = employee[index]
    list_of_dicts.append(temp_employe)

print(list_of_dicts)
print(list_of_dicts[0]["FIRST_NAME"], list_of_dicts[0]["SALARY"])
list_of_dicts[0]["get_to_work"] = "9:00"
list_of_dicts[0]["get_out_of_work"] = "17:00"

