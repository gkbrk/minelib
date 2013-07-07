"""This file generates the packets according to the protocol at wiki.vg/Protocol.

"""

import data_type_parser

def packet_keepalive(keepalive_id):
    return data_type_parser.int(keepalive_id)

def packet_handshake(protocol_version,username,host,port):
    packet='\x02'+data_type_parser.byte(protocol_version)+data_type_parser.string16(username)+data_type_parser.string16(host)+data_type_parser.int(port)
    return packet

def packet_client_statuses(payload):
    packet='\xcd'+data_type_parser.byte(payload)
    return packet

def packet_chat_message(msg):
    packet='\x03'+data_type_parser.string16(msg)
    return packet
