import os
import discord
import app_util


intents = discord.Intents.default()
intents.members = True


class MyBot(app_util.Bot):
    def __init__(self):
        super().__init__(command_prefix='-', intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        await self.change_presence(activity=discord.Game(name='embed builder'))


bot = MyBot()
bot.load_extension('src.em')
bot.load_extension('src.help')
bot.load_extension('src.ping')
bot.run(os.getenv('DISCORD_TOKEN'))
