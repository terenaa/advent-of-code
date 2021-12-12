# --- Day 2: Dive! ---

def solve_a(day_input: list) -> int:
    horizontal_position = 0
    depth = 0

    for command in day_input:
        direction, change = command.split(" ")

        if direction == "forward":
            horizontal_position += int(change)
        elif direction == "down":
            depth += int(change)
        elif direction == "up":
            depth -= int(change)

    return horizontal_position * depth


def solve_b(day_input: list) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in day_input:
        direction, change = command.split(" ")

        if direction == "forward":
            horizontal_position += int(change)
            depth += aim * int(change)
        elif direction == "down":
            aim += int(change)
        elif direction == "up":
            aim -= int(change)

    return horizontal_position * depth


if __name__ == "__main__":
    with open("input/day2.txt", "r") as input_file:
        input_str_list = input_file.read().splitlines()

        print("Day 2 - part a: %i" % solve_a(input_str_list))
        print("Day 2 - part b: %i" % solve_b(input_str_list))
