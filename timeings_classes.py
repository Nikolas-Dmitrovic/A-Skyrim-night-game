# TODO add timer reset functionality to reset and reuse decorator

class wait:

    def __init__(self, time):
        # multiplies time in seconds by game tick rate
        self.timings = time * 60
        self.count = 0

    def __call__(self, func, *args, **kwargs):
        def innerfunc(*args, **kwargs):
            self.count += 1
            if self.count == self.timings:
                return func(*args, **kwargs)

        return innerfunc


class waitFor:

    def __init__(self, time):
        self.timings = time * 60
        self.count = 0

    def __call__(self):
        if self.count == self.timings:
            return True
        else:
            return False


class do_for:

    def __init__(self, target_count):
        self.max = target_count
        self.count = 0

    def __call__(self, func, *args, **kwargs):

        def innerfunc(*args, **kwargs):
            if self.count <= self.max:
                return func(*args, **kwargs)
            if self.count > self.max:
                return

        return innerfunc
