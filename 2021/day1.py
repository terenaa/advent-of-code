# --- Day 1: Sonar Sweep ---

def solve_a(day_input: list) -> int:
    current = None
    increasing_measurements = 0

    for depth in day_input:
        if current is not None:
            if depth > current:
                increasing_measurements += 1

        current = depth

    return increasing_measurements


def solve_b(day_input: list) -> int:
    current = None
    increasing_measurements = 0

    for i in range(2, len(day_input)):
        depth_sum = day_input[i] + day_input[i - 1] + day_input[i - 2]

        if current is not None:
            if depth_sum > current:
                increasing_measurements += 1

        current = depth_sum

    return increasing_measurements


if __name__ == "__main__":
    with open("input/day1.txt", "r") as input_file:
        input_str_list = input_file.read().splitlines()
        input_list = [int(x) for x in input_str_list]

        print("Day 1 - part a: %i" % solve_a(input_list))
        print("Day 1 - part b: %i" % solve_b(input_list))
