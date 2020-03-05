#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 19:07:02 2020

@author: sheyda
"""
s=input("please insert your file ")
file=open(s,"r")
c=[ch for ch in file.read()]
for char in c:
    print(char)