import packet_parsers
import threading
import minelib

class packet_listener(threading.Thread):
    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.packet_functions = {
            0x00: packet_parsers.parse_keepalive,
            0x01: packet_parsers.parse_login_request,
            0x03: packet_parsers.parse_chat_message,
            0x04: packet_parsers.parse_time_update,
            0x05: packet_parsers.parse_entity_equipment,
            0x06: packet_parsers.parse_spawn_position,
            0x08: packet_parsers.parse_health_update,
            0x09: packet_parsers.parse_respawn,
            0x0d: packet_parsers.parse_player_pos_and_look,
            0x10: packet_parsers.parse_held_item_change,
            0x11: packet_parsers.parse_use_bed,
            0x12: packet_parsers.parse_animation,
            0x14: packet_parsers.parse_spawn_named_entity,
            0x16: packet_parsers.parse_collect_item,
            0x17: packet_parsers.parse_spawn_object_vehicle,
            0x18: packet_parsers.parse_spawn_mob,
            0x19: packet_parsers.parse_spawn_painting,
            0x1a: packet_parsers.parse_spawn_exp_orb,
            0x1c: packet_parsers.parse_entity_velocity,
            0x1d: packet_parsers.parse_destroy_entity,
            0x1e: packet_parsers.parse_entity,
            0x1f: packet_parsers.parse_entity_relative_move,
            0x20: packet_parsers.parse_entity_look,
            0x21: packet_parsers.parse_entity_look_and_relative_move,
            0x22: packet_parsers.parse_entity_teleport,
            0x23: packet_parsers.parse_entity_head_look,
            0x26: packet_parsers.parse_entity_status,
            0x27: packet_parsers.parse_attach_entity,
            0x28: packet_parsers.parse_entity_metadata,
            0x29: packet_parsers.parse_entity_effect,
            0x2a: packet_parsers.parse_remove_entity_effect,
            0x2b: packet_parsers.parse_set_experience,
            0x2c: packet_parsers.parse_entity_properties,
            0x33: packet_parsers.parse_chunk_data,
            0x34: packet_parsers.parse_multi_block_change,
            0x35: packet_parsers.parse_block_change,
            0x38: packet_parsers.parse_map_chunk_bulk,
            0x3d: packet_parsers.parse_sound_or_particle_effect,
            0x3e: packet_parsers.parse_named_sound_effect,
            0x46: packet_parsers.parse_change_game_state,
            0x67: packet_parsers.parse_set_slot,
            0x68: packet_parsers.parse_set_window_items,
            0x69: packet_parsers.parse_update_window_property,
            0x84: packet_parsers.parse_update_tile_entity,
            0xc8: packet_parsers.parse_increment_statistic,
            0xc9: packet_parsers.parse_player_list_item,
            0xca: packet_parsers.parse_player_abilities,
            0xfa: packet_parsers.parse_plugin_message,
            0xfd: packet_parsers.parse_encryption_key_request,
            0xff: packet_parsers.parse_disconnect_kick
        }
        self.connection=connection
    def run(self):
        packet_functions=self.packet_functions
        connection=self.connection
        while True:
            fileobj = connection.makefile()
            packet_id = ord(fileobj.read(1))
            if packet_id in packet_functions:
                print packet_functions[packet_id](fileobj, connection)
            else:
                print "Got unknown packet."
                print "The packet ID is ",
                print packet_id
                import sys
                sys.exit()
