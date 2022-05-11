import pyautogui 
from PIL import Image, ImageGrab
import time
import keyboard

#creating press function to press key
def press(key):
    pyautogui.keyDown(key)

#creating iscollide function
def iscollide(data):
#logic for cactus
    for a in range(335, 397):
        for b in range(376, 455):
            if data[a,b] > 100:
                press("up")
                return
#logic for bird   
    for i in range(335,397):
        for j in range(323,366):
            if data[i,j] > 100:
                press("down")
                return
    return
    

if __name__ == "__main__":
    print('Game will start in 3 seconds')
    time.sleep(3)
    press("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        iscollide(data)
 """It is not complete yet very basic code, it will only work in day mode of dino game"""

