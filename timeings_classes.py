
# TODO add timer reset functionality to reset and reuse decorator

class timing:

    def __init__(self, time):
        # multiplies time in seconds by game tick rate
        self.timings = time*60
        self.count = 0

    def __call__(self, func, *args,**kwargs):
        def innerfunc(*args,**kwargs):
            self.count += 1
            if self.count == self.timings:
                print(self.count)
                return func(*args,**kwargs)
        return innerfunc
