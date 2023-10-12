from typing import Tuple

import numpy as np


def value_v1(triangle: np.ndarray, state: Tuple[int, int]) -> int:
    row, col = state
    reward = triangle[row][col]
    if row == triangle.shape[0] - 1:
        return reward
    return reward + max(
        value_v1(triangle, state=(row + 1, col)),
        value_v1(triangle, state=(row + 1, col + 1)),
    )


def value_v2(triangle: np.ndarray, state: Tuple[int, int]) -> int:
    values = np.zeros(triangle.shape, dtype=int)
    last_row = triangle.shape[0] - 1
    for row in range(last_row, -1, -1):
        for col in range(row + 1):
            next_return = (
                0
                if row == last_row
                else max(
                    values[row + 1, col],
                    values[row + 1, col + 1],
                )
            )
            values[row, col] = triangle[row][col] + next_return
    return values[state]


if __name__ == "__main__":
    size = int(input())
    triangle = np.zeros((size, size), dtype=int)
    for row in range(size):
        input_line = input()
        rewards = [int(s) for s in input_line.split(" ")]
        assert len(rewards) == 1 + row
        for col, reward in enumerate(rewards):
            triangle[row, col] = reward

    state = (0, 0)
    best_return = value_v2(triangle, state)
    print(f"{best_return=}")
