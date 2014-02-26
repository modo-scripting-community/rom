#python
#Autor: Bernd Möller

#browse ROM render path

err = False
try:
    lx.eval("dialog.setup dir")
    lx.eval("dialog.title \"Select renders file folder...\"")
    lx.eval("dialog.open")
    dir = lx.eval("dialog.result ?")
    lx.eval('user.value bm_ROMFilePath {%s}' % dir)
except:
    err = True