import os
import discord
from extslash import commands


intents = discord.Intents.default()
intents.members = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='-', intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = MyBot()
bot.load_extension('src.embed')
bot.load_extension('src.help')
bot.load_extension('src.ping')
bot.run(os.getenv('DISCORD_TOKEN'))
