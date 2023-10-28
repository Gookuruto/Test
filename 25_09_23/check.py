def square(num):
    return num * num


def cube(num):
    return square(num) * num


def power_of_num(power):
    if power == 2:
        return square
    elif power == 3:
        return cube


num_powers = power_of_num(3)
# num_powers będzie funkcją square
print(num_powers(5))
# 25
