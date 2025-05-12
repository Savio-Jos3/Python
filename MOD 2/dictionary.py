"""
Comprehensive Python Dictionary Methods - Single File Reference

This script demonstrates all built-in dictionary methods with:
- Syntax
- Description
- Example usage
- Expected output (as comments)
"""

def demo_clear():
    # Method: clear()
    # Syntax: dict.clear()
    # Description: Remove all items from the dictionary.
    d = {'a': 1, 'b': 2}
    d.clear()
    print(d)  # Output: {}


def demo_copy():
    # Method: copy()
    # Syntax: dict.copy()
    # Description: Return a shallow copy of the dictionary.
    original = {'x': 10, 'y': [20, 30]}
    cp = original.copy()
    cp['y'].append(40)
    print(original)  # Output: {'x': 10, 'y': [20, 30, 40]}
    print(cp)        # Output: {'x': 10, 'y': [20, 30, 40]}


def demo_fromkeys():
    # Method: fromkeys(iterable, value=None)
    # Syntax: dict.fromkeys(['a','b'], 0)
    # Description: Create new dict with keys from iterable and values set to value.
    keys = ('name', 'age')
    new_dict = dict.fromkeys(keys, 'unknown')
    print(new_dict)  # Output: {'name': 'unknown', 'age': 'unknown'}


def demo_get():
    # Method: get(key, default=None)
    # Syntax: dict.get('key', default)
    # Description: Return value for key if key in dict, else default.
    d = {'a': 1}
    print(d.get('a'))        # Output: 1
    print(d.get('b', 0))     # Output: 0


def demo_items():
    # Method: items()
    # Syntax: dict.items()
    # Description: Return a view object of (key, value) pairs.
    d = {'a': 1, 'b': 2}
    print(list(d.items()))   # Output: [('a', 1), ('b', 2)]


def demo_keys():
    # Method: keys()
    # Syntax: dict.keys()
    # Description: Return a view object of dictionary keys.
    d = {'a': 1, 'b': 2}
    print(list(d.keys()))    # Output: ['a', 'b']


def demo_pop():
    # Method: pop(key, default)
    # Syntax: dict.pop('a', None)
    # Description: Remove specified key and return the value. If key not found, return default or raise KeyError.
    d = {'a': 1, 'b': 2}
    val = d.pop('a')
    print(val)  # Output: 1
    print(d)    # Output: {'b': 2}


def demo_popitem():
    # Method: popitem()
    # Syntax: dict.popitem()
    # Description: Remove and return a (key, value) pair. Raises KeyError if dict is empty.
    d = {'a': 1, 'b': 2}
    item = d.popitem()
    print(item)  # Output: ('b', 2)  # last inserted pair
    print(d)     # Output: {'a': 1}


def demo_setdefault():
    # Method: setdefault(key, default=None)
    # Syntax: dict.setdefault('a', 0)
    # Description: If key in dict, return its value. If not, insert key with default and return default.
    d = {'x': 5}
    print(d.setdefault('x', 0))  # Output: 5  (existing)
    print(d.setdefault('y', 10)) # Output: 10 (inserted)
    print(d)                     # Output: {'x': 5, 'y': 10}


def demo_update():
    # Method: update([other])
    # Syntax: dict.update({'a':1, 'b':2})
    # Description: Update dictionary with key/value pairs from other, overwriting existing keys.
    d = {'a': 1}
    d.update({'b': 2, 'a': 3})
    print(d)  # Output: {'a': 3, 'b': 2}


def demo_values():
    # Method: values()
    # Syntax: dict.values()
    # Description: Return a view object of dictionary values.
    d = {'a': 1, 'b': 2}
    print(list(d.values()))    # Output: [1, 2]


if __name__ == '__main__':
    # Execute all demo functions
    for name, func in globals().items():
        if name.startswith('demo_') and callable(func):
            print(f"--- Running {name} ---")
            func()
            print()  # Blank line for readability