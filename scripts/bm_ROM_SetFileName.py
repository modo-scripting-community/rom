#python
#Autor: Bernd Möller

#set filename for all render outputs based on ROM user value
outputPattern = lx.eval('user.value bm_ROMOutputPattern ?')
polyRender = lx.eval('query sceneservice polyRender.id ? first')
lx.eval('select.item %s' %polyRender)
lx.eval('item.channel outPat "%s"'%outputPattern)

numRos = lx.eval1('query sceneservice renderOutput.N ?')
roPath = lx.eval('user.value bm_ROMFilePath ?')
roFormat = lx.eval('user.value CmdMyPopUpCommand_val ?')
for i in range(0,numRos):
    roId = lx.eval('query sceneservice renderOutput.ID ? %s' % i)
    lx.eval('select.item %s'%roId)
    lx.eval('item.channel renderOutput$filename "%s"' %roPath )
    lx.eval('item.channel renderOutput$format "%s"' %roFormat )

