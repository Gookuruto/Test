def read_n_lines(n):
    with open("abc.txt", "r") as f:
        content = f.readlines()
    return ''.join(content[:n])

print(read_n_lines(5))

def read_n(n):
    with open("abc.txt", "r") as f:
        lines = f.readlines()
        if len(lines) >= n:
            line3 = lines[:n]
            return print(line3)
read_n(3)

with open("abc.txt", "r") as f:
    counter = 0
    n = 4
    for line in f:
        print(line)
        counter += 1
        if counter == n:
            break


with open("abc.txt", "r") as f:
    counter = 0
    n = 4
    while counter < n:
        print(f.readline())
        counter +=1