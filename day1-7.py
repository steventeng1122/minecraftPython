# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:10:23 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

X,Y,Z=mc.player.getTilePos()
mc.setBlock(X,Y-1,Z,46)