def main():
    puzzle = get_puzzle()
    key = "XMAS"
    size = len(key)
    x_len = len(puzzle[0])
    y_len = len(puzzle)
    count = 0
    print(puzzle[1][2])
    for fila_n, fila in enumerate(puzzle):
        count_array = []
        for columna_n, col in enumerate(fila):

            if col == key[0]:
                # print(
                #     f"Fila: [{fila_n }] Columna [{columna_n }] char:{puzzle[fila_n ][columna_n ]}",
                # )
                # if fila_n == 9 and columna_n == 3:
                #     print(columna_n - size)
                if columna_n - size + 1 >= 0:

                    key_reversed = all(
                        (fila[columna_n - index] == char)
                        for index, char in enumerate(key)
                    )

                    key_up_left = all(
                        (puzzle[fila_n - index][columna_n - index] == char)
                        for index, char in enumerate(key)
                    )

                    key_down_left = (fila_n + size < y_len) and all(
                        (puzzle[fila_n + index][columna_n - index] == char)
                        for index, char in enumerate(key)
                    )

                    count_array.extend([key_reversed, key_up_left, key_down_left])

                if columna_n + size - 1 <= x_len:
                    key_adelante = fila[columna_n : size + columna_n] == key

                    key_up_right = all(
                        (puzzle[fila_n - index][columna_n + index] == char)
                        for index, char in enumerate(key)
                    )

                    key_down_right = (fila_n + size < y_len) and all(
                        (puzzle[fila_n + index][columna_n + index] == char)
                        for index, char in enumerate(key)
                    )

                    count_array.extend([key_adelante, key_up_right, key_down_right])

                key_up = (fila_n - size >= 0) and all(
                    (puzzle[fila_n - index][columna_n] == char)
                    for index, char in enumerate(key)
                )

                key_down = (fila_n + size < y_len) and all(
                    (puzzle[fila_n - index][columna_n] == char)
                    for index, char in enumerate(key)
                )
                count_array.extend([key_up, key_down])
                # print(count_array)
                for is_correct in count_array:
                    if is_correct:
                        count += 1
                count_array = []

    print(f"Count: {count}")


def get_puzzle() -> list[list[int]]:
    puzzle = []
    with open("input.txt", "r") as fichero:
        while (puzzle_line := fichero.readline()) != "":
            puzzle.append(puzzle_line)
    return puzzle


if __name__ == "__main__":
    main()

# print("----------------")
# if key_down_right:
#     for index, char in enumerate(key):
#         print(
#             f"Fila: [{fila_n - index}] Columna [{columna_n + index}] char:{puzzle[fila_n - index][columna_n + index]}=={char}",
#         )
