#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:07:02 2020

@author: sheyda
"""
from playsound import playsound
import time
import random
s=input("Please Enter the path of your file ")
file=open(s,"r")
c=[ch for ch in file.read()]
for char in c:
    time.sleep(random.randint(1,1))
    if char=='a':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/28.mp3')
    if char=='b':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/26.mp3')
    if char=='c':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/25.mp3')
    if char=='d':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/27.mp3')
    if char=='e':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/24.mp3')
    if char=='f':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/25.mp3')
    if char=='g':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/26.mp3')
    if char=='h':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/29.mp3')
    if char=='i':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/26.mp3')
    if char=='j':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/28.mp3')
    if char=='k':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/29.mp3')
    if char=='l':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/28.mp3')
    if char=='m':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/27.mp3')
    if char=='n':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/28.mp3')
    if char=='o':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/29.mp3')
    if char=='p':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/26.mp3')
    if char=='q':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/28.mp3')
    if char=='r':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/25.mp3')
    if char=='s':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/27.mp3')
    if char=='t':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/23.mp3')
    if char=='u':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/24.mp3')
    if char=='v':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/28.mp3')
    if char=='w':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/27.mp3')
    if char=='x':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/22.mp3')
    if char=='y':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/26.mp3')
    if char=='z':
        playsound('/home/sheyda/The-world-of-sound/sounds/piano/19.mp3')