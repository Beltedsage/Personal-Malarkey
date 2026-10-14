import keyboard
import math

pressed = set()
count = 0

map = []
mapSize = 10

for r in range(mapSize):
    # row = "X"*mapSize
    # print(row, type(row))
    # # map += ("X" * mapSize)
    # map += row
    
    row = "X" * mapSize
    map += (row)

playerPos = [math.ceil(mapSize / 2), math.ceil(mapSize / 2)]

oldPlayerPos = playerPos


def on_key(event):
    global count
    
    # oldPlayerPos = playerPos


    if event.event_type == keyboard.KEY_UP:
        pressed.discard(event.name)
        return

    if event.name in pressed:
        return  # held, ignore the repeat
    pressed.add(event.name)

    count += 1
    print(f"{event.name} pressed")
    print(count)

    if event.name == "w":
        playerPos[0] += 1
    elif event.name == "s":
        playerPos[0] -= 1
    elif event.name == "a":
        playerPos[1] += 1
    elif event.name == "d":
        playerPos[1] -= 1
    else:
        return

    print(playerPos)
    
    print(map[playerPos[0]][playerPos[1]])
    
    map[playerPos[0]][playerPos[1]] = "M"
    
    # map[int(playerPos[0]), int(playerPos[1])] = "M"
    # map(oldPlayerPos = "X")
    
print(map)

# for r in range(mapSize):
#     for i in range(mapSize):
        

for item in map:
    for item2 in item:
        print(item2, end="")
    # print()
    



keyboard.hook(on_key)
keyboard.wait("esc")