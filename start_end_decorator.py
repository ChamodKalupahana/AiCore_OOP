def print_start_end(func):
    def wrapper(*args):
        print('This is the start of function')
        func(*args)
        print('This is the end of function')
    return wrapper

@print_start_end
def example_function(x):
    print('You inputted:', str(x))
    pass

example_function(10)