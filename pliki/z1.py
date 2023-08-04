import random


def read_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        result = f.read()
    return result


def read_n_lines(n: int, file: str) -> str:
    with open(file, "r") as f:
        lines = [f.readline() for _ in range(n)]

    return "".join(lines)


def read_n_lines_op2(n: int, file: str) -> str:
    with open(file, "r") as f:
        for i in range(n):
            yield f.readline()


#
# for line in read_n_lines_op2(10,"one.txt"):
#     print(line)

def squares_to_file(file_path: str):
    random_numbers = [random.randint(-9999, 9999) for i in range(100)]
    with open(file_path, "w") as f:
        for number in random_numbers:
            f.write(f"{number} {number ** 2}\n")

def squares_to_file_op2(file_path:str):
    with open(file_path, "w") as f:
        for i in range(100):
            number = random.randint(-9999,9999)
            f.write(f"{number} {number **2}\n")

squares_to_file("sqares.txt")
# print(read_n_lines(10, "one.txt"))
