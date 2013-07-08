import minelib

ping_data = minelib.custom_client() \
    .get_serverlist_ping("ufg.me", 25565)

print ping_data
