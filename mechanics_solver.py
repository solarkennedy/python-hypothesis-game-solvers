#!/usr/bin/env python3

import unittest
from itertools import combinations

from hypothesis import given, settings, note, Phase
from hypothesis.strategies import lists, integers, sampled_from


def rule1(matrix):
    # "From number 5 number 3 is reachable with a knight's move"
    row5, col5 = find_element(matrix, 5)
    for kmove in [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]:
        try:
            if matrix[row5 + kmove[0]][col5 + kmove[1]] == 3:
                 return True
        except IndexError:
            pass
    return False


def rule2(matrix):
    # "The sum of the numbers in the 3rd row is 7"
    return matrix[2][0] + matrix[2][1] + matrix[2][2] + matrix[2][3] == 7 


def rule3(matrix):
    # "Number 4 stands alone in the column on the far left"
    return set([matrix[0][0], matrix[1][0], matrix[2][0], matrix[3][0]]) == set([0, 0, 0, 4])


def rule4(matrix):
    # "In none of the rows can stand a number that's greater than the numbers
    # in the row below it"
    max_so_far = 0
    for row in range(len(matrix)):
        row_max = max(matrix[row][0], matrix[row][1], matrix[row][2], matrix[row][3])
        if row_max >= max_so_far:
            max_so_far = row_max
        else:
            return False
    return True


def rule5(matrix):
    # "If you add up all the numbers in the 4th column, the result is 3
    return matrix[0][3] + matrix[1][3] + matrix[2][3] + matrix[3][3] == 3


def rule6(matrix):
    # "Number 5 is the only one standing alone in both its row and column."
    row, col = find_element(matrix, 5)
    return set([matrix[0][col], matrix[1][col], matrix[2][col], matrix[3][col]]) == set([0, 0, 0, 5]) and set([matrix[row][0], matrix[row][1], matrix[row][2], matrix[row][3]]) == set([0, 0, 0, 5])


def find_element(matrix, x):
    for m in range(len(matrix)):
        for n in range(len(matrix[0])):
            if matrix[m][n] == x:
                return m, n

def test_rule1_good():
    m = [[0 for x in range(4)] for y in range(4)]
    m[0][0] = 5
    m[2][1] = 3
    assert rule1(m), ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))


def test_rule1_good2():
    m = [[0 for x in range(4)] for y in range(4)]
    m[0][0] = 5
    m[1][2] = 3
    assert rule1(m), ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))


def test_rule1_nogood():
    m = [[0 for x in range(4)] for y in range(4)]
    m[0][0] = 5
    m[2][2] = 3
    assert not rule1(m), ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))


def test_rule4_nogood():
    m = [[0 for x in range(4)] for y in range(4)]
    m[0][0] = 4
    m[1][0] = 3
    m[2][0] = 2
    m[3][0] = 1
    assert not rule4(m), ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))


def test_rule4_good():
    m = [[0 for x in range(4)] for y in range(4)]
    m[0][0] = 2
    m[1][0] = 3
    m[2][0] = 4
    m[3][0] = 5
    assert rule4(m), ('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))


@given(lists(elements=integers(min_value=1, max_value=15), min_size=5, max_size=5, unique=True))
@settings(max_examples=200000000000, deadline=None, phases=[Phase.generate])
def test_mechanics_solver(positions):
        m = [[0 for x in range(4)] for y in range(4)] 

        # First we place the knobs in the positions according to the input list
        for knob in range(len(positions)):
            position = positions[knob]
            row = position / 4
            col = position % 4
            m[row][col] = knob + 1
        note('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in m]))
        assert not all([rule1(m), rule2(m), rule3(m), rule4(m), rule5(m), rule6(m)])


if __name__ == "__main__":
    test_mechanics_solver()
