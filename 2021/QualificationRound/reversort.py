"""
Reversort problem
-----------------

-- Problem:
    Given an array of integers and its length, compute the cost of sorting it in ascending order.

-- Solution idea:
    Implement the algorithm to calculate the number of iterations required for sorting the array.
"""


def reverse_sort(lst):
    """
    Given a list of integers, compute the cost of reversing the list
    and flush the cost to the console.
    """

    cost = 0

    for i in range(len(lst) - 1):
        j = lst.index(min(lst[i:]))  # find the index of the smallest element in the sublist
        lst[i:j+1] = reverse(lst[i:j+1])

        cost += j - i + 1
        #print(f"i: {i}\nj: {j}\nlst: {lst}\ncost: {cost}\n")

    return cost


def reverse(lst):
    """
    Given a list, reverse its order.
    """
    return list(reversed(lst))


def main(T):
    """
    Given the number of test cases, read all cases,
    compute and print their costs.
    """

    # read all cases
    cases = []

    for case in range(T):
        # the first line
        N = int(input())  # number of elements in list
        lst = input()  # read the second line
        lst = [int(el) for el in lst.split()]

        cases.append(lst)

    # for each case, compute and print its cost
    for case, lst in enumerate(cases):
        cost = reverse_sort(lst=lst)
        print(f"Case #{case + 1}: {cost}", flush=True)


if __name__ == "__main__":
    T = int(input())  # test cases
    main(T)

# =============== END OF FILE ===============


