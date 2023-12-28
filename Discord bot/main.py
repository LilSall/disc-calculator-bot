import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print('working ...')

@client.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f"The result of {num1} + {num2} is : {result}")

@client.command()
async def subtract(ctx, num1: int, num2: int):
    result = num1 - num2
    await ctx.send(f"The result of {num1} - {num2} is : {result}")#

@client.command()
async def multiply(ctx, num1: int, num2: int):
    result = num1 * num2
    await ctx.send(f"The result of {num1} x {num2} is : {result}")

@client.command()
async def divide(ctx, num1: int, num2: int):
    if num2 == 0:
        await ctx.send("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        await ctx.send(f"The result of {num1} / {num2} is : {result}")

@client.command()
async def calc(ctx, *, expression: str):
    try:
        result = eval(expression)
        await ctx.send(f"The result of the calculation is : {result}")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command()
async def Help(ctx):
    embed = discord.Embed(
        title="Calculator Bot",
        description="This bot helps you perform mathematical operations.",
        color=discord.Color.blue()
    )

    embed.add_field(name="!add", value="Add two numbers: `!add 5 10`", inline=False)
    embed.add_field(name="!subtract", value="Subtract two numbers: `!subtract 10 5`", inline=False)
    embed.add_field(name="!multiply", value="Multiply two numbers: `!multiply 5 10`", inline=False)
    embed.add_field(name="!divide", value="Divide two numbers: `!divide 10 5`", inline=False)
    embed.add_field(name="!calc", value="Calculate an expression: `!calculate 5 + 3`", inline=False)

    await ctx.send(embed=embed)



client.run('YOUR-BOT-TOKEN')
