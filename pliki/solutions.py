# 4
def file_read(fname):
    from itertools import islice
    with open(fname, "a+") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    txt = open(fname)
    print(txt.read())


file_read('abc.txt')


# 5
def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]


print(longest_word('test.txt'))

# 6
import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_uppercase:
    with open(letter + ".txt", "w") as f:
        f.writelines(letter)


# 7
def filetolistofints(filename):
    list_to_return = []
    with open(filename) as f:
        line = f.readline()
        while line:
            list_to_return.append(int(line))
            line = f.readline()
    return list_to_return


primeslist = filetolistofints('one.txt')
happieslist = filetolistofints('two.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)

#7.2
primeslist = []
with open('primenumbers.txt') as primesfile:
    line = primesfile.readline()
    while line:
        primeslist.append(int(line))
        line = primesfile.readline()

happieslist = []
with open('happynumbers.txt') as happiesfile:
    line = happiesfile.readline()
    while line:
        happieslist.append(int(line))
        line = happiesfile.readline()

overlaplist = []
for elem in primeslist:
    if elem in happieslist:
        overlaplist.append(elem)

print(overlaplist)
