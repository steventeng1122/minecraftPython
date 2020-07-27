# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:11:11 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x=345.5
y=118.1
z=-27.6
mc.player.setPos(x,y,z)