password_range = range(307237, 769058)


def test_for_valid_password(password):

    password_digits = [int(char) for char in str(password)]

    for index in range(len(password_digits) - 1):
        if password_digits[index] > password_digits[index + 1]:
            return False

    for index in range(len(password_digits) - 1):
        if password_digits[index] == password_digits[index + 1]:
            return True

    return False


def solve_part1():
    valid_passwords = 0

    for password in password_range:
        if test_for_valid_password(password):
            valid_passwords += 1

    return valid_passwords


def solve_part2():
    pass


def solve_all():
    print(f"*** {__file__} ***")
    print(f"Solution to part 1: {solve_part1()}")
    print(f"Solution to part 2: {solve_part2()}")


if __name__ == "__main__":
    solve_all()
