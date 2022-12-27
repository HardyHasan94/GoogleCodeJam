"""
Moons and Umbrellas problem
---------------------------

-- Problem:
    Given a string containing the letters 'C', 'J' and question marks, and the costs x and y of 'CJ' and 'JC' resp.,
    replace the question marks with either 'C' or 'J' such that the total cost is minimal.
    Example string: s = 'J?CC??', x=1, y=2
            Solution: s = 'JCCCC' --> cost = y = 2 because of the JC substring (CC or JJ have cost 0).

"""

import itertools
import re
import math

def compute_cost(x, y, sublst):
    """Compute and return the total cost of a string."""
    n_cj = len(re.findall('CJ', ''.join(sublst)))
    n_jc = len(re.findall('JC', ''.join(sublst)))

    return n_cj*x + n_jc*y


def find_closest_letter(s):
    """Find and return the first non-empty letter."""
    for el in s:
        if el != '?':
            return el
    return 0


def find_opposite(c):
    """Given a char c which is either C or J, return the other letter."""
    return 'J' if c == 'C' else 'C'


def smallest_pair(x, y):
    """Given costs x and y, return a list of the pair with the smallest cost."""

    return list(sorted({'CJ': x, 'JC': y}.items(), key=lambda kv: kv[1])[0][0])

def positive_case(x, y, s):
    """
    Fill in the missing letters of given string when both costs are positive.

    Parameters
    ----------
    x: int
        cost of 'CJ'
    y: int
        cost of 'JC'
    s: str
        The string

    Returns
    -------
    new string with all '?' replace by C or J.
    """
    s_list = list(s)

    # if no letters are filled, then replace all '?' with the same letter.
    if len(set(s_list)) == 1 and s_list[0] == '?':
        return 'C'*len(s_list)

    # if first char is ?, set it equal to the closest letter to the right of it
    if s_list[0] == '?':
        s_list[0] = find_closest_letter(s_list)

    # for the rest of the '?', set them equal to the previous letter
    for i in range(1, len(s_list)):
        if s_list[i] == '?':
            s_list[i] = s_list[i-1]

    return ''.join(s_list)


def negative_case(x, y, s):
    """
    Fill in the missing letters of given string when both costs are negative.

    Parameters
    ----------
    x: int
        cost of 'CJ'
    y: int
        cost of 'JC'
    s: str
        The string

    Returns
    -------
    new string with all '?' replace by C or J.
    """
    s_list = list(s)

    # if no letters are given, then fill the first two positions with the lowest cost pair
    if len(set(s_list)) == 1 and s_list[0] == '?':
        s_list[:2] = smallest_pair(x, y)

    # if the first position is ?, then find the closest letter to it and the distance between them,
    # and based on that determine how to fill that position
    if s_list[0] == '?':
        closest = find_closest_letter(s_list)
        d = s_list.index(closest)
        opposite = find_opposite(closest)
        s_list[0] = opposite if (d-1) % 2 == 0 else closest

    # otherwise for each ? replace it with the opposite of the letter preceding it.
    for i in range(1, len(s_list)):
        if s_list[i] == '?':
            s_list[i] = find_opposite(s_list[i-1])

    return ''.join(s_list)


def opposite_case(x, y, s):
    """
    Fill in the missing letters of given string when the costs are opposite in sign.

    Parameters
    ----------
    x: int
        cost of 'CJ'
    y: int
        cost of 'JC'
    s: str
        The string

    Returns
    -------
    new string with all '?' replace by C or J.
    """
    s_list = list(s)

    # if no letters are given, then fill the first two positions with the lowest cost pair
    if len(set(s_list)) == 1 and s_list[0] == '?':
        s_list[:2] = smallest_pair(x, y)

    # if the first position is ?, fill it so to gain a negative cost if possible
    if s_list[0] == '?':
        closest = find_closest_letter(s_list)
        sp = smallest_pair(x, y)
        if closest == sp[1]:
            s_list[0] = sp[0]
        else:
            s_list[0] = closest

    # if the last position is ?, fill it so to gain a negative cost if possible
    if s_list[-1] == '?':
        closest = find_closest_letter(list(reversed(s_list)))
        sp = smallest_pair(x, y)
        if closest == sp[0]:
            s_list[-1] = sp[1]
        else:
            s_list[-1] = closest

    # if x+y < 0, use the same technique as case 2
    if x + y < 0:
        return negative_case(x, y, ''.join(s_list))

    # if x+y > 0, use the same technique as case 1
    if x + y >= 0:
        return positive_case(x, y, ''.join(s_list))


def find_cost(x, y, s):
    """
    Find the minimal cost of a string for given costs.

    The solution idea is to first find the type this test string belongs too
    and fill in the missing chars, then compute the cost and return it.
    There are three types of string, namely where both costs are positive, both negative
    or opposite costs.

    Parameters
    ----------
    x: int
        cost of 'CJ'
    y
    s: int
        cost of 'JC'

    Returns
    -------
    cost: int
        The minimal cost

    """
    if x >= 0 and y >= 0:
        s = positive_case(x, y, s)
    elif x <= 0 and y <= 0:
        s = negative_case(x, y, s)
    else:
        s = opposite_case(x, y, s)

    cost = compute_cost(x, y, s)

    return cost


def main(T):
    """
    Given the number of test cases, read all cases,
    compute and print their costs.
    """
    costs = []

    # read all cases
    for case in range(T):
        # each case consists of the costs and the string
        x, y, s = input().split()
        x, y = int(x), int(y)
        if len(s) == 1:
            # no need to run the algorithm. minimal cost is obvious
            costs.append(0)
        else:
            cost = find_cost(x, y, s)
            costs.append(cost)

    for case, cost in enumerate(costs):
        print(f"Case #{case+1}: {cost}")


if __name__ == "__main__":
    T = int(input())  # test cases
    main(T)

# =============== END OF FILE ===============
