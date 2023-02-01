import asyncio
import steam
import aiohttp
from io import BytesIO

class MyClient(steam.Client):
    async def on_ready(self) -> None:
        print("user", self.user)
        while True:
            await self.user.edit(avatar=await self._get_cat())
            print("updated")
            await asyncio.sleep(60)
    
    async def _get_cat(self) -> steam.Image:
        async with aiohttp.ClientSession() as sess:
            async with sess.get("https://thiscatdoesnotexist.com/") as resp:
                data = await resp.content.read()
                return steam.Image(BytesIO(data))


client = MyClient()
client.run("login", "password")