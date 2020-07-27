# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:59:22 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()


print(mc.player.getTilePos())
