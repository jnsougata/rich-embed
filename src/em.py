import sys
import asyncio
import traceback
import discord
import app_util


async def check(ctx: app_util.Context):
    if not ctx.guild:
        await ctx.send_response(f'{ctx.author.mention} please use command `{ctx.name}` inside a guild')
    elif not ctx.author.guild_permissions.administrator:
        await ctx.send_response(f'{ctx.author.mention} you are not an administrator')
    else:
        return True


class Main(app_util.Cog):

    def __init__(self, bot: app_util.Bot):
        self.bot = bot

    @app_util.Cog.listener
    async def on_command_error(self, ctx: app_util.Context, error: Exception):
        stack = traceback.format_exception(type(error), error, error.__traceback__)
        print(''.join(stack), file=sys.stderr)
        if ctx.responded:
            await ctx.send_followup(f'{ctx.author.mention} something went wrong! Please retry after a few seconds...')


    @app_util.Cog.command(
        command=app_util.SlashCommand(
            name='embed',
            description='creates an embed to current channel',
            options=[
                app_util.StrOption('title', 'title of the embed', required=False),
                app_util.StrOption('description', 'description of the embed', required=False),
                app_util.StrOption('url', 'hyperlink url of the title', required=False),
                app_util.StrOption('color', 'color hex of the embed', required=False),
                app_util.UserOption('author', 'author of the embed', required=False),
                app_util.StrOption('author_url', 'hyperlink url of the author', required=False),
                app_util.AttachmentOption('thumbnail', 'image file of thumbnail', required=False),
                app_util.AttachmentOption('image', 'image file to add to embed', required=False),
                app_util.StrOption('footer_text', 'footer text of the embed', required=False),
                app_util.AttachmentOption('footer_icon', 'file for embed', required=False),
                app_util.StrOption('link_button', 'sends a link in button form with embed', required=False),
            ],
        ),
    )
    @app_util.Cog.before_invoke(check)
    async def embed(
            self,
            ctx: app_util.Context,
            *,
            title: str, description: str, url: str,
            color: str, author: discord.User, author_url: str,
            thumbnail: discord.Attachment, image: discord.Attachment,
            footer_icon: discord.Attachment, footer_text: str, link_button: str,
    ):
        await ctx.defer(ephemeral=True)
        slots = {}
        if title:
            slots['title'] = title
            if url:
                slots['url'] = url
        if footer_text:
            slots['footer'] = {'text': footer_text}
            if footer_icon:
                slots['footer']['icon_url'] = footer_icon.url
        if description:
            slots['description'] = description.replace('$/', '\n')
        if author:
            slots['author'] = {
                'name': author.name,
                'icon_url': author.avatar.url,
            }
            if author_url:
                slots['author']['url'] = author_url
        if thumbnail:
            slots['thumbnail'] = {'url': thumbnail.url}
        if image:
            slots['image'] = {'url': image.url}

        if slots:
            view = discord.ui.View()
            if link_button:
                button = discord.ui.Button(style=discord.ButtonStyle.link, label='link', url=link_button)
                view.add_item(button)
            if color:
                slots['color'] = int(color, 16)
            embed = discord.Embed.from_dict(slots)
            await ctx.channel.send(embed=embed, view=view)
            await ctx.send_followup(f'{ctx.author.mention} embed posted here...')
        else:
            await ctx.send_followup(f'{ctx.author.mention} can not post an empty embed...')


def setup(bot: app_util.Bot):
    bot.add_application_cog(Main(bot))
