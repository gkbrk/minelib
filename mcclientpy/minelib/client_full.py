import data_type_parser
import packet_generators
import packet_parsers
import threading
import minelib

class packet_listener(threading.Thread):    
    def run(self):
        while True:
            data=connection.recv(100000)
            if data!="":
                parse_packet(data)

class packet_listener1(threading.Thread):    
    def run(self):
        while True:
            packet_id=connection.recv(1)
            if not packet_id=="":
                if ord(packet_id) in packet_functions:
                    function=packet_functions[ord(packet_id)](connection)
                else:
                    print ord(packet_id)
                    import sys
                    sys.exit()

packet_functions={
0x00:packet_parsers.parse_keepalive,
0x01:packet_parsers.parse_login_request,
0x03:packet_parsers.parse_chat_message,
0x04:packet_parsers.parse_time_update,
0x05:packet_parsers.parse_entity_equipment,
0x06:packet_parsers.parse_spawn_position,
0x08:packet_parsers.parse_health_update,
0x09:packet_parsers.parse_respawn,
0x0d:packet_parsers.parse_player_pos_and_look,
0x10:packet_parsers.parse_held_item_change,
0x11:packet_parsers.parse_use_bed,
0x12:packet_parsers.parse_animation,
0x14:packet_parsers.parse_spawn_named_entity,
0x16:packet_parsers.parse_collect_item,
0x19:packet_parsers.parse_spawn_painting,
0x1a:packet_parsers.parse_spawn_exp_orb,
0x1c:packet_parsers.parse_entity_velocity,
0x1d:packet_parsers.parse_destroy_entity,
0x1e:packet_parsers.parse_entity,
0x1f:packet_parsers.parse_entity_relative_move,
0x20:packet_parsers.parse_entity_look,
0x21:packet_parsers.parse_entity_look_and_relative_move,
0x22:packet_parsers.parse_entity_teleport,
0x23:packet_parsers.parse_entity_head_look,
0x26:packet_parsers.parse_entity_status,
0x27:packet_parsers.parse_attach_entity,
0x29:packet_parsers.parse_entity_effect,
0x2a:packet_parsers.parse_remove_entity_effect,
0x2b:packet_parsers.parse_set_experience,
0x33:packet_parsers.parse_chunk_data
}

client=minelib.custom_client("GKBRKbot")
connection=client.connect_to_server("localhost",25565)
client.packet_handshake(connection)
client.packet_client_statuses(connection,0)
packet_listener1().start()
