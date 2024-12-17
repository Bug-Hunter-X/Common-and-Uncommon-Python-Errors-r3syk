def function_with_uncommon_error(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Or raise a custom exception
    except TypeError:
        print("Error: Invalid input types")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    return result

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero, None
print(function_with_uncommon_error(10, "a")) # Output: Error: Invalid input types, None
print(function_with_uncommon_error(10, 2.5)) # Output: 4.0

#Example of an Uncommon Error: Recursion Depth Exceeded
def recursive_function(n):
    if n == 0:
        return 0
    else:
        return recursive_function(n - 1) + n

# print(recursive_function(10000)) # This will cause RecursionError