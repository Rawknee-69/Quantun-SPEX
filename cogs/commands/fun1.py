
import discord
from discord.ext import commands

class hacker111111111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Security commands"""

    def _help_custom(self):
        emoji = '<:hacker_fun:1065916639767429151>'
        label = "Fun Commands"
        description = "Show You Fun Commands"
        return emoji, label, description
        

    @commands.group()
    async def __Fun__(self, ctx: commands.Context):
        """` tickle` , `kiss` , `hug` , `slap` , `pat` , `feed` , `pet` , `howgay` , `slots` , ` penis` , `meme` , `cat` , `iplookup`"""

