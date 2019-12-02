from math import floor


def determine_fuel(mass):
    fuel = floor(mass / 3) - 2
    return fuel


def determine_fuel_for_fuel(mass):
    total_fuel = 0
    fuel = determine_fuel(mass)
    while fuel > 0:
        total_fuel += fuel
        fuel = determine_fuel(fuel)

    return total_fuel


def solve_day1_part1():
    fuel_total = 0
    with open("day1_input.txt", "r") as file:
        for line in file:
            input_value = int(line)
            fuel_total += determine_fuel(input_value)

    return fuel_total


def solve_day1_part2():
    fuel_total = 0
    with open("day1_input.txt", "r") as file:
        for line in file:
            input_value = int(line)
            fuel_total += determine_fuel_for_fuel(input_value)

    return fuel_total


if __name__ == "__main__":
    print(f"day 1, part 1: {solve_day1_part1()}")
    print(f"day 1, part 2: {solve_day1_part2()}")
