#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:07:02 2020

@author: sheyda
"""
from playsound import playsound
from time import sleep
from termcolor import colored 
import random


def pause():
    statusSleep = random.randint(0,10)
    if statusSleep == 0:
        sleep(0.5)
    elif statusSleep == 1:
        sleep(1)

s = input("Please Enter the path of your file: ")
file = open(s, "r")
c=[ch for ch in file.read()]
for char in c:
    
    pause()
    if char=='a':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    if char=='b':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/14.mp3')
    if char=='c':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    if char=='d':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/15.mp3')
    if char=='e':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/16.mp3')
    if char=='f':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/18.mp3')
    if char=='g':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/13.mp3')
    if char=='h':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/21.mp3')
    if char=='i':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/23.mp3')
    if char=='j':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='k':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    if char=='l':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='m':
        print(char)
        playsound('./sounds/piano/27.mp3')
    if char=='n':
        print(char)
        playsound('./sounds/piano/28.mp3')
    if char=='o':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    if char=='p':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/23.mp3')
    if char=='q':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/24.mp3')
    if char=='s':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    if char=='t':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/24.mp3')
    if char=='r':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    if char=='u':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='v':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='w':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    if char=='x':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='y':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='z':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    if char=='*':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='#':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    if char=='!':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=='"':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    if char=='/':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    if char=='-':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    if char=='8':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/21.mp3')
    if char=='@':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/24.mp3')
    if char=='*':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    if char=='$':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    if char=="(":
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char==')':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char==':':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    
    elif char=='A':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char=='B':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    elif char=='C':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/25.mp3')
    elif char=='D':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    elif char=='E':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/24.mp3')
    elif char=='F':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/25.mp3')
    elif char=='G':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    elif char=='H':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    elif char=='I':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    elif char=='J':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char=='K':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    elif char=='L':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char=='M':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    elif char=='N':
        text = colored(char, 'yellow', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char=='O':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/29.mp3')
    elif char=='P':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    elif char=='Q':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char=='R':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/25.mp3')
    elif char=='S':
        text = colored(char, 'magenta', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    elif char=='T':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/23.mp3')
    elif char=='U':
        text = colored(char, 'cyan', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/24.mp3')
    elif char=='V':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/28.mp3')
    elif char=='W':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/27.mp3')
    elif char=='X':
        text = colored(char, 'green', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/22.mp3')
    elif char=='Y':
        text = colored(char, 'blue', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/26.mp3')
    elif char=='Z':
        text = colored(char, 'red', attrs=['reverse', 'blink'])
        print(text)
        playsound('./sounds/piano/19.mp3')

