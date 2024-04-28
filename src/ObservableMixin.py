class ObservableMixin:
    def __int__(self):
        self.observer_list = []

    def attach(self, observer):
        self.observer_list.append(observer)

    def detach(self, observer):
        self.observer_list.remove(observer)

    def notify(self, msg, value):
        for observer in self.observer_list:
            observer.on_event(msg, value)
