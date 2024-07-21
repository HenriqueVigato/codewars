def square_digits(num):
    split_numbers = [n for n in str(num)]
    squared_numbers = [str(int(n) ** 2) for n in split_numbers]

    return int("".join(squared_numbers))


print(square_digits(955))
