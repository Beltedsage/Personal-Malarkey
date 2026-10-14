import keyboard
import time
import math

INTERVAL = 0.2  # seconds between registered presses
last_time = {}

count = 0

map = {}

mapSize = 10

for r in range(mapSize):
    map[r] = ("X"*mapSize)
    
playerPos = [math.ceil(mapSize/2), math.ceil(mapSize/2)]

# playerPos = [mapSize/2, mapSize/2]

def on_press(event):
    global count
    # print(event)
    now = time.monotonic() # generally time since last system boot - good for avoiding DST
    if now - last_time.get(event.name, 0) < INTERVAL: # if it has been longer than the interval since the lat button press
        return
    last_time[event.name] = now
    count += 1
    print(f"{event.name} pressed")
    print(count)
    
    if event.name == "w":
        playerPos[0] += 1
        print(playerPos)
    if event.name == "s":
            playerPos[0] -= 1
            print(playerPos)
    if event.name == "a":
            playerPos[1] += 1
            print(playerPos)
    if event.name == "d":
            playerPos[1] -= 1
            print(playerPos)
    
    
for row in map:
    print(map[row])

# print(map)
    

keyboard.on_press(on_press)
keyboard.wait("esc")

print("HELLO")