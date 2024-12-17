The solution for the ZeroDivisionError and TypeError is already present in the bug.py code with the try-except block.  For the RecursionError,  a solution would be to add a base case check to prevent excessive recursion.  Here's an example:

def recursive_function_fixed(n, max_depth=1000):
    if n == 0 or max_depth == 0:
        return 0
    else:
        return recursive_function_fixed(n - 1, max_depth - 1) + n

print(recursive_function_fixed(10000)) # This will work