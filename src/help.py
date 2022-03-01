import discord
import app_util


class Emo:
    FAQ = '<:Faq:862729604666228738>'
    SUP = '<:Support:862728959254855711>'
    SETUP = '<:setup:936619226259652760>'



class Help(app_util.Cog):
    def __init__(self, bot: app_util.Bot):
        self.bot = bot

    @extslash.Cog.command(
        command=extslash.SlashCommand(
            name='help',
            description='insights about the commands'
        )
    )
    async def command(self, ctx: extslash.ApplicationContext):
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
                        f'\n> `8` **author_url**: The hyperlink url of the author name'
                        f'\n> `9` **footer_text**: The footer text of the embed'
                        f'\n> `10` **footer_icon**: The footer icon of the embed'
                        f'\n> `11` **link_button**: Send a hyperlink button with the embed'
                        f'\n> `12` For making new line in the description use **`$/`**'
                        f'\n> `13` This embeds support basic text formatting'
                        f'\n> To know more formatting styles visit **[here]'
                        f'(https://support.discord.com/hc/'
                        f'en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-)**'
                        f'\n> {Emo.SUP} Having issues? Join **[Dev & Support](https://discord.gg/VE5qRFfmG2)**',
            color=0x005aef)
        await ctx.send_response(embed=emd)


def setup(bot: app_util.Bot):
    bot.add_application_cog(Help(bot))
