"""
Reversort Engineering problem
-----------------------------

-- Problem:
    This problem is related to the problem in `reversort.py`, namely given a cost `C` and an integer `N`
    find a permutation of the integers {1,..,N} such that the cost of sorting it according to the
    `reversort` algorithm is exactly equal to `C`, or state that there exist no such permutation.

-- Solution idea:
    The solution consists of two steps, first we have to determine whether it is possible to find
    such a permutation that satisfy the cost constraint, and secondly we have to find the permutation
    if it is possible to do so.

    1. For this step, we find the minimum and maximum possible costs for a list of length `N` and
    check whether C is whithin these two bounds. The function `is_possible(N, C)` does that.
    2. For this step, we have to first find a sum of terms that equal C, and find a permutation that
    would result in this sum when sorted iteratively. The function `find_subcosts(N, C)` does that.
    This function creates this sum by iteratively finding these terms, in a way such that each term
    attains its upperbound value before the term right to it starts to increase. Initially all terms
    are 1, which is the lower bound of each term. The upper bounds are {N, N-1, N-2, .., 3, 2}

    Once these terms are found, the next step is to reverse segments of the original list iteratively
    such that each such modification gives rise to the term at that position. The reverse operation
    is performed between the current index of `term + element - 1` and the current index of the element,
    for each element in the original sorted list.

"""

def is_possible(N, C):
    """
    Check whether the cost is possible to be achieved
    by sorting any permutation of the integers {1,..,N}.

    Parameters
    ----------
    N: int
        Length of list
    C: int
        Cost of sorting.

    Returns
    -------
    possible: bool
        True if a permutation exist, else false
    """
    min_cost = N-1
    max_cost = ((N-1)*(N+2))//2
    return min_cost <= C <= max_cost


def find_subcosts(N, C):
    """
    Find a sum of N-1 terms that is equal to C,
    where each term is within its bounds.

    Parameters
    ----------
    N: int
        Length of list
    C: int
        Cost of sorting.

    Returns
    -------
    subcosts: list
        List of the terms at each position in the sum.
    """
    subcosts = [1 for _ in range(N-1)]
    upper_bounds = [N-i for i in range(N-1)]
    
    for pos in range(N-1):
        if sum(subcosts) == C:
            break
        ub = upper_bounds[pos] - 1
        while sum(subcosts) != C and ub > 0:
            subcosts[pos] += 1
            ub -= 1

    return subcosts


def find_list(N, C):
    """
    Find and return a permutation of the integers {1,..,N}
    such that the cost of sorting it is equal to C.

    Parameters
    ----------
    N: int
        Length of list
    C: int
        Cost of sorting.

    Returns
    -------
    lst: list
        A list satisfying the cost constraint.

    """
    org = range(1, N)
    lst = list(range(1, N+1))

    subcosts = find_subcosts(N, C)

    for el in org:
        cur_pos = lst.index(el)
        subcost = subcosts[el-1]
        j = (subcost + el - 1)
        j_pos = lst.index(j)
        minimum, maximum = min([cur_pos, j_pos]), max([cur_pos, j_pos])
        lst[minimum:maximum+1] = list(reversed(lst[minimum:maximum+1]))

    return lst


def main(T):
    """
    Given the number of test cases, read all cases,
    and print either a list or 'IMPOSSIBLE' when so.
    """
    lists = []

    for case in range(T):
        inp = input()
        N, C = [int(el) for el in inp.split()]
        possible = is_possible(N, C)

        if not possible:
            lists.append('IMPOSSIBLE')
        else:
            lst = find_list(N, C)
            lst = [str(el) for el in lst]
            lists.append(' '.join(lst))

    for case, el in enumerate(lists):
        print(f"Case #{case + 1}: {el}", flush=True)


if __name__ == "__main__":
    T = int(input())  # test cases
    main(T)

# =============== END OF FILE ===============
