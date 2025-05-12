"""
Comprehensive Python List Methods - Single File Reference

Contains all built-in list methods with syntax, description,
example code, and expected outputs as comments.
"""

def demo_append():
    # append(x): Add an item to the end of the list.
    lst = [1, 2, 3]
    lst.append(4)
    print(lst)  # [1, 2, 3, 4]

def demo_extend():
    # extend(iterable): Extend list by appending elements from the iterable.
    lst = [1, 2]
    lst.extend([3, 4])
    print(lst)  # [1, 2, 3, 4]

def demo_insert():
    # insert(i, x): Insert an item at a given position.
    lst = [1, 3, 4]
    lst.insert(1, 2)
    print(lst)  # [1, 2, 3, 4]

def demo_remove():
    # remove(x): Remove first occurrence of value.
    lst = [1, 2, 3, 2]
    lst.remove(2)
    print(lst)  # [1, 3, 2]

def demo_pop():
    # pop([i]): Remove and return item at index (default last).
    lst = [1, 2, 3]
    item = lst.pop()
    print(item)  # 3
    print(lst)   # [1, 2]

def demo_clear():
    # clear(): Remove all items from the list.
    lst = [1, 2, 3]
    lst.clear()
    print(lst)  # []

def demo_index():
    # index(x[, start[, end]]): Return first index of value.
    lst = ['a', 'b', 'c', 'b']
    print(lst.index('b'))       # 1
    # print(lst.index('x')) would raise ValueError

def demo_count():
    # count(x): Return number of occurrences of value.
    lst = [1, 2, 2, 3, 2]
    print(lst.count(2))         # 3

def demo_sort():
    # sort(key=None, reverse=False): Sort list in place.
    lst = [3, 1, 2]
    lst.sort()
    print(lst)  # [1, 2, 3]
    lst.sort(reverse=True)
    print(lst)  # [3, 2, 1]

def demo_reverse():
    # reverse(): Reverse the elements of the list in place.
    lst = [1, 2, 3]
    lst.reverse()
    print(lst)  # [3, 2, 1]

def demo_copy():
    # copy(): Return a shallow copy of the list.
    lst = [1, 2, [3, 4]]
    lst_copy = lst.copy()
    lst_copy[2].append(5)
    print(lst)       # [1, 2, [3, 4, 5]]
    print(lst_copy)  # [1, 2, [3, 4, 5]]

if __name__ == '__main__':
    # Execute all demos
    for name, func in globals().items():
        if name.startswith('demo_'):
            print(f"--- {name} ---")
            func()
            print()