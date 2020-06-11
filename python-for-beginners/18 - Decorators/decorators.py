def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done Logging')
    return wrapper

@logger
def sample():
    print('--Inside sample function')

sample()