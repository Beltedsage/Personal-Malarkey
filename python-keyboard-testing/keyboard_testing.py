import keyboard

# while True:
#     try:
#         if keyboard.is_pressed("q"):
#             print("SUCCESS!")
#             break
#     except:
#         print("You melon.")
#         break

num = 0

while True:
    
    if keyboard.is_pressed("w"):
        num += 1
        print(num)
    elif keyboard.is_pressed("s"):
        num -= 1
        print(num)
        
    