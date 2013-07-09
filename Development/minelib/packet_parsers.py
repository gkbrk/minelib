"""This file is used to parse the packets returned by the server."""

import data_type_parser
import mc_datatype
import packet_generators
import pynbt
import io
import cStringIO


def makeio(string):
    return cStringIO.StringIO(string)


def parse_keepalive(fileobj, socket):
    keepalive_id = mc_datatype.readInt(fileobj)
    print "Got keepalive. Responding"
    socket.send("\x00")
    mc_datatype.sendInt(socket,keepalive_id)
    return "Keepalive"


def parse_login_request(fileobj, socket):
    result = {}
    result['EntityID'] = mc_datatype.readInt(fileobj)
    result['LevelType'] = mc_datatype.readString(fileobj)
    result["GameMode"] = mc_datatype.readByte(fileobj)
    result["Dimension"] = mc_datatype.readByte(fileobj)
    result["Difficulty"] = mc_datatype.readByte(fileobj)
    result["NotUsed"] = mc_datatype.readByte(fileobj)
    result["MaxPlayers"] = mc_datatype.readByte(fileobj)
    return result


def parse_spawn_position(fileobj, socket):
    result = {}
    result["X"] = data_type_parser.parse_int(fileobj)
    result["Y"] = data_type_parser.parse_int(fileobj)
    result["Z"] = data_type_parser.parse_int(fileobj)
    return result


def parse_chat_message(fileobj, socket):
    chat_message = mc_datatype.readString(fileobj)
    return {"ChatMessage":chat_message}


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
    result["Difficulty"] = mc_datatype.readByte(fileobj)
    result["GameMode"] = mc_datatype.readByte(fileobj)
    result["WorldHeight"] = data_type_parser.parse_short(fileobj)
    result["LevelType"] = mc_datatype.readString(fileobj)
    return result


def parse_player_pos_and_look(fileobj, socket):
    # Not fully implemented. Just responding with an appropriate packet.
    socket.send("\x0d" + fileobj.read(41))


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

def parse_spawn_object_vehicle(fileobj,socket):
    FileObject=fileobj
    EntityID = mc_datatype.readInt(FileObject)
    Type = mc_datatype.readByte(FileObject)
    x = mc_datatype.readInt(FileObject)
    y = mc_datatype.readInt(FileObject)
    z = mc_datatype.readInt(FileObject)
    yaw = mc_datatype.readByte(FileObject)
    pitch = mc_datatype.readByte(FileObject)
    data = mc_datatype.readInt(FileObject)
    if (data > 0):
        SpeedX = mc_datatype.readShort(FileObject)
        SpeedY = mc_datatype.readShort(FileObject)
        SpeedZ = mc_datatype.readShort(FileObject)
        return {'EntityID': EntityID,
                'Type': Type,
                'x': x,
                'y': y,
                'z': z,
                'yaw': yaw,
                'pitch': pitch,
                'SpeedX': SpeedX,
                'SpeedY': SpeedY,
                'SpeedZ': SpeedZ
        }
    else:
        return {'EntityID': EntityID,
                'Type': Type,
                'x': x,
                'y': y,
                'z': z,
                'yaw': yaw,
                'pitch': pitch
        }

def parse_spawn_mob(fileobj,socket):
    result={}
    result["EntityID"]=mc_datatype.readInt(fileobj)
    result["Type"]=mc_datatype.readByte(fileobj)
    result["X"]=mc_datatype.readInt(fileobj)
    result["Y"]=mc_datatype.readInt(fileobj)
    result["Z"]=mc_datatype.readInt(fileobj)
    result["Pitch"]=mc_datatype.readByte(fileobj)
    result["HeadPitch"]=mc_datatype.readByte(fileobj)
    result["Yaw"]=mc_datatype.readByte(fileobj)
    result["VelocityX"]=mc_datatype.readShort(fileobj)
    result["VelocityY"]=mc_datatype.readShort(fileobj)
    result["VelocityZ"]=mc_datatype.readShort(fileobj)
    result["Metadata"]=mc_datatype.readEntityMetadata(fileobj)
    return result


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
    entity_count = mc_datatype.readByte(fileobj)
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

