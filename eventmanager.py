# super class for all events
class Event:

    def __init__(self):
        self.name = "Generic event"

    def __str__(self):
        return self.name


class QuitEvent(Event):

    def __init__(self):
        self.name = "Quit event"


class TickEvent(Event):

    def __init__(self):
        self.name = "Tick event"


class InputEvent(Event):

    def __init__(self, unicodechar, clickpos):
        self.name = "Input event"
        self.char = unicodechar
        self.clickpos = clickpos

    def __str__(self):
        return f'{self.name}, char={self.char}, clickpos={self.clickpos}'


class InitializeEvent(Event):

    def __init__(self):
        self.name = "Initialize event"


class EventManager:

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    # add event to message queue
    def Post(self, event):

        if not isinstance(event, TickEvent):
            # print the event (unless it is TickEvent)
            print(str(event))
        for listener in self.listeners.keys():
            listener.notify(event)
