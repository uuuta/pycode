import threading
import time


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.wait = True
        self.counter = 0
        self.next_call = time.perf_counter()

    def _run(self):
        if self.wait:
            self._restart()
        self.function(*self.args, **self.kwargs)
        if not self.wait:
            self._restart()

    def _restart(self):
        if self.is_running:
            self._set_timer()

    def _set_timer(self):
        self.next_call += self.interval
        self._timer = threading.Timer(self.next_call - time.perf_counter(), self._run)
        self._timer.start()

    def start(self, wait=True):
        self.next_call = time.perf_counter()
        self.wait = wait
        self.is_running = True
        self._set_timer()

    def stop(self):
        self._timer.cancel()
        self.is_running = False
