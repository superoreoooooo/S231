import asyncio
from minepi import Player

async def main(skinName):
    p = Player(name=skinName)
    await p.initialize()

    await p.skin.render_skin(hr=30, vr=-30, display_cape=True, display_second_layer=True, aa=True)
    p.skin.skin.show()

#asyncio.run(main())