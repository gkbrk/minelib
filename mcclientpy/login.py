import minelib

client=minelib.cracked_client("GKBRK")
connection=client.connect_to_server("localhost",25565)
client.packet_handshake(connection)
client.packet_client_statuses(connection,0)
client.packet_chat_message(connection,"Hello MineLib!")