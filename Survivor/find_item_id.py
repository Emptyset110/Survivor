from Survivor import Player
import time

user = Player()
user.login(username = "benediction", password = "A prayer that asks for God's blessing")

for i in range(340000, 360000):
    user.mystery_box( item_id = i )
    time.sleep(0.5)
