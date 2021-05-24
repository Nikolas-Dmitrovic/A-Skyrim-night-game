class timing:

    def __init__(self, time):
        self.timings = time
        self.count = 0

    def __call__(self, func, *args,**kwargs):
        def innerfunc(*args,**kwargs):
            self.count += 1
            if self.count == self.timings:
                print(self.count)
                return func(*args,**kwargs)
        return innerfunc

    def set_time(self, time):
        self.timings = time