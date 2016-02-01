#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block
import math


def setup_ground (mc, bid):
    size = 64
    pos = mc.player.getPos()
    mc.setBlocks(pos.x-100,-100,pos.z-100,pos.x+100,-1,pos.z+100,block.GRASS)
    mc.setBlocks(pos.x-100,0,pos.z-100,pos.x+100,1000,pos.z+100,block.AIR.id)


def make (mc,bid):
    pos = mc.player.getPos()
    mc.setBlocks(pos.x,0,pos.z,pos.x+12,4,pos.z,43)
    mc.setBlocks(pos.x,0,pos.z,pos.x,4,pos.z+14,43)
    mc.setBlocks(pos.x+12,0,pos.z,pos.x+12,4,pos.z+14,43)
    mc.setBlocks(pos.x,0,pos.z+14,pos.x+12,4,pos.z+14,43)
    mc.setBlocks(pos.x-1,4,pos.z-1,pos.x+13,4,pos.z+15,44)
    mc.setBlocks(pos.x+1,1,pos.z,pos.x+2,2,pos.z,102)
    mc.setBlocks(pos.x,1,pos.z+1,pos.x,2,pos.z+2,102)
    mc.setBlocks(pos.x,1,pos.z+3,pos.x,2,pos.z+4,102)
    mc.setBlocks(pos.x,1,pos.z+10,pos.x,2,pos.z+10,102)

mc = minecraft.Minecraft.create()
mc.postToChat("Start: daigaku")


setup_ground(mc, block.BRICK_BLOCK.id)
make(mc, block.BRICK_BLOCK.id)
mc.postToChat("End: daigaku")
print "End"
