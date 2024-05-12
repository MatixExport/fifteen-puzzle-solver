import time

from ObserverMixin import ObserverMixin
from timeit import default_timer as timer


def timeit(f):
    def wrapper(*args):
        instance = args[0]
        start = timer()
        result = f(*args)
        end = timer()
        instance.elapsed_time = round((end - start) * 1000, 3)
        return result

    return wrapper


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

    def clear(self):
        self.elapsed_time = None
        self.solver = None
        self.solution = None
        self.max_depth = 0
        self.visited_states = 0
        self.processed_states = 0

    def on_depth(self, value):
        if value > self.max_depth:
            self.max_depth = value

    def on_processed(self, value):
        self.processed_states += value

    def on_visited(self, value):
        self.visited_states += value

    def set_event_handlers(self):
        self.add_event_handler("depth", self.on_depth)
        self.add_event_handler("visited", self.on_visited)
        self.add_event_handler("processed", self.on_processed)

    def set_solver(self, solver):
        self.clear()
        self.solver = solver
        self.solver.attach(self)

    @timeit
    def recorded_solve(self):
        self.solution = self.solver.solve()
        return self.solution

    def parse_recorded_information(self):
        info = ""
        if self.solution:
            info += str(len(self.solution)) + "\n"
        info += str(self.visited_states) + "\n"
        info += str(self.processed_states) + "\n"
        info += str(self.max_depth) + "\n"
        info += str(self.elapsed_time) + "\n"
        return info

