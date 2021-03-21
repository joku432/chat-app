from robot.api.deco import keyword
from client import client
from server import server

class ChatLib:
    def __init__(self):
        self.server = None

    @keyword
    def start_server(self):
        if not self.server:
            self.server = server.Server() 

    @keyword
    def close_server(self):
        if self.server is not None:
            self.server._cleanup()
            self.server = None
