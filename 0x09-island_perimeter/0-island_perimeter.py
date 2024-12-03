#!/usr/bin/python3

"""This is module contains a function
that allow to determine the perimeter of
an island
"""


def island_perimeter(grid):
    """it determine the perimeter of the island
    param:
        grid: list
    return:
        A number
    """
    perimeter = 0
    # print(len(grid), " : " ,len(grid[0]))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(f"[{grid[i][j]}]", end='')

            if grid[i][j] == 1:
                # verify at the top
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i-1][j] == 0:
                # verify at the bottom
                    perimeter += 1
                if grid[i][j - 1] == 0:
                # verify at the left
                    perimeter += 1
                if grid[i][j + 1] == 0:
                # verify at the right
                    perimeter += 1
        # print('')
    return perimeter
