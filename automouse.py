import threading
import time
import pyautogui
import keyboard
import random

class MouseMoveThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
    
    def run(self):
        x_range = (0, pyautogui.size().width)
        y_range = (0, pyautogui.size().height)
        pyautogui.FAILSAFE = False

        while not self.stop_event.is_set():
            c_x, c_y = pyautogui.position()
            x = random.randint(*x_range)
            y = random.randint(*y_range)

            pyautogui.moveRel(x - c_x, y - c_y, random.randint(1, 3))
    
    def stop(self):
        self.stop_event.set()

class StopMouseThread(threading.Thread):
    def __init__(self, move_thread):
        threading.Thread.__init__(self)
        self.move_thread = move_thread
    
    def run(self):
        keyboard.wait('esc')
        self.move_thread.stop()

if __name__ == '__main__':
    move_thread = MouseMoveThread()
    stop_thread = StopMouseThread(move_thread)
    move_thread.start()
    stop_thread.start()
    
    move_thread.join()
    stop_thread.join()
