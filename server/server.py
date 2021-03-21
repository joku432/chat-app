from multiprocessing import Process
import socket
from server_properties import *

class Server:
    def __init__(self):
        self.listen_thread = None
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((SERVER_ADDRESS, SERVER_PORT))
        self._listen_on_thread()

    def listen(self):
        while True:
            conn, addr = self.sock.accept()
            if conn in self.clients:
                print('This connection already exists.')
            self.clients.append(conn)

    def _listen_on_thread(self):
        self.listen_thread = Process(target=self.listen)
        self.listen_thread.start()
    
    def _cleanup(self):
        for client in self.clients:
            client.close()
        self.listen_thread.join()


    def read_messages(self):
        try:
            while True:
                not_active = []
                for client in self.clients:
                    msg = client.recv(1024)
                    if not msg:
                        not_active.append(client)
                    
                    if msg[0] == '/':
                        # Command.
                        # CommandParser.parse(msg)

                for client in not_active:
                    self.clients.remove(client)
        except Exception as e:
            self._cleanup()
        
            
