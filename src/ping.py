import sys
import traceback
import discord
import extslash
from extslash.commands import Bot, SlashCog, ApplicationContext



class Ping(SlashCog):
    def __init__(self, bot: Bot):
        self.bot = bot

    def register(self):
        return extslash.SlashCommand(name='ping', description='shows avg ping of client',)

    async def command(self, ctx: ApplicationContext):
        await ctx.send_response(embed=discord.Embed(title='Pong!', description=f'{self.bot.latency * 1000:.2f}ms'))


    async def on_error(self, ctx: ApplicationContext, error: Exception):
        stack = traceback.format_exception(type(error), error, error.__traceback__)
        print(''.join(stack), file=sys.stderr)
        await ctx.send_response(f'Something went wrong! Please try again...', ephemeral=True)


def setup(bot: Bot):
    bot.add_slash_cog(Ping(bot), 877399405056102431)