def parse_entity_metadata(fileobj, socket):
    result={}
    result["EntityID"]=mc_datatype.readInt(fileobj)
    result["EntityMetadata"]=mc_datatype.readEntityMetadata(fileobj)
    return result

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

def parse_block_change(fileobj, socket):
    result={}
    result["X"]=mc_datatype.readInt(fileobj)
    result["Y"]=mc_datatype.readByte(fileobj)
    result["Z"]=mc_datatype.readInt(fileobj)
    result["BlockType"]=mc_datatype.readShort(fileobj)
    result["BlockMetadata"]=mc_datatype.readByte(fileobj)

def parse_map_chunk_bulk(fileobj,socket):
    FileObject=fileobj
    #short - number of chunks
    ChunkCount = mc_datatype.readShort(FileObject)

    #int - chunk data length
    ChunkDataLength = mc_datatype.readInt(FileObject)
    SkyLightSent = mc_datatype.readBoolean(FileObject)
    RawData = FileObject.read(ChunkDataLength)

    metadata = []
    for i in range(ChunkCount):
        ChunkX = mc_datatype.readInt(FileObject)
        ChunkZ = mc_datatype.readInt(FileObject)
        PrimaryBitMap = mc_datatype.readUnsignedShort(FileObject)
        AddBitMap = mc_datatype.readUnsignedShort(FileObject)
        metadata.append({'x': ChunkX,
                         'z': ChunkZ,
                         'PrimaryBitMap': PrimaryBitMap,
                         'AddBitMap': AddBitMap
                         })

    return {'ChunkCount': ChunkCount,
            'SkyLightSent': SkyLightSent,
            'RawData': RawData,
            'ChunkMeta': metadata
    }

def parse_named_sound_effect(fileobj, socket):
    result={}
    result["SoundName"]=mc_datatype.readString(fileobj)
    result["EffectPositionX"]=mc_datatype.readInt(fileobj)
    result["EffectPositionY"]=mc_datatype.readInt(fileobj)
    result["EffectPositionZ"]=mc_datatype.readInt(fileobj)
    result["Volume"]=mc_datatype.readFloat(fileobj)
    result["Pitch"]=mc_datatype.readByte(fileobj)
    return result

def parse_change_game_state(fileobj, socket):
    # Not fully implemented. Just getting the appropriate packet data.
    data = fileobj.read(2)

def parse_set_slot(fileobj,socket):
    result={}
    result["WindowID"]=mc_datatype.readByte(fileobj)
    result["Slot"]=mc_datatype.readShort(fileobj)
    result["SlotData"]=mc_datatype.readSlotData(fileobj)
    return result

def parse_set_window_items(fileobj,socket):
    result={}
    result["WindowID"]=mc_datatype.readByte(fileobj)
    result["Count"]=mc_datatype.readShort(fileobj)
    slots=[]
    for i in range(result["Count"]):
        slotdata=mc_datatype.readSlotData(fileobj)
        slots.append(slotdata)
    result["Slots"]=slots
    return result

def parse_update_tile_entity(fileobj, socket):
    FileObject=fileobj
    X = mc_datatype.readInt(FileObject)
    Y = mc_datatype.readShort(FileObject)
    Z = mc_datatype.readInt(FileObject)
    Action = mc_datatype.readByte(FileObject)
    DataLength = mc_datatype.readShort(FileObject)
    if (DataLength != -1):
        ByteArray = mc_datatype.readByteArray(FileObject, DataLength)
        NBTData = pynbt.NBTFile(io.BytesIO(ByteArray), compression=pynbt.NBTFile.Compression.GZIP)
        return {'x': X,
                'y': Y,
                'z': Z,
                'Action': Action,
                'NBTData': NBTData
        }
    return {'x': X,
            'y': Y,
            'z': Z,
            'Action': Action
    }

def parse_player_list_item(fileobj, socket):
    result = {}
    result["PlayerName"] = mc_datatype.readString(fileobj)
    result["Online"] = mc_datatype.readBoolean(fileobj)
    result["Ping"] = data_type_parser.parse_short(fileobj)
    return result

def parse_player_abilities(fileobj, socket):
    # Not fully implemented. Just getting the appropriate data.
    data = fileobj.read(3)
