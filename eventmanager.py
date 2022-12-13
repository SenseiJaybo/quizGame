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


class InitializeEvent(Event):

    def __init__(self):
        self.name = "Initialize event"


class StateChangeEvent(Event):

    def __init__(self, state):
        self.name = "State change event"
        self.state = state

    def __str__(self):
        if self.state:
            return '%s pushed %s' % (self.name, self.state)
        else:
            return '%s popped' % (self.name,)


class AudioEvent(Event):

    def __init__(self):
        self.name = "Audio event"


class EventManager:

    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    # add event to message queue
    def Post(self, event):

        if not isinstance(event, TickEvent):
            # print the event (unless it is TickEvent)
            print(str(event))
        for listener in self.listeners.keys():
            listener.notify(event)
