import minelib

client=minelib.custom_client("GKBRK")
client.do_server_login("localhost")
import time
time.sleep(5)
client.disconnect()
