import socket
import struct
import data_type_parser
import packet_generators
import packet_parsers
import client_full


class custom_client():
    def __init__(self, username="Player"):
        self.username = username

    def get_serverlist_ping(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        server_ping_package = struct.pack("!BB", 0xFE, 0x01)
        s.send(server_ping_package)

        data = s.recv(1024)

        s.close()

        data = data[3:].decode("utf-16be")
        data = data[3:].split("\x00")

        results = {}
        results["ProtocolVersion"] = data[0]
        results["ServerVersion"] = data[1]
        results["MOTD"] = data[2]
        results["OnlinePlayers"] = data[3]
        results["MaxPlayers"] = data[4]
        return results

    def connect_to_server(self, host, port):
        self.host = host
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((host, port))

    def packet_handshake(self):
        username = self.username
        host = self.host
        port = self.port
        packet = packet_generators.packet_handshake(61, username, host, port)
        self.connection.send(packet)
        data = self.connection.recv(1024)
        if data[0] == "\xfd":
            return True
        else:
            return False

    def packet_client_statuses(self, payload=0):
        packet = packet_generators.packet_client_statuses(payload)
        self.connection.send(packet)

    def packet_chat_message(self, s, msg):
        packet = packet_generators.packet_chat_message(msg)
        s.send(packet)
    
    def do_server_login(self, host, port=25565, join_message="Hello Minelib!"):
        self.connect_to_server(host, port)
        self.packet_handshake()
        self.packet_client_statuses(0)
        client_full.packet_listener(self.connection).start()
        return self
    
    def disconnect(self, reason="Disconnected by user!"):
        self.connection.send(packet_generators.packet_disconnect(reason))
