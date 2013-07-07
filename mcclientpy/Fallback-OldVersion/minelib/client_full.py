import Queue
import data_type_parser
import packet_generators
import packet_parsers
import threading
import minelib
import io
import cStringIO

class packet_listener(threading.Thread):    
    def run(self):
        while True:
            data=connection.recv(100000)
            if data!="":
                parse_packet(data)

def parse_packet(data):
    packet_id=ord(data[0])
    data=cStringIO.StringIO(data)
    if packet_id==0x00:
        print "Got keep-alive. Responding..."
        keepalive_id=data_type_parser.parse_int(data)
        connection.send("\x00"+data_type_parser.int(keepalive_id))

client=minelib.cracked_client("GKBRKbot")
connection=client.connect_to_server("localhost",25565)
client.packet_handshake(connection)
client.packet_client_statuses(connection,0)
packet_listener().start()
import time
time.sleep(1)
client.packet_chat_message(connection,"Hello MineLib!")
