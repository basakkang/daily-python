import datetime
import functools
import time

def do_not_disturb(func):
    now = datetime.datetime.now()
    hour = now.hour
    def wrapper(*args, **kwargs):
        if hour > 23 or hour < 7:
            print('do not disturb mode')
        else:
            func(*args, **kwargs)

    return wrapper

@do_not_disturb
def alert_message(message):
    print(message)

if __name__ == "__main__":
    alert_message('what are you doing?')
