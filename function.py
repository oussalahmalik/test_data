from pip import main


def add(a, b):
    """
        args: hello
        a: int
        b: int
    """
    return a + b

if __name__ == "__main__":
    c = add(10, 20)
    print(c)