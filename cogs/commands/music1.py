import discord
from discord.ext import commands


class hacker1111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Music commands"""
  
    def help_custom(self):
		      emoji = '<:icons_music:1065918333389643826>'
		      label = "Music Commands"
		      description = "Show You Music Commands"
		      return emoji, label, description

    @commands.group()
    async def __Music__(self, ctx: commands.Context):
        """`connect` , `disconnect` , `play` , `loop` , `stop` , `queue` , `pause` , `resume` , `skip`"""