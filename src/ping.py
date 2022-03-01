import discord
import app_util



class Ping(extslash.Cog):
    def __init__(self, bot: app_util.Bot):
        self.bot = bot

    @extslash.Cog.command(
        command=app_util.SlashCommand(name='ping', description='shows avg ping of client'),
        guild_id=877399405056102431
    )
    async def command(self, ctx: app_util.Context):
        await ctx.send_response(embed=discord.Embed(title='Pong!', description=f'{self.bot.latency * 1000:.2f}ms'))


def setup(bot: app_util.Bot):
    bot.add_application_cog(Ping(bot))
