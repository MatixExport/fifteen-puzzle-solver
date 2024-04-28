import time

from src.ObserverMixin import ObserverMixin


class Logger(ObserverMixin):

    def __init__(self):
        super().__init__()
        self.elapsed_time = None
        self.solver = None
        self.solution = None
        self.max_depth = 0
        self.visited_states = 0
        self.processed_states = 0
        self.set_event_handlers()

    def on_depth(self, value):
        if value > self.max_depth:
            self.max_depth = value

    def on_processed(self, value):
        self.processed_states += value

    def on_visited(self, value):
        self.visited_states += value

    def set_event_handlers(self):
        self.add_event_handler("depth",self.on_depth)
        self.add_event_handler("visited", self.on_visited)
        self.add_event_handler("processed", self.on_processed)

    def timeit(self, method):
        def timed(*args, **kwargs):
            ts = time.time()
            result = method(*args, **kwargs)
            te = time.time()
            self.elapsed_time = '%r  %2.22f ms' % (method.__name__, (te - ts) * 1000)
            return result

        return timed

    def set_solver(self, solver):
        self.solver = solver
        self.solver.attach(self)

    @timeit
    def recorded_solve(self):
        self.solution = self.solver.solve()
        return self.solution
