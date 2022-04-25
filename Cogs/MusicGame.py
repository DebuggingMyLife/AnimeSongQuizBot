import discord
from discord.ext import commands
import pandas
import random
import time

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = pandas.read_csv("AnimeMusicDB.csv")

    @commands.command()
    async def RandomMusic(self,ctx):
        RandomIndex = random.randint(1,2105)
        print(RandomIndex)
        Track = self.db.iloc[RandomIndex,1]
        await ctx.send(f"Your random track is : {Track}")

    @commands.command(aliases=['gs'])
    async def GS(self, ctx):
        while True:
            RandomIndex = random.randint(1,2105)
            Track = self.db.iloc[RandomIndex,1]
            AnimeTitle = self.db.iloc[RandomIndex,8]
            await ctx.invoke(self.bot.get_command('play'), search=Track)
            while True:

                answer = await.self.bot.wait_for(AnimeTitle), check=lambda message: message.author == ctx.author):
                await ctx.send("Correct!")

            await ctx.invoke(self.bot.get_command('leave'))
            await ctx.send(f"This track is from {AnimeTitle}")
            break


async def setup(client):
    await client.add_cog(Game(client))
