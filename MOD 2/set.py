"""
Comprehensive Python Set Methods - Single File Reference

This script demonstrates all built-in set methods with:
- Syntax
- Description
- Example usage
- Expected output (as comments)
"""

def demo_clear():
    # Method: clear()
    # Syntax: s.clear()
    # Description: Remove all elements from the set.
    s = {1, 2, 3}
    s.clear()
    print(s)  # Output: set()


def demo_copy():
    # Method: copy()
    # Syntax: s.copy()
    # Description: Return a shallow copy of the set.
    s = {1, 2, 3}
    cp = s.copy()
    cp.add(4)
    print(s)   # Output: {1, 2, 3}
    print(cp)  # Output: {1, 2, 3, 4}


def demo_difference():
    # Method: difference(other, ...)
    # Syntax: s.difference(t)
    # Description: Return a new set with elements in s that are not in t.
    s = {1, 2, 3}
    t = {2, 3, 4}
    print(s.difference(t))  # Output: {1}


def demo_difference_update():
    # Method: difference_update(other, ...)
    # Syntax: s.difference_update(t)
    # Description: Remove all elements of another set from this set.
    s = {1, 2, 3}
    t = {2, 3, 4}
    s.difference_update(t)
    print(s)  # Output: {1}


def demo_discard():
    # Method: discard(elem)
    # Syntax: s.discard(x)
    # Description: Remove element x if present. Does nothing if x not in set.
    s = {1, 2, 3}
    s.discard(2)
    s.discard(4)
    print(s)  # Output: {1, 3}


def demo_intersection():
    # Method: intersection(other, ...)
    # Syntax: s.intersection(t)
    # Description: Return a new set with elements common to s and t.
    s = {1, 2, 3}
    t = {2, 3, 4}
    print(s.intersection(t))  # Output: {2, 3}


def demo_intersection_update():
    # Method: intersection_update(other, ...)
    # Syntax: s.intersection_update(t)
    # Description: Update set s, keeping only elements found in it and all others.
    s = {1, 2, 3}
    t = {2, 3, 4}
    s.intersection_update(t)
    print(s)  # Output: {2, 3}


def demo_isdisjoint():
    # Method: isdisjoint(other)
    # Syntax: s.isdisjoint(t)
    # Description: Return True if s has no elements in common with t.
    s = {1, 2}
    t = {3, 4}
    print(s.isdisjoint(t))  # Output: True


def demo_issubset():
    # Method: issubset(other)
    # Syntax: s.issubset(t)
    # Description: Return True if every element in s is in t.
    s = {1, 2}
    t = {1, 2, 3}
    print(s.issubset(t))    # Output: True


def demo_issuperset():
    # Method: issuperset(other)
    # Syntax: s.issuperset(t)
    # Description: Return True if every element in t is in s.
    s = {1, 2, 3}
    t = {1, 2}
    print(s.issuperset(t))  # Output: True


def demo_pop():
    # Method: pop()
    # Syntax: s.pop()
    # Description: Remove and return an arbitrary element. Raises KeyError if empty.
    s = {1, 2, 3}
    e = s.pop()
    print(e)    # Output: (arbitrary element, e.g., 1)
    print(s)    # Output: remaining elements, e.g., {2, 3}


def demo_remove():
    # Method: remove(elem)
    # Syntax: s.remove(x)
    # Description: Remove element x. Raises KeyError if not present.
    s = {1, 2, 3}
    s.remove(2)
    # s.remove(4) would raise KeyError
    print(s)  # Output: {1, 3}


def demo_symmetric_difference():
    # Method: symmetric_difference(other)
    # Syntax: s.symmetric_difference(t)
    # Description: Return a new set with elements in either s or t but not both.
    s = {1, 2, 3}
    t = {2, 3, 4}
    print(s.symmetric_difference(t))  # Output: {1, 4}


def demo_symmetric_difference_update():
    # Method: symmetric_difference_update(other)
    # Syntax: s.symmetric_difference_update(t)
    # Description: Update s, keeping only elements found in either s or t but not both.
    s = {1, 2, 3}
    t = {2, 3, 4}
    s.symmetric_difference_update(t)
    print(s)  # Output: {1, 4}


def demo_union():
    # Method: union(other, ...)
    # Syntax: s.union(t)
    # Description: Return a new set with elements from s and t.
    s = {1, 2}
    t = {2, 3}
    print(s.union(t))  # Output: {1, 2, 3}


def demo_update():
    # Method: update(other, ...)
    # Syntax: s.update(t)
    # Description: Update set s, adding elements from t.
    s = {1, 2}
    t = {2, 3}
    s.update(t)
    print(s)  # Output: {1, 2, 3}


if __name__ == '__main__':
    # Execute all demo functions
    for name, func in globals().items():
        if name.startswith('demo_') and callable(func):
            print(f"--- Running {name} ---")
            func()
            print()  # Blank line for readability