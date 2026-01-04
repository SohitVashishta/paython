"""
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

"""

def factorial(n):
    """
    Calculates the factorial of a number using recursion.

    Parameters
    ----------
    n : int
        The number to calculate the factorial of.

    Returns
    -------
    int
        The calculated factorial of n.

    Examples
    --------
    >>> factorial(5)
    120
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print("Factorial of", num, "is", result)
