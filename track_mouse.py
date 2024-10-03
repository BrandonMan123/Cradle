from ahk import AHK
import time
import keyboard
import json
ahk = AHK()
x, y = 1920, 1080

res = []
tmp = []
is_recording = True
coord_formed = False
while is_recording:
    pos = ahk.get_mouse_position()
    time.sleep(0.2)
    pos_x = pos.x
    pos_y = pos.y
    res_x = round(pos_x / x, 3)
    res_y = round(pos_y / y, 3)
    print(f"x: {res_x}, y: {res_y}")
    print(f"x abs: {pos_x}, y abs: {pos_y}\n" )
    if keyboard.is_pressed('a'):
        print ("saved value")
        tmp.extend([pos_x, pos_y])
        if not coord_formed:
            coord_formed = True
        else:
            x1, y1, x2, y2 = tmp
            to_append = {"top": x1, "left": y1, "width": x2-x1, "height": y2-y1}
            res.append(to_append)
            tmp = []
            coord_formed = False
    if keyboard.is_pressed('s'):
        break
with open("test.json", "w") as f:
    json.dump(res, f)
    # print(ahk.get_mouse_position())