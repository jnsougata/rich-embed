import discord
import extslash



class Ping(extslash.Cog):
    def __init__(self, bot: extslash.Bot):
        self.bot = bot

    @extslash.Cog.command(
        command=extslash.SlashCommand(name='ping', description='shows avg ping of client'),
        guild_id=877399405056102431
    )
    async def command(self, ctx: extslash.ApplicationContext):
        await ctx.send_response(embed=discord.Embed(title='Pong!', description=f'{self.bot.latency * 1000:.2f}ms'))


def setup(bot: extslash.Bot):
    bot.add_slash_cog(Ping(bot))
