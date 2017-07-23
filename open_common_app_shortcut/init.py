#!/usr/bin/env python
import os


def open_main_app():
    os.startfile("E:\Bin\QQScLauncher.exe")
    os.startfile("F:\Program Files (x86)\\Netease\CloudMusic\cloudmusic.exe")
    os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")


def open_books():
    os.startfile("C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe")

if __name__ == '__main__':
    open_main_app()
    open_books()