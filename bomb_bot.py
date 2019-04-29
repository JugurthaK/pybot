# -*- coding: utf-8 -*-
import discord
import random
def syracuse(n):
    if (n%2 == 0):
        return (n//2)
    else :
        return (n*3+1)

def randomizePlayer(tab):
    return (tab[random.randint(0, len(tab) -1)])

def clearArray(tab):
    tab = list()

client = discord.Client()

@client.event
async def on_ready():
    print("Oh shit, here we go again 💣")



@client.event
async def on_message(message):
    if message.content.startswith("/bomb"):
        splitted = message.content.split(" ")
        argType = splitted[1]
        print("Arg Type ", argType)
        if (argType == "🚀"):
            global tabBot
            tabBot = list()
            for i in range(3, len(splitted)):
                tabBot.append(splitted[i])
            await message.channel.send("*is Ready*")

        if tabBot[0] == "/PyBomb":
            n = syracuse(int(splitted[2])) 
            player = randomizePlayer(tabBot)
            await message.channel.send("%s :bomb: %d" % (player,n))
    
        if (argType == ":skull:"):
            if (message.author != client.user):
                await message.channel.send("HAHA NOOB !")
            else:
                await message.channel.send("OH NO !")
            tabBot = list()
            print("Reset de la partie")
    
    if message.content.startswith("/PyBomb"):
        splitted = message.content.split(" ")
        argType = splitted[1]
        if (argType == ":bomb:"):
            n = syracuse(int(splitted[2]))
            if n != 1:
                player = randomizePlayer(tabBot)
                await message.channel.send("%s :bomb: %d" % (player,n))
            else :
                await message.channel.send("/bomb :skull:")
        
client.run(config.discord_bomb_token)
