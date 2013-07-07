import socket
import struct
import data_type_parser
import packet_generators
import packet_parsers

class cracked_client():
    def __init__(self,username="Player"):
        self.username=username
    
    def get_serverlist_ping(self,host,port):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        
        server_ping_package=struct.pack("!BB",0xFE,0x01)
        s.send(server_ping_package)
        
        data=s.recv(1024)
        
        s.close()
        
        data=data[3:].decode("utf-16be")
        data=data[3:].split("\x00")
        
        results={}
        results["ProtocolVersion"]=data[0]
        results["ServerVersion"]=data[1]
        results["MOTD"]=data[2]
        results["OnlinePlayers"]=data[3]
        results["MaxPlayers"]=data[4]
        return results
    
    def connect_to_server(self,host,port):
        self.host=host
        self.port=port
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        return s
    
    def packet_handshake(self,s):
        username=self.username
        host=self.host
        port=self.port
        packet=packet_generators.packet_handshake(61,username,host,port)
        s.send(packet)
        data=s.recv(1024)
        if data[0]=="\xfd":
            return True
        else:
            return False
    
    def packet_client_statuses(self,s,payload=0):
        packet=packet_generators.packet_client_statuses(payload)
        s.send(packet)
    
    def packet_chat_message(self,s,msg):
        packet=packet_generators.packet_chat_message(msg)
        s.send(packet)
