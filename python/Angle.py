# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:09:55 2020

@author: rafae
"""

def getAngle(Top, Left, Right):
    a=math.sqrt((Top[1]-Left[0])**2 +(Left[1]-Top[0])**2)
    c=math.sqrt((Left[1]-Right[0])**2 +(Right[1]-Left[0])**2)
    b=math.sqrt((Top[1]-Right[0])**2 +(Right[1]-Top[0])**2)
    return math.degrees(math.acos((c**2 - b**2 - a**2)/(-2.0 * a * b)))



print(getAngle((3,2),(0,0),(4,0)))

