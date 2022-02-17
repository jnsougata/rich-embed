import sys
import traceback
import discord
import extslash


class Emo:
    FAQ = '<:Faq:862729604666228738>'
    SUP = '<:Support:862728959254855711>'
    SETUP = '<:setup:936619226259652760>'



class Help(extslash.Cog):
    def __init__(self, bot: extslash.Bot):
        self.bot = bot

    @extslash.Cog.command(command=extslash.SlashCommand(name='help', description='insights about the commands'))
    async def command(self, ctx: extslash.ApplicationContext):
        await ctx.defer()
        emd = discord.Embed(
            description=f'\n\n{Emo.SETUP} Create & send embeds using **`/embed`**'
                        f'\n\n{Emo.FAQ} **FAQs**'
                        f'\n\n> `1` **title**: The title of the embed'
                        f'\n> `2` **description**: The description of the embed'
                        f'\n> `3` **color**: The color of the embed'
                        f'\n> `4` **url**: The hyperlink url of the title'
                        f'\n> `5` **thumbnail**: The image file of thumbnail'
                        f'\n> `6` **image**: The image file to attach with embed'
                        f'\n> `7` **author**: The author of the embed'
                        f'\n> `8` **footer**: The footer text of the embed'
                        f'\n> `9` For making new line in the description use **`$/`**'
                        f'\n> `10` This embeds support basic text formatting '
                        f'\n> To know more formatting styles visit **[here]'
                        f'(https://support.discord.com/hc/'
                        f'en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-)**'
                        f'\n> {Emo.SUP} Having issues? Join **[Dev & Support](https://discord.gg/VE5qRFfmG2)**',
            color=0x005aef)
        await ctx.send_followup(embed=emd)


def setup(bot: extslash.Bot):
    bot.add_slash_cog(Help(bot))
