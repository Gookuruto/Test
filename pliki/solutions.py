# 4
def file_read(fname):
    from itertools import islice
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    txt = open(fname)
    print(txt.read())
    txt.close()


file_read('abc.txt')


# 5
def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = max_length(words)
    return [word for word in words if len(word) == max_len]


def max_length(words):
    max_value = 0
    for word in words:
        if max_value < len(word):
            max_value = len(word)
    return max_value


print(longest_word('test.txt'))

# 6
import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_uppercase:
    with open("letters/"+letter + ".txt", "w") as f:
        pass


# 7
# def filetolistofints(filename):
#     list_to_return = []
#     with open(filename) as f:
#         line = f.readline()
#         while line:
#             list_to_return.append(int(line))
#             line = f.readline()
#     return list_to_return
#
# #
# primeslist = filetolistofints('one.txt')
# happieslist = filetolistofints('two.txt')
#
# overlaplist = [elem for elem in primeslist if elem in happieslist]
# print(overlaplist)
#
# #7.2
# primeslist = []
# with open('one.txt') as primesfile:
#     line = primesfile.readline()
#     while line:
#         primeslist.append(int(line))
#         line = primesfile.readline()
#
# happieslist = []
# with open('two.txt') as happiesfile:
#     line = happiesfile.readline()
#     while line:
#         happieslist.append(int(line))
#         line = happiesfile.readline()
#
# overlaplist = []
# for elem in primeslist:
#     if elem in happieslist:
#         overlaplist.append(elem)
#
# print(overlaplist)


def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = file.read().splitlines()
            numbers = [int(num) for num in numbers if num.isnumeric()]
            return set(numbers)
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {file_path}")
    except Exception as e:
        return set()


if __name__ == "__main__":
    primes_file_path = "one.txt"
    happy_numbers_file_path = "two.txt"

    primes_set = read_numbers_from_file(primes_file_path)
    happy_numbers_set = read_numbers_from_file(happy_numbers_file_path)

    common_numbers = primes_set.intersection(happy_numbers_set)

    if common_numbers:
        print("Liczby występujące w obu plikach:")
        print(common_numbers)
    else:
        print("Brak wspólnych liczb w obu plikach.")