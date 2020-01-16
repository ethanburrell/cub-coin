class MyBroadcaster():
    def __init__(self):
        self.onChange = EventHook()


class EventHook(object):

    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def fire(self, *args, **keywargs):
        for handler in self.__handlers:
            handler(*args, **keywargs)

    def clearObjectHandlers(self, inObject):
        self.__handlers = [h for h in self._handlers if getattr(h, 'im_self', False) != obj]
        """
        for theHandler in self.__handlers:
            if theHandler.im_self == inObject:
                self -= theHandler
        """
