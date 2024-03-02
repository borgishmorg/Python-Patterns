# Echo server program
# Based on https://docs.python.org/3/library/selectors.html#examples
# and https://www.dre.vanderbilt.edu/~schmidt/PDF/reactor-siemens.pdf

import selectors
import socket
from abc import ABC, abstractmethod


class SynchronousEventDemultiplexer:
    def __init__(self, selector: selectors.BaseSelector) -> None:
        self.selector = selector
    
    def select(self):
        return self.selector.select()

class InitiationDispatcher:
    def __init__(self) -> None:
        self.selector = selectors.DefaultSelector()

    def handle_events(self):
        while True:
            events = self.selector.select()
            for key, mask in events:
                handler: EventHandler = key.data
                handler.handle_event(mask)

    def register_handler(self, handler: 'EventHandler'):
        self.selector.register(
            handler.get_handle(),
            events=selectors.EVENT_READ|selectors.EVENT_WRITE,
            data=handler,
        )
    
    def remove_handler(self, handler: 'EventHandler'):
        self.selector.unregister(handler.get_handle())


class EventHandler(ABC):
    def __init__(self, socket: socket.socket, dispatcher: InitiationDispatcher) -> None:
        self.socket = socket
        self.dispatcher = dispatcher

    @abstractmethod
    def handle_event(self, event_type: int):
        pass

    def get_handle(self):
        return self.socket


class AcceptEventHandler(EventHandler):
    def handle_event(self, event_type: int):
        if event_type & selectors.EVENT_READ:
            conn, addr = self.socket.accept()  # Should be ready
            conn.setblocking(False)

            handler = ReadEventHandler(
                socket=conn,
                dispatcher=self.dispatcher,
            )
            self.dispatcher.register_handler(handler)


class ReadEventHandler(EventHandler):
    def __init__(self, socket: socket.socket, dispatcher: InitiationDispatcher) -> None:
        super().__init__(socket, dispatcher)

        self.data = None

    def handle_event(self, event_type: int):
        if event_type & selectors.EVENT_READ:
            self.data = self.socket.recv(1024)  # Should be ready
        if event_type & selectors.EVENT_WRITE:
            if self.data:
                self.socket.send(self.data)  # Should be ready
            self.dispatcher.remove_handler(self)
            self.socket.close()


HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(100)
    s.setblocking(False)

    initialisation_dispatcher = InitiationDispatcher()
    accept_handler = AcceptEventHandler(
        socket=s,
        dispatcher=initialisation_dispatcher,
    )
    initialisation_dispatcher.register_handler(accept_handler)
    initialisation_dispatcher.handle_events()
