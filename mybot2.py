import discord
from discord.ext import commands
from mycode import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def hah(ctx, count_heh = 5):
    await ctx.send("ha" * count_heh)

@bot.command()
async def generate_password(ctx):
    await ctx.send('ini password untukmu:')
    await ctx.send(gen_pass(12))

@bot.command()
async def pangkatkan(ctx):
    await ctx.send('coba kirimkan angka yg ingin di pangkatkan')
    angka = await bot.wait_for('message',check=lambda m:m.author == ctx.author and m.channel == ctx.channel)
    angka=int(angka.content)
    
    await ctx.send(f'berikut pangkat dua dari{angka}')
    await ctx.send(angka**2)
    @bot.command()
async def help(ctx):
    await ctx.send('hello = untuk menyapa bot !generate_password = untuk membuat password !pangkatkan :untuk mempangkat duakan angka')

bot.run('masukkan token')
