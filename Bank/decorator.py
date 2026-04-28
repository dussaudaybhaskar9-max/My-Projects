import time
def delay(func):
    def inner_func(*args,**kwrgs):
        time.sleep(5)
        func(*args,**kwrgs)
    return inner_func
