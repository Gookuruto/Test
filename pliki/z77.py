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