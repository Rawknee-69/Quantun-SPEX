import os
from core.Astroz import Astroz
import asyncio, json
import jishaku, cogs
from discord.ext import commands, tasks
import discord
from discord import app_commands
import traceback
from discord.ext.commands import Context
from discord import Spotify
import aiohttp
import base64
import time
from io import BytesIO

os.environ["JISHAKU_NO_DM_TRACEBACK"] = "False"
os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

client = Astroz()
tree = client.tree
TOKEN = os.getenv("TOKEN")
CMD_LOGS = client.get_channel(1146337447471497338)


@commands.cooldown(1, 2, commands.BucketType.user)
@commands.max_concurrency(1, per=commands.BucketType.default, wait=False)
@commands.guild_only()
@client.command()
async def generate(ctx: commands.Context, *, prompt: str):
  ETA = int(time.time() + 60)
  await ctx.send(
    f"**Go grab a coffee , this may take some time... ETA: <t:{ETA}:R>**")
  async with aiohttp.request("POST",
                             "https://backend.craiyon.com/generate",
                             json={"prompt": prompt}) as resp:
    r = await resp.json()
    images = r['images']
    image = BytesIO(base64.decodebytes(images[0].encode("utf-8")))
    return await ctx.reply(content="CONTENT GENERATED BY **craiyon.com**",
                           file=discord.File(image, "generatedimage.png"))




class Hacker(discord.ui.Modal):
  tit = discord.ui.TextInput(
    label='Embed Title',
    placeholder='Embed title here',
  )

  description = discord.ui.TextInput(
    label='Embed Description',
    style=discord.TextStyle.long,
    placeholder='Embed description optional',
    required=False,
    max_length=400,
  )

  thumbnail = discord.ui.TextInput(
    label='Embed Thumbnail',
    placeholder='Embed thumbnail here optional',
    required=False,
  )

  img = discord.ui.TextInput(
    label='Embed Image',
    placeholder='Embed image here optional',
    required=False,
  )

  footer = discord.ui.TextInput(
    label='Embed footer',
    placeholder='Embed footer here optional',
    required=False,
  )

  async def on_submit(self, interaction: discord.Interaction):
    embed = discord.Embed(title=self.tit.value,
                          description=self.description.value,
                          color=0x00FFE4)
    if not self.thumbnail.value is None:
      embed.set_thumbnail(url=self.thumbnail.value)
    if not self.img.value is None:
      embed.set_image(url=self.img.value)
    if not self.footer.value is None:
      embed.set_footer(text=self.footer.value)
    await interaction.response.send_message(embed=embed)

  async def on_error(self, interaction: discord.Interaction,
                     error: Exception) -> None:
    await interaction.response.send_message('Oops! Something went wrong.',
                                            ephemeral=True)

    traceback.print_tb(error.__traceback__)


@tree.command(name="embed", description="Create An Embed")
async def _embed(interaction: discord.Interaction) -> None:
  await interaction.response.send_modal(Hacker())


########################################


@client.event
async def on_ready():
  print("Loaded & Online!")
  print(f"Logged in as: {client.user}")
  print(f"Connected to: {len(client.guilds)} guilds")
  print(f"Connected to: {len(client.users)} users")
  print("SRC Credits Goes TO @itzyourhacker")
  try:
    synced = await client.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(e)


@client.event
async def on_command_completion(context: Context) -> None:

  full_command_name = context.command.qualified_name
  split = full_command_name.split("\n")
  executed_command = str(split[0])
  hacker = CMD_LOGS
  if context.guild is not None:
    try:
      embed = discord.Embed(color=0x2f3136)
      embed.set_author(
        name=f"Executed {executed_command} Command By : {context.author}",
        icon_url=f"{context.author.avatar}")
      embed.set_thumbnail(url=f"{context.author.avatar}")
      embed.add_field(name="Command Name :",
                      value=f"{executed_command}",
                      inline=False)
      embed.add_field(
        name="Command Executed By :",
        value=
        f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed.add_field(
        name="Command Executed In :",
        value=
        f"{context.guild.name}  | ID: [{context.guild.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed.add_field(
        name="Command Executed In Channel :",
        value=
        f"{context.channel.name}  | ID: [{context.channel.id}](https://discord.com/channel/{context.channel.id})",
        inline=False)
      embed.set_footer(text="Thanks for Using Me!",
                       icon_url=client.user.display_avatar.url)
      await hacker.send(embed=embed)
    except:
      print('Error')
  else:
    try:

      embed1 = discord.Embed(color=0x2f3136)
      embed1.set_author(
        name=f"Executed {executed_command} Command By : {context.author}",
        icon_url=f"{context.author.avatar}")
      embed1.set_thumbnail(url=f"{context.author.avatar}")
      embed1.add_field(name="Command Name :",
                       value=f"{executed_command}",
                       inline=False)
      embed1.add_field(
        name="Command Executed By :",
        value=
        f"{context.author} | ID: [{context.author.id}](https://discord.com/users/{context.author.id})",
        inline=False)
      embed1.set_footer(text="Thanks For Using Me!",
                        icon_url=client.user.display_avatar.url)
      await hacker.send(embed=embed1)
    except:
      print("SRC Credits Goes TO @itzyourhacker")


from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route('/')
def home():
  return "YouTube.com/@CyberSecDiscord"


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  server = Thread(target=run)
  server.start()


keep_alive()


@client.command()
async def makeembed(ctx, *, description):
  if not description:
    await ctx.channel.send(
      "One or more values are missing. Command should look like 'makeEmbed (description)'"
    )

  embed = discord.Embed(description=description, color=0x2f3136)
  if ctx.guild.icon is not None:
    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon.url)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)

  await ctx.send(embed=embed)


async def main():
  async with client:
    os.system("clear")
    await client.load_extension("cogs")
    await client.load_extension("jishaku")
    await client.start(TOKEN)


if __name__ == "__main__":
  asyncio.run(main())
