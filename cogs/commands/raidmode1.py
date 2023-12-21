import discord
from discord.ext import commands


class hacker1111(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    """Voice Commands"""

    def _help_custom(self):
        emoji =  '<:hacker_raidmode:1065916706901475348>'
        label = "Raidmode Commands"
        description = "Show You Raidmode Commands"
        return emoji, label, description                  
        

    @commands.group()
    async def __Raidmode__(self, ctx: commands.Context):
        """`automod` , `antispam on` , `antispam off` , `antilink off` ,  `antilink on`
        
        `logall enable` , `logall disable`"""
        
        
        