#!/usr/bin/env python

import random
import time

import pyautogui
from AppKit import NSWorkspace


def main():
    print(
        "Loaded... watching for WoW window and sending kess presses when wow window active"
    )
    wowTitle = "Wow"
    starttime = time.time()
    keys = ['w', 'a', 's', 'd', 'space']
    while True:
        current_window = NSWorkspace.sharedWorkspace().activeApplication()[
            'NSApplicationName'
        ]
        print(f'Current window is {current_window}')
        key = random.randint(0, len(keys) - 1)
        if current_window == wowTitle:
            print("Current window is WoW... pressing key: " + keys[key])
            pyautogui.press(keys[key])
        interval = random.randint(1, 30)
        time.sleep(interval - ((time.time() - starttime) % interval))


if __name__ == "__main__":
    main()
