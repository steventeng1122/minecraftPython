# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:33:01 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time



mc.player.setTilePos(x,y,z)
time.sleep(2)
x=x+10
x,y,z=mc.player.getTilePos()
mc.player.setTilePos(x,y,z)   
time.sleep(2)
x=x+10
mc.player.setTilePos(x,y,z) 
y=y+50
time.sleep(2)
y=y+50
mc.player.setTilePos(x,y,z)
time.sleep(2)
y=y+50
mc.player.setTilePos(x,y,z)
