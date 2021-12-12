# --- Day 3: Binary Diagnostic ---

def solve_a(day_input: list) -> int:
    gamma_rate = ""
    epsilon_rate = ""
    input_length = len(day_input)

    for i in range(len(day_input[0])):
        avg = sum([int(x[i]) for x in day_input]) / input_length

        gamma_rate += "1" if avg > 0.5 else "0"
        epsilon_rate += "0" if avg > 0.5 else "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def solve_b(day_input: list) -> int:
    return calculate_oxygen_generator_rating(day_input, 0) * calculate_co2_scrubber_rating(day_input, 0)


def calculate_oxygen_generator_rating(data_input: list, column: int) -> int:
    if len(data_input) == 1:
        return int(data_input[0], 2)

    ones, zeroes = separate_dominants(data_input, column)

    return calculate_oxygen_generator_rating(ones if len(ones) >= len(zeroes) else zeroes, column + 1)


def calculate_co2_scrubber_rating(data_input: list, column: int) -> int:
    if len(data_input) == 1:
        return int(data_input[0], 2)

    ones, zeroes = separate_dominants(data_input, column)

    return calculate_co2_scrubber_rating(ones if len(ones) < len(zeroes) else zeroes, column + 1)


def separate_dominants(data_input: list, column: int) -> tuple[list, list]:
    ones = []
    zeroes = []

    for i in range(len(data_input)):
        if data_input[i][column] == "1":
            ones.append(data_input[i])
        else:
            zeroes.append(data_input[i])

    return ones, zeroes


if __name__ == "__main__":
    with open("input/day3.txt", "r") as input_file:
        input_str_list = input_file.read().splitlines()

        print("Day 3 - part a: %i" % solve_a(input_str_list))
        print("Day 3 - part b: %i" % solve_b(input_str_list))
