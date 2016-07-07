from Survivor import Player
import time

user = Player()
user.login(username = "emptyset110", password = "emptyset110.")

for i in range(300000, 320000):
    user.mystery_box( item_id = i )
    time.sleep(1)
