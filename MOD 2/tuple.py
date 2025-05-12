"""
Comprehensive Python Tuple Methods - Single File Reference

This script demonstrates all built-in tuple methods with:
- Syntax
- Description
- Example usage
- Expected output (as comments)
"""

def demo_count():
    # Method: count(x)
    # Syntax: tuple.count(x)
    # Description: Return the number of occurrences of value x in the tuple.
    tpl = (1, 2, 2, 3, 2)
    # Example:
    result = tpl.count(2)
    print(result)  # Output: 3
    # Explanation: There are three occurrences of the value 2 in the tuple.


def demo_index():
    # Method: index(x[, start[, end]])
    # Syntax: tuple.index(x, start=0, end=len(tuple))
    # Description: Return the first index of value x in the tuple. Raises ValueError if not found.
    tpl = ('a', 'b', 'c', 'b')
    # Example:
    idx = tpl.index('b')
    print(idx)  # Output: 1
    # Explanation: 'b' first appears at index position 1 in the tuple.


if __name__ == '__main__':
    # Execute all demonstration functions
    for name, func in globals().items():
        if name.startswith('demo_') and callable(func):
            print(f"--- Running {name} ---")
            func()
            print()  # Blank line for readability