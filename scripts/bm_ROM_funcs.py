#python
#Autor: Bernd Möller
import lx

# !!! Thanks to Farfarer for the next two functions !!!
# saves the current selection
def saveSel():
    myPrevSelected = []
    n = lx.eval( "query sceneservice txLayer.N ?" ) # Using all here is meaningless, as far as I know.
    for i in xrange(n): # xrange is faster for large numbers, and you don't have to specify a lower bound of 0 for range either - it will default to 0.
        if lx.eval1("query sceneservice txLayer.isSelected ? %s" % i):
            myID = lx.eval1("query sceneservice txLayer.id ? %s" % i)
            myPrevSelected.append (myID)        # Store the ID here, as the index may not point to the same thing if you've made changes.
            lx.eval("select.subItem %s remove" % myID)
    return myPrevSelected

#restores selection based on a list
def restoreSel(myPrevSelected):
    lx.eval('select.drop item')
    for id in myPrevSelected:
        # Changed this to "add" as "set" will replace the current selection with this thing alone.
        lx.eval("select.subItem %s add" % id)

#check if there is a group in the ST named "ROM"
def ccRomGroup ():
    try:
        romID = lx.eval('query sceneservice item.ID ? {ROM}')
    except:
        lx.eval('select.drop item')
        lx.eval('shader.create mask')
        renderID = lx.eval('query sceneservice polyRender.ID ? 0')
        lx.eval('texture.parent %s -1'%renderID)
        lx.eval('item.name ROM')
        lx.eval('item.editorColor green')
        romID = lx.eval('query sceneservice selection ? mask')
        lx.out('--- ROM mask created! ---')

#check if mask in ROM group exists
def checkMaskInRom (maskID):
    romMaskExists = None
    romChildrenAll = lx.evalN('query sceneservice mask.children ? {ROM}')
    romChildren = []
    for child in romChildrenAll:
        if(lx.eval('query sceneservice item.type ? {%s}' % child) == 'mask'):
            romChildren.append(child)
    lx.eval('select.item %s set'%maskID)
    maskItemSel = lx.eval('mask.setMesh ?')
    if(maskItemSel == '(all)'):
        for romChild in romChildren:
            lx.out('---')
            lx.eval('select.item %s'%romChild)
            romChildSel = lx.eval('mask.setMesh ?')
            if(romChildSel == '(all)'):
                romChildName = lx.eval('item.name ?')
                lx.out(romChildName.split(' ')[0])
                lx.eval('select.item %s'%maskID)
                maskName = lx.eval('item.name ?')
                lx.out(maskName.split(' ')[0])
                if (romChildName.split(' ')[0] == maskName.split(' ')[0]):
                    romMaskExists = romChild
    else:
        for romChild in romChildren:
            lx.out('---')
            lx.eval('select.item %s'%romChild)
            romChildSel = lx.eval('mask.setMesh ?')
            if(romChildSel == maskItemSel):
                lx.out(romChildSel)
                lx.out(maskItemSel)
                romMaskExists = romChild
    return romMaskExists

#create a mask in ROM group
def createMaskInRom(maskID):
    lx.out('blubb')
    romID = lx.eval('query sceneservice item.ID ? {ROM}')
    lx.eval('select.item %s set'%maskID)
    maskName = lx.eval('item.name ?')
    maskMesh = lx.eval('mask.setMesh ?')
    maskPTagType = lx.eval('mask.setPTagType ?')
    maskPTag = lx.eval('mask.setPTag ?')
    lx.eval('select.drop item')
    lx.eval('shader.create mask')
    lx.eval('texture.parent %s -1'%romID)
    lx.eval('item.name {%s}'%maskName)
    lx.eval('item.editorColor white')
    lx.eval('mask.setMesh {%s}'%maskMesh)
    lx.eval('mask.setPTagType {%s}'%maskPTagType)
    lx.eval('mask.setPTag {%s}'%maskPTag)
    maskOutID = lx.eval('query sceneservice selection ? mask')
    lx.out('--- ROM mask created! ---')
    return maskOutID


#check if render output of specific type is in mask
def checkRoInGroup(maskID, roType):
    roExists = None
    grpChildrenAll = lx.evalN('query sceneservice mask.children ? %s'%maskID)
    grpChildren = []
    for grpChild in grpChildrenAll:
        if(lx.eval('query sceneservice item.type ? {%s}'%grpChild) == 'renderOutput'):
            lx.eval('select.item %s set'%grpChild)
            roEffect = lx.eval('shader.setEffect ?')
            if (roEffect == roType):
                roExists = grpChild
    return roExists

#create a renderoutput and color it in the ST
editorColors = { 'shade.alpha' : 'white' }
def createRoInGroup(maskID, roType):
    lx.eval('select.item %s'%maskID)
    maskName = lx.eval('item.name ?')
    maskName = maskName.split(' ')[0]#.translate(None, '() <>äöüß')
    lx.out(maskName)
    lx.eval('shader.create renderOutput')
    lx.eval('shader.setEffect {%s}'%roType)
    alphaName = maskName + '_Alpha'
    lx.eval('item.name %s'%alphaName)

    lx.out(roType)
    lx.out(editorColors[roType])
    lx.eval('item.editorColor %s'%editorColors[roType])

    

    
    
    
    
    
    
    
    
    
    