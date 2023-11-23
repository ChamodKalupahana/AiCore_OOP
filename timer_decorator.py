import time

# measure time elpashed during function
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        total_time = time.time() - start_time
        print('Total time for function:', str(total_time))
    return wrapper

@timer
def example_function(x, test=10):
    # x is to test *args
    # test=10 is to test **kwargs
    print('You inputted:', str(x))
    time.sleep(1)
    pass

example_function(10)