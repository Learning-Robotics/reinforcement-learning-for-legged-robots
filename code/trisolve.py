def value(triangle: list, row: int, col: int) -> int:
    nb_rows = len(triangle)
    reward = triangle[row][col]
    if row == nb_rows - 1:
        return reward
    return reward + max(
        value(triangle, row + 1, col),
        value(triangle, row + 1, col + 1),
    )


if __name__ == "__main__":
    size = int(input())
    triangle = []
    for line_num in range(size):
        line = input()
        triangle.append([int(s) for s in line.split(" ")])
        assert len(triangle[-1]) == 1 + line_num
    best_return = value(triangle, 0, 0)
    print(f"{best_return=}")
