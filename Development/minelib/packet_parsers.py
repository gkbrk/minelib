"""This file is used to parse the packets returned by the server."""

import data_type_parser
import mc_datatype
import packet_generators
import cStringIO


def makeio(string):
    return cStringIO.StringIO(string)


def parse_keepalive(fileobj, socket):
    keepalive_id = data_type_parser.parse_int(fileobj)
    print "Got keepalive. Responding"
    socket.send(packet_generators.packet_keepalive(keepalive_id))


def parse_login_request(fileobj, socket):
    result = {}
    result['EntityID'] = data_type_parser.parse_int(fileobj)
    result['LevelType'] = mc_datatype.readString(fileobj)
    result["GameMode"] = data_type_parser.parse_byte(fileobj)
    result["Dimension"] = data_type_parser.parse_byte(fileobj)
    result["Difficulty"] = data_type_parser.parse_byte(fileobj)
    result["NotUsed"] = data_type_parser.parse_byte(fileobj)
    result["MaxPlayers"] = data_type_parser.parse_byte(fileobj)
    return result


def parse_spawn_position(fileobj, socket):
    result = {}
    result["X"] = data_type_parser.parse_int(fileobj)
    result["Y"] = data_type_parser.parse_int(fileobj)
    result["Z"] = data_type_parser.parse_int(fileobj)
    return result


def parse_chat_message(fileobj, socket):
    chat_message = mc_datatype.readString(fileobj)
    return chat_message


def parse_time_update(fileobj, socket):
    result = {}
    result["WorldAge"] = data_type_parser.parse_long(fileobj)
    result["TimeOfDay"] = data_type_parser.parse_long(fileobj)
    return result


def parse_entity_equipment(fileobj, socket):
    result = {}
    result["EntityID"] = data_type_parser.parse_int(fileobj)
    result["Slot"] = data_type_parser.parse_short(fileobj)
    result["SlotData"] = mc_datatype.readSlotData(fileobj)
    return result


def parse_health_update(fileobj, socket):
    result = {}
    result["Health"] = data_type_parser.parse_int(fileobj)
    result["Food"] = data_type_parser.parse_int(fileobj)
    result["FoodSaturation"] = data_type_parser.parse_float(fileobj)
    return result


def parse_respawn(fileobj, socket):
    result = {}
    result["Dimension"] = data_type_parser.parse_int(fileobj)
    result["Difficulty"] = data_type_parser.parse_byte(fileobj)
    result["GameMode"] = data_type_parser.parse_byte(fileobj)
    result["WorldHeight"] = data_type_parser.parse_short(fileobj)
    result["LevelType"] = mc_datatype.readString(fileobj)
    return result


def parse_player_pos_and_look(fileobj, socket):
    # Not fully implemented. Just responding with an appropriate packet.
    socket.send("0x0d" + fileobj.read(41))


def parse_held_item_change(fileobj, socket):
    slot_id = data_type_parser.parse_short(fileobj)
    return slot_id


def parse_use_bed(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(14)


def parse_animation(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(5)


def parse_spawn_named_entity(fileobj, socket):
    # Not implemented yet.
    pass


def parse_collect_item(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(8)


def parse_spawn_painting(fileobj, socket):
    result = {}
    result["EntitiyID"] = data_type_parser.parse_int(fileobj)
    result["Title"] = mc_datatype.readString(fileobj)
    result["X"] = data_type_parser.parse_int(fileobj)
    result["Y"] = data_type_parser.parse_int(fileobj)
    result["Z"] = data_type_parser.parse_int(fileobj)
    result["Direction"] = data_type_parser.parse_int(fileobj)
    return result


def parse_spawn_exp_orb(fileobj, socket):
    result = {}
    result["EntityID"] = data_type_parser.parse_int(fileobj)
    result["X"] = data_type_parser.parse_int(fileobj)
    result["Y"] = data_type_parser.parse_int(fileobj)
    result["Z"] = data_type_parser.parse_int(fileobj)
    result["Count"] = data_type_parser.parse_short(fileobj)
    return result


def parse_entity_velocity(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(10)


def parse_destroy_entity(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    entity_count = data_type_parser.parse_byte(fileobj)
    for i in range(entity_count):
        fileobj.read(4)


def parse_entity(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(4)


def parse_entity_relative_move(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(7)


def parse_entity_look(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(6)


def parse_entity_look_and_relative_move(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(9)


def parse_entity_teleport(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(18)


def parse_entity_head_look(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(5)


def parse_entity_status(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(5)


def parse_attach_entity(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(8)


def parse_entity_effect(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(8)


def parse_remove_entity_effect(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(5)


def parse_set_experience(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(8)


def parse_chunk_data(fileobj, socket):
    fileobj.read(13)
    size = data_type_parser.parse_int(fileobj)
    fileobj.read(size)

def parse_change_game_state(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(2)

def parse_player_list_item(fileobj, socket):
    result = {}
    result["PlayerName"] = mc_datatype.readString(fileobj)
    result["Online"] = mc_datatype.readBoolean(fileobj)
    result["Ping"] = data_type_parser.parse_short(fileobj)
    return result

def parse_player_abilities(fileobj, socket):
    # Not fully implemented. Just getting the appropriate data.
    data = fileobj.read(3)
