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
import sys
import argparse
import string
from pathlib import Path
#----------------------------------------------------------------
parser = argparse.ArgumentParser(prog="piano",
                                 description="A Collection of Piano Notes That Make A Pleasant Sound"
                                 )
parser.add_argument("--info",
                    help="show some information about the program",
                    action="store_true"
                    )
parser.add_argument("--file", "-f",
                    help="input text file",
                    type=str
                    )
parser.add_argument("--interactive", "-i",
                    help="provide a string instead of a file",
                    type=str)
args = parser.parse_args()

if args.info:
    print("The World of Sound\n"
          "A Collection of Piano Notes That Make A Pleasant Sound\n"
          "Developers: Sheyda Masoudi & Kia Hamedi\n"
          "Email: ubuntuic6449@gmail.com\n"
          "Github Address: https://github.com/sheyda1997/The-world-of-sound.git\n"
          )
    sys.exit(0)

if args.file:
    s = args.file
    file = open(s, "r")
    c = [ch for ch in file.read()]
elif args.interactive:
    c = [ch for ch in args.interactive]
else:
    s = input("Please enter the path of your file>>> ")
    file = open(s, "r")
    c = [ch for ch in file.read()]
    home=str(Path.home())
#------------------------------------------------------------------

def pause():
    statusSleep = random.randint(0,10)
    if statusSleep == 0:
        sleep(0.5)
    elif statusSleep == 1:
        sleep(1)
#------------------------------------------------------------------


for char in c:

    pause()
    
    
    if char.isupper() == True:
        char=char.lower()
    
    if char =='\n':
        continue
    
    alph=list(string.ascii_lowercase)
    otherchar=('#' ,  '*',  '!',    '&',   ')',  '(',   '/'  , '-' , '}' , '{' ,'%' , '$' , '0' ,'1','2','3','4','5','6','7',' 8','9', ' '  ' ')
    alph.extend(otherchar)
    sound=['27','26','25','26','28','27','26','25','26','28','27','26','25','26','28','27','26','25','26','28',
             '27','26','25','26','28','27','26','25','26','28',
             '27','26','25','26','28','27','26','25','26','28',
             '27','26','25','26','28','27','26','25','26','28']
    index_of_char= alph.index(f'{char}')
    sounds=sound[index_of_char]
    text = colored(char, 'cyan', attrs=['reverse', 'blink'])
    print(text)
    playsound(f'{home}/piano/{sounds}.mp3')

 