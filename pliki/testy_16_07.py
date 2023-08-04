with open("testy_16_07.txt", "a") as f:
    f.write("dodane\n")


with open("testy_16_07.txt", "r") as f:
    content = f.read()

    print(content)
