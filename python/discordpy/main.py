import os
import asyncio
import discord
from discord.ext import commands

from replit import db
from models import init_db
from maintain import maintain


def get_prefix(bot, message):
    id = str(message.guild.id)
    guilds = db["guilds"]
    guild = guilds.get(id)
    if not guild:
        guilds[id] = {"prefix": "."}
        db["guilds"] = guilds
        guild = guilds[id]
    return guild["prefix"]


help_command = commands.DefaultHelpCommand(no_category="Commands")
discord.utils.setup_logging()
bot = commands.Bot(
    intents=discord.Intents.all(), command_prefix=get_prefix, help_command=help_command
)


@bot.command()
async def load(ctx, extension):
    """Load cog"""
    cog = f"cogs.{extension}"
    await bot.load_extension(cog)
    await ctx.send(f"{cog} loaded")


@bot.command()
async def unload(ctx, extension):
    """Unload cog"""
    cog = f"cogs.{extension}"
    await bot.unload_extension(cog)
    await ctx.send(f"{cog} unloaded")


@bot.command()
async def reload(ctx, extension):
    """Reload cog"""
    await unload(ctx, extension)
    await load(ctx, extension)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            cog = f"cogs.{filename[:-3]}"
            await bot.load_extension(cog)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(os.environ.get("SECERET_KEY"))


if __name__ == "__main__":
    try:
        init_db()
        maintain()
        asyncio.run(main())
    finally:
        db.close()
