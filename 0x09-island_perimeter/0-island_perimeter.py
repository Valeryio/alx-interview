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
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i-1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
