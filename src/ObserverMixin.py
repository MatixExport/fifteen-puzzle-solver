class ObserverMixin:
    def __init__(self):
        self.event_handlers = {}

    def add_event_handler(self, name, func):
        self.event_handlers[name] = func

    def remove_event_handler(self, name):
        self.event_handlers.pop(name)

    def on_event(self, msg, value):
        if msg in self.event_handlers:
            self.event_handlers[msg](value)
