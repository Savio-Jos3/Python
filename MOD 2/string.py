"""
Comprehensive Python String Methods - Single File Reference

Contains all 38 built-in string methods with syntax, description,
example code, and expected outputs as comments.
"""

def demo_capitalize():
    # capitalize(): first char uppercase, rest lowercase
    s = "hello WORLD"
    print(s.capitalize())  # Hello world

def demo_casefold():
    # casefold(): aggressive lowercase for caseless matching
    s = "Straße"
    print(s.casefold())     # strasse

def demo_center():
    # center(width, fillchar)
    s = "cat"
    print(s.center(10, '-'))  # ---cat----

def demo_count():
    # count(sub)
    s = "banana"
    print(s.count('a'))       # 3
    print(s.count('an'))      # 2

def demo_encode():
    # encode(encoding, errors)
    s = "hello"
    b = s.encode('utf-8')
    print(b)                  # b'hello'

def demo_endswith():
    # endswith(suffix)
    s = "example.py"
    print(s.endswith('.py'))  # True

def demo_expandtabs():
    # expandtabs(tabsize)
    s = "a\tb"
    print(s.expandtabs(4))    # a   b

def demo_find():
    # find(sub)
    s = "hello"
    print(s.find('l'))        # 2
    print(s.find('x'))        # -1

def demo_format():
    # format(*args)
    print("{} + {} = {}".format(2,3,5))  # 2 + 3 = 5

def demo_index():
    # index(sub)
    s = "hello"
    print(s.index('e'))       # 1

def demo_isalnum():
    # isalnum()
    print("abc123".isalnum())  # True
    print("abc!".isalnum())    # False

def demo_isalpha():
    # isalpha()
    print("abc".isalpha())     # True

def demo_isdigit():
    # isdigit()
    print("123".isdigit())     # True

def demo_islower():
    # islower()
    print("hello".islower())   # True

def demo_isspace():
    # isspace()
    print(" \t\n".isspace())  # True

def demo_istitle():
    # istitle()
    print("Hello World".istitle())  # True

def demo_isupper():
    # isupper()
    print("HELLO".isupper())   # True

def demo_join():
    # join(iterable)
    print("-".join(['a','b','c']))  # 'a-b-c'

def demo_ljust():
    # ljust(width, fillchar)
    s = "cat"
    print(s.ljust(5, '.'))     # cat..

def demo_lower():
    # lower()
    print("HELLO".lower())    # hello

def demo_lstrip():
    # lstrip(chars)
    s = "   hello"
    print(s.lstrip())          # hello

def demo_partition():
    # partition(sep)
    s = "key=value=more"
    print(s.partition('='))    # ('key','=', 'value=more')

def demo_replace():
    # replace(old,new,count)
    s = "one one one"
    print(s.replace('one','two',2))  # two two one

def demo_rfind():
    # rfind(sub)
    s = "banana"
    print(s.rfind('a'))        # 5

def demo_rindex():
    # rindex(sub)
    s = "banana"
    print(s.rindex('a'))       # 5

def demo_rjust():
    # rjust(width,fillchar)
    s = "cat"
    print(s.rjust(5, '.'))     # ..cat

def demo_rpartition():
    # rpartition(sep)
    s = "key=value=more"
    print(s.rpartition('='))   # ('key=value','=', 'more')

def demo_rsplit():
    # rsplit(sep,maxsplit)
    s = "a,b,c,d"
    print(s.rsplit(',',2))    # ['a,b','c','d']

def demo_rstrip():
    # rstrip(chars)
    s = "hello   "
    print(s.rstrip())         # hello

def demo_split():
    # split(sep,maxsplit)
    s = "one two  three"
    print(s.split())          # ['one','two','three']

def demo_splitlines():
    # splitlines(keepends)
    s = "a\nb\r\nc"
    print(s.splitlines())     # ['a','b','c']

def demo_startswith():
    # startswith(prefix)
    s = "python"
    print(s.startswith('py'))  # True

def demo_strip():
    # strip(chars)
    s = "***hello***"
    print(s.strip('*'))       # hello

def demo_swapcase():
    # swapcase()
    s = "Hello World"
    print(s.swapcase())       # hELLO wORLD

def demo_title():
    # title()
    s = "hello world"
    print(s.title())          # Hello World

def demo_translate():
    # translate(table)
    s = "abc xyz"
    tab = str.maketrans('abc','123')
    print(s.translate(tab))   # 123 xyz

def demo_upper():
    # upper()
    print("hello".upper())   # HELLO

def demo_zfill():
    # zfill(width)
    s = "42"
    print(s.zfill(5))          # 00042

if __name__ == '__main__':
    # Call all demos
    for name, func in globals().items():
        if name.startswith('demo_'):
            print(f"--- {name} ---")
            func()
            print()