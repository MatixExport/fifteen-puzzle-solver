import time


class Logger:

    def __init__(self):
        self.elapsed_time = None
        self.solver = None

    def timeit(self, method):
        def timed(*args, **kwargs):
            ts = time.time()
            result = method(*args, **kwargs)
            te = time.time()
            self.elapsed_time = '%r  %2.22f ms' % (method.__name__, (te - ts) * 1000)
            return result

        return timed

    def on_event(self, msg, value):
        pass

    def set_solver(self, solver):
        self.solver = solver
        self.solver.attach(self)

    @timeit
    def recorded_solve(self):
        return self.solver.solve()
