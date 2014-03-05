#python
#Autor: Bernd Möller

#create outputs for comp stack

import traceback
import bm_ROM_funcs as funcs

try:
    saveSel = funcs.saveSel()
    romID = funcs.ccGroup('ROM')
    romCompID = funcs.ccGroup('ROMutils')
    lx.eval('select.item %s set'%romCompID)
    lx.eval('texture.parent %s -1'%romID)
    ROs = ('shade.normal','depth','occl.ambient')
    for output in ROs:
        if not funcs.checkRoInGroup(romCompID, output):
            funcs.createRoInGroup(romCompID, output)
    
    funcs.restoreSel(saveSel)
except:
    lx.out(traceback.format_exc())