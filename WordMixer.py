# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 03:01:00 2017

@author: Tim
"""
import random
import time
    
def mix():
    ms_file = open("MillenialSoup.csv", "r")
    ms_str = ms_file.read()
    ms_file.close()
    ms_list = ms_str.split(',')
    random.shuffle(ms_list)
    ms_str=','.join(ms_list)
    ms_str=ms_str.replace('..','.')
    ms_list = ms_str.split(',')
    
    outputForever(ms_list)
    
def outputForever(nonsense):

    for x in range(0,50):
        s = str(random.choice(nonsense))
        print(s, sep='')
        time.sleep(0.2)
        
def readFile():
    f = open("MillenialSoup.txt", "r")
    print("FILE CONTENTS -->")
    print(f.read())
    f.close()
    
mix()


    