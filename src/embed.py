import sys
import discord
import traceback
import extslash


class Embed(extslash.Cog):
    def __init__(self, bot: extslash.Bot):
        self.bot = bot

    @extslash.Cog.command(
        command=extslash.SlashCommand(
            name='embed',
            description='creates an embed to a channel',
            options=[
                extslash.ChannelOption(
                    name='channel',
                    description='text channel to send the embed to',
                    channel_types=[
                        extslash.ChannelType.GUILD_TEXT,
                        extslash.ChannelType.GUILD_NEWS,
                        extslash.ChannelType.GUILD_STORE
                    ],
                    required=True),
                extslash.StrOption('title', 'title of the embed', required=False),
                extslash.StrOption('description', 'description of the embed', required=False),
                extslash.StrOption('url', 'url of the embed', required=False),
                extslash.StrOption('color', 'color hex of the embed', required=False),
                extslash.UserOption('author', 'author of the embed', required=False),
                extslash.StrOption('footer', 'footer text of the embed', required=False),
                extslash.AttachmentOption('thumbnail', 'image file of the thumbnail', required=False),
                extslash.AttachmentOption('image', 'image file of embed image', required=False),
            ],
        )
    )
    async def command(self, ctx: extslash.ApplicationContext):

        await ctx.defer(ephemeral=True)

        if not ctx.author.guild_permissions.administrator:
            await ctx.send_followup('You need to be an admin or equivalent to use this command', ephemeral=True)
            return

        channel = ctx.options[0].value
        if not channel.permissions_for(ctx.me).send_messages:
            await ctx.send_followup(f'I do not have permission to send messages in {channel.mention}', ephemeral=True)
            return

        ctx.options.pop(0)
        slots = {}
        for option in ctx.options:
            special = ['author', 'footer', 'thumbnail', 'image', 'color', 'description']
            name = option.name
            if name not in special:
                slots[option.name] = option.value
            elif option.name == 'footer':
                slots['footer'] = {'text': option.value}
            elif option.name == 'thumbnail':
                slots['thumbnail'] = {'url': option.value.url}
            elif option.name == 'image':
                slots['image'] = {'url': option.value.url}
            elif option.name == 'color':
                slots['color'] = int(f'0x{option.value}', 16)
            elif option.name == 'author':
                slots['author'] = {
                    'name': option.value.name,
                    'icon_url': option.value.avatar.url
                }
            elif option.name == 'description':
                string = option.value.replace('$/', '\n')
                slots['description'] = string

        embed = discord.Embed.from_dict(slots)
        await channel.send(embed=embed)
        await ctx.send_followup(f'Embed sent successfully to {channel.mention}', ephemeral=True)


    @extslash.Cog.listener
    async def on_command_error(self, ctx: extslash.ApplicationContext, error: Exception):
        stack = traceback.format_exception(type(error), error, error.__traceback__)
        print(''.join(stack), file=sys.stderr)
        await ctx.send_followup(f'Something went wrong! Please try again...', ephemeral=True)





def setup(bot: extslash.Bot):
    bot.add_slash_cog(Embed(bot))
