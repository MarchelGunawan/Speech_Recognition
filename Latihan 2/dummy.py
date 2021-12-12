from threading import Timer

class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)

def dummyfn(msg="foo"):
    print(msg)

timer = RepeatTimer(1, dummyfn)
timer.start()
time.sleep(1)
timer.cancel()