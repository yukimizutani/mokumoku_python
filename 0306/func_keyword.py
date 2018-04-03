def parrot(voltage, state="a stiff", action="voo", type="Norwegian Blue"):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print("******")


def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


def concat(*args, sep="/"):
    return sep.join(args)


def make_incrementor(n):
    return lambda x: x + n

def p(q):
    return q[1]


def my_function():
    """
    Do nothing, but document it.
    No, really, it does't do anything.
    """
    pass

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


# print(my_function.__doc__)

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=p)
# pairs.sort(key=lambda pair: pair[1])

# f = make_incrementor(42)
# print(f(0))
# print(f(1))


# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

#write_multiple_items(open("test.txt", "w"), ",", "a", "b", "c")
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# parrot(1000)
# parrot(voltage=1000, action="VOOM")
# parrot(action="VOOM", voltage=1000)
# parrot('a million', 'bereft of life', 'jump')
# parrot(actor='John Cleese')
