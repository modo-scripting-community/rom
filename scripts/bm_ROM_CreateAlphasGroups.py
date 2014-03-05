#python
#Autor: Bernd Möller

#create alpha outputs for selected masks

import traceback
import bm_ROM_funcs as funcs

try:
    selMasks = lx.evalN('query sceneservice selection ? mask')
    saveSel = funcs.saveSel()
    funcs.ccGroup('ROM')
    for mask in selMasks:
        #create mask in ROM group
        maskInRom = funcs.checkMaskInRom(mask)
        if not (maskInRom):
            maskInRom = funcs.createMaskInRom(mask)
        alphaInGroup = funcs.checkRoInGroup(maskInRom, 'shade.alpha')
        if not (alphaInGroup):
            funcs.createRoInGroup(maskInRom, 'shade.alpha')
    funcs.restoreSel(saveSel)
except:
    lx.out(traceback.format_exc())