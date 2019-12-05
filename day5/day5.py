from itertools import product


def load_instructions(filename):
    with open(filename, "r") as file:
        line = file.readline()

    return parse_instructions(line)


def parse_instructions(instructions_as_string):
    return list(map(int, instructions_as_string.split(",")))


def get_next_instruction(instructions, instruction_pointer):

    instruction = instructions[instruction_pointer]
    
    return instruction


def run_program(instructions, input_value):

    instruction_pointer = 0

    while True:

        instruction = get_next_instruction(instructions, instruction_pointer)

        if instruction == 99:
            break
        elif instruction == 1:

            instruction_pointer += 1
            location = instructions[instruction_pointer]
            first_number = instructions[location]

            instruction_pointer += 1
            location = instructions[instruction_pointer]
            second_number = instructions[location]

            instruction_pointer += 1
            location = instructions[instruction_pointer]
            instructions[location] = first_number + second_number

            instruction_pointer += 1

        elif instruction == 2:
            instruction_pointer += 1
            location = instructions[instruction_pointer]
            first_number = instructions[location]

            instruction_pointer += 1
            location = instructions[instruction_pointer]
            second_number = instructions[location]

            instruction_pointer += 1
            location = instructions[instruction_pointer]
            instructions[location] = first_number * second_number

            instruction_pointer += 1
        elif instruction == 3:
            instruction_pointer += 1
            location = instructions[instruction_pointer]
            instructions[location] = input_value
        elif instruction == 4:
            instruction_pointer += 1
            location = instructions[instruction_pointer]
            output_value = instructions[location]

        else:
            raise Exception(f"Unexpected OpCode [{instruction}]")

    return output_value


def solve_part1():
    input_value = 1
    instructions = load_instructions(filename="input.txt")
    result = run_program(instructions, input_value)
    return result[0]


def solve_part2():
    pass


def solve_all():
    print(f"*** {__file__} ***")
    print(f"Solution to part 1: {solve_part1()}")
    print(f"Solution to part 2: {solve_part2()}")


if __name__ == "__main__":
    solve_all()
