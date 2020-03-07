#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:07:02 2020

@author: sheyda
"""
from playsound import playsound
from time import sleep
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
        playsound('./sounds/piano/29.mp3')
    if char=='b':
        playsound('./sounds/piano/14.mp3')
    if char=='c':
        playsound('./sounds/piano/29.mp3')
    if char=='d':
        playsound('./sounds/piano/15.mp3')
    if char=='e':
        playsound('./sounds/piano/16.mp3')
    if char=='f':
        playsound('./sounds/piano/18.mp3')
    if char=='g':
        playsound('./sounds/piano/13.mp3')
    if char=='h':
        playsound('./sounds/piano/21.mp3')
    if char=='i':
        playsound('./sounds/piano/23.mp3')
    if char=='j':
        playsound('./sounds/piano/28.mp3')
    if char=='k':
        playsound('./sounds/piano/29.mp3')
    if char=='l':
        playsound('./sounds/piano/28.mp3')
    if char=='m':
        playsound('./sounds/piano/27.mp3')
    if char=='n':
        playsound('./sounds/piano/28.mp3')
    if char=='o':
        playsound('./sounds/piano/26.mp3')
    if char=='p':
        playsound('./sounds/piano/23.mp3')
    if char=='q':
        playsound('./sounds/piano/24.mp3')
    if char=='s':
        playsound('./sounds/piano/29.mp3')
    if char=='t':
        playsound('./sounds/piano/24.mp3')
    if char=='r':
        playsound('./sounds/piano/26.mp3')
    if char=='u':
        playsound('./sounds/piano/28.mp3')
    if char=='v':
        playsound('./sounds/piano/28.mp3')
    if char=='w':
        playsound('./sounds/piano/27.mp3')
    if char=='x':
        playsound('./sounds/piano/28.mp3')
    if char=='y':
        playsound('./sounds/piano/28.mp3')
    if char=='z':
        playsound('./sounds/piano/27.mp3')
    if char=='*':
        playsound('./sounds/piano/28.mp3')
    if char=='#':
        playsound('./sounds/piano/26.mp3')
    if char=='!':
        playsound('./sounds/piano/28.mp3')
    if char=='"':
        playsound('./sounds/piano/29.mp3')
    if char=='/':
        playsound('./sounds/piano/27.mp3')
    if char=='-':
        playsound('./sounds/piano/29.mp3')
    if char=='8':
        playsound('./sounds/piano/21.mp3')
    if char=='@':
        playsound('./sounds/piano/24.mp3')
    if char=='*':
        playsound('./sounds/piano/27.mp3')
    if char=='$':
        playsound('./sounds/piano/28.mp3')
    if char=="(":
        playsound('./sounds/piano/28.mp3')
    elif char==')':
        playsound('./sounds/piano/28.mp3')
    elif char==':':
        playsound('./sounds/piano/28.mp3')
    
    elif char=='A':
        playsound('./sounds/piano/28.mp3')
    elif char=='B':
        playsound('./sounds/piano/26.mp3')
    elif char=='C':
        playsound('./sounds/piano/25.mp3')
    elif char=='D':
        playsound('./sounds/piano/27.mp3')
    elif char=='E':
        playsound('./sounds/piano/24.mp3')
    elif char=='F':
        playsound('./sounds/piano/25.mp3')
    elif char=='G':
        playsound('./sounds/piano/26.mp3')
    elif char=='H':
        playsound('./sounds/piano/29.mp3')
    elif char=='I':
        playsound('./sounds/piano/26.mp3')
    elif char=='J':
        playsound('./sounds/piano/28.mp3')
    elif char=='K':
        playsound('./sounds/piano/29.mp3')
    elif char=='L':
        playsound('./sounds/piano/28.mp3')
    elif char=='M':
        playsound('./sounds/piano/27.mp3')
    elif char=='N':
        playsound('./sounds/piano/28.mp3')
    elif char=='O':
        playsound('./sounds/piano/29.mp3')
    elif char=='P':
        playsound('./sounds/piano/26.mp3')
    elif char=='Q':
        playsound('./sounds/piano/28.mp3')
    elif char=='R':
        playsound('./sounds/piano/25.mp3')
    elif char=='S':
        playsound('./sounds/piano/27.mp3')
    elif char=='T':
        playsound('./sounds/piano/23.mp3')
    elif char=='U':
        playsound('./sounds/piano/24.mp3')
    elif char=='V':
        playsound('./sounds/piano/28.mp3')
    elif char=='W':
        playsound('./sounds/piano/27.mp3')
    elif char=='X':
        playsound('./sounds/piano/22.mp3')
    elif char=='Y':
        playsound('./sounds/piano/26.mp3')
    elif char=='Z':
        playsound('./sounds/piano/19.mp3')

