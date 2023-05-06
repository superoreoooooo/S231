import asyncio
import projectN_SkinViewer

def showSkin(Nickname) :
    try :
        asyncio.run(projectN_SkinViewer.main(Nickname))
    except :
        print("ERROR!")