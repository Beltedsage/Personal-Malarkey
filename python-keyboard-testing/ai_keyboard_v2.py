import keyboard
import math

pressed = set()
count = 0

map = {}

mapSize = 10

for r in range(mapSize):
    map[r] = ("X"*mapSize)
    
playerPos = [math.ceil(mapSize/2), math.ceil(mapSize/2)]


def on_press(event):
    global count
    if event.name in pressed:
        return  # key is being held, ignore the repeat
    pressed.add(event.name)

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
def on_release(event):
    pressed.discard(event.name)

keyboard.on_press(on_press)
keyboard.on_release(on_release)
keyboard.wait("esc")