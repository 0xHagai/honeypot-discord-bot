import requests
import discord
from discord.ext import commands
import os




intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
@bot.event
async def on_ready():
    print("Bot is online")

@bot.hybrid_command(with_app_command=True)
async def hp(ctx, token:str):

    chain = "eth"
    detect = requests.get(f"https://aywt3wreda.execute-api.eu-west-1.amazonaws.com/default/IsHoneypot?chain={chain}&token={token}").json()

    if "message" in detect :
        await ctx.send("Invalid token address or chain")
    else :
        if detect['IsHoneypot'] == True:
            embed = discord.Embed(
                title= "⚠ HONEYPOT ⚠",
                color= discord.Color.red()
                
            )
            embed.set_thumbnail(url="https://i.pinimg.com/originals/e3/f4/73/e3f47330fbb5d8fec26c311100c876c0.png")
            embed.set_footer(text="Check made by honeypot.is might not be accurate")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title= "NOT HONEYPOT",
                color= discord.Color.green()
                
            )
            embed.add_field(name="Buy tax", value=str(detect['BuyTax']) + "%",inline=True)
            embed.add_field(name="Sell tax", value=str(detect['SellTax']) + "%",inline=True)
            embed.add_field(name="Holders", value = f"https://etherscan.io/token/{token}#balances", inline=False)
            embed.set_thumbnail(url="https://creazilla-store.fra1.digitaloceanspaces.com/cliparts/60301/thumb-up-emoji-clipart-xl.png")
            embed.set_footer(text="Check made by honeypot.is might not be accurate")
            await ctx.send(embed=embed)

    


bot.run(os.environ['discord_api'])
