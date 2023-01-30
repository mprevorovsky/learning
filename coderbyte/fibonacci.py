"""
just playing...
"""

import timeit


def fib(n: int) -> int:
    """
    Returns the n-th number in the Fibonacci sequence.
    """

    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_memo(n: int, memo: dict[int, int] = {}) -> int:
    """
    Returns the n-th number in the Fibonacci sequence.
    Uses memoization for increased speed
    """

    if n <= 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        return memo[n]


# print(timeit.timeit('fib(40)', globals=globals(), number=1))
print(timeit.timeit("fib_memo(20)", globals=globals(), number=1))
