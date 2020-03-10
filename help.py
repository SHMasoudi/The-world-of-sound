#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:17:23 2020

@author: sheyda
"""
import sys
try:
    option=sys.argv[1]
except IndexError:
    import piano
else:
    if option=="-h" or option=="--help":
        print("Help")
    else:
        print("invalid option")
        sys.exit(1)
