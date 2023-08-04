# # ==================================================
# import csv
#
# reader = csv.reader(open("employees.csv"))
# for row in reader:
#     print(row)
# # ==================================================
# import csv
# #
# reader = csv.reader(open("employees.csv"))
# no_lines = len(list(reader))
# print(no_lines)
# # ==================================================
import csv

csv_string = """1,2,3
4,5,6
7,8,9
"""
print("Original string:")
print(csv_string)
lines = csv_string.splitlines()
print("List of CSV formatted strings:")
print(lines)
reader = csv.reader(lines)
parsed_csv = list(reader)
print("\nList representation of the CSV file:")
print(parsed_csv)
