import uuid
import threading
from functools import wraps


def delay(delay=0.):
    def wrap(f):
        @wraps(f)
        def delayed(*args, **kwargs):
            timer = threading.Timer(delay, f, args=args, kwargs=kwargs)
            timer.start()
        return delayed
    return wrap


class Timer:
    callbacks = []

    def run(self, fn, time):
        @delay(time)
        def run_function():
            if callback_id in self.callbacks:
                fn()

        callback_id = uuid.uuid4()
        run_function()
        self.callbacks.append(callback_id)
        return callback_id

    def clear(self, callback_id = None):
        if callback_id:
            try:
                self.callbacks.remove(callback_id)
            except Exception as e:
                print("There is no id: " + str(callback_id))
        else:
            self.callbacks = []


SET_TIMEOUT = Timer()


"""
def some_fn():
    print('Run later')
    
id1 = SET_TIMEOUT.run(some_fn, 3.0)
id2 = SET_TIMEOUT.run(some_fn, 2.0)
SET_TIMEOUT.clear(id1)
"""
