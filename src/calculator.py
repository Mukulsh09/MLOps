def fun1(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def fun2(x, y):
    """Subtracts y from x and returns the result."""
    return x - y

def fun3(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

def fun4(x, y):
    """Combines results of fun1, fun2, and fun3 and returns their sum."""
    return fun1(x, y) + fun2(x, y) + fun3(x, y)

def fun5(x, y):
    """Divides x by y and returns the result. Returns 0 if y is 0."""
    if y == 0:
        return 0
    return x / y
