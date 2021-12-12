# --- Day 4: Giant Squid ---

def solve_a(numbers: list, boards: list) -> int:
    boards_count = len(boards)

    for number in numbers:
        for i in range(boards_count):
            boards[i] = [-1 if x == number else x for x in boards[i]]

            if not is_winner(boards[i]):
                continue

            return number * sum([0 if x == -1 else x for x in boards[i]])

    return -1


def solve_b(numbers: list, boards: list) -> int:
    for number in numbers:
        boards_count = len(boards)

        for i in range(boards_count):
            boards[i] = [-1 if x == number else x for x in boards[i]]

            if not is_winner(boards[i]):
                continue

            if boards_count == 1:
                return number * sum([0 if x == -1 else x for x in boards[i]])

            boards[i] = None

        boards = list(filter(None, boards))

    return -1


def is_winner(board: list) -> bool:
    board_size = 5

    for i in range(0, len(board), board_size):
        if sum(board[i:i + board_size]) == board_size * -1:
            return True

    for i in range(board_size):
        if sum([board[x + i] for x in range(0, len(board), board_size)]) == board_size * -1:
            return True

    return False


def prepare_day_input(input_list: list) -> tuple[list, list]:
    numbers = [int(x) for x in input_list[0].split(",")]
    boards = []

    current_board = []
    for i in range(2, len(input_list)):
        if input_list[i] != "":
            current_board.extend([int(x) for x in filter(None, input_list[i].split(" "))])
            continue

        boards.append(current_board)
        current_board = []

    boards.append(current_board)

    return numbers, boards


if __name__ == "__main__":
    with open("input/day4.txt", "r") as input_file:
        input_str_list = input_file.read().splitlines()
        number_list, board_list = prepare_day_input(input_str_list)

        print("Day 4 - part a: %i" % solve_a(number_list, board_list))
        print("Day 4 - part b: %i" % solve_b(number_list, board_list))
