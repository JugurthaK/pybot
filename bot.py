# -*- coding: utf-8 -*-
# prefix : /p03
import discord
import random
import requests as req
import json
import time
import base64
import config
## Functions to use
# Create a random with dice
OWM = config.openweather_token

def rollTheDice(n = 6):
    return (random.randint(1, n))

def getWeather(city):
    rep = req.get("https://api.openweathermap.org/data/2.5/weather?q=%s,fr&appid=%s&units=metric" % (city, OWM))
    values = json.loads(rep.text)
    embed = discord.Embed()
    embed.add_field(name="Ville", value=values["name"], inline=True)
    embed.add_field(name="Météo", value=values["weather"][0]["description"].capitalize(), inline=True)
    embed.add_field(name="Température", value="%s °C" % values["main"]["temp"], inline=True)
    ts_sr = time.ctime(values["sys"]["sunrise"])
    embed.add_field(name=":sunny:", value=ts_sr, inline=True)
    ts_ss = time.ctime(values["sys"]["sunset"])
    embed.add_field(name=":sunrise:", value=ts_ss, inline=True)
    return (embed)

def getPokemon(name):
    rep = req.get("http://ray0.be/pokeapi/pokemon-row/fr/%s" % name)
    values = json.loads(rep.text)
    rep = json.loads(rep.text)
    data = rep["data"]
    nom_pkmn = data['nom_fr'] 
    type1_pkmn = data['type1'] 
    type2_pkmn = data['type2']
    stat_pv = data['stat_pv']
    stat_atq = data['stat_attaque']
    stat_defense = data['stat_defense']
    stat_atqspe = data['stat_attaquespe']
    stat_defensespe = data['stat_defensespe']
    stat_vitesse = data['stat_vitesse']
    embed = discord.Embed(color=0xffe000)
    embed.set_author(name=nom_pkmn)
    embed.set_thumbnail(url='http://ray0.be/pokeapi/pokemon-img/fr/%s'% name)
    embed.add_field(name="Type Primaire", value=type1_pkmn, inline=True)
    embed.add_field(name="Type Secondaire", value=type2_pkmn, inline=True)
    embed.add_field(name="Points de Vie", value=stat_pv, inline=False)
    embed.add_field(name="Attaque", value=stat_atq, inline=True)
    embed.add_field(name="Défense", value=stat_defense, inline=True)
    embed.add_field(name="Attaque Spéciale", value=stat_atqspe, inline=True)
    embed.add_field(name="Défense Spéciale", value=stat_defensespe, inline=True)
    embed.add_field(name="Vitesse", value=stat_vitesse, inline=True)
    return (embed)

######################################################## MAIN CODE ####################################################################
client = discord.Client()
@client.event
async def on_ready():
    print("The bot is Ready : Logged as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith("/p03"):
        splitted = message.content.split(" ")
        argType = splitted[1]
        ## Gestion des commandes
        # Gestion du ping
        if (argType == "ping"):
            await message.channel.send("Le pong")
        # Gestion du dice
        if (argType == "dice"):
            if len(splitted) != 3:
                argValue = 6
            else: 
                argValue = int(splitted[2])
            await message.channel.send("Résultat du tirage : %d" % rollTheDice(argValue))
        # Gestion de cat
        if (argType == "cat"):
            await message.channel.send("https://cataas.com/c")
        # Gestion de la météo
        if (argType == "meteo"):
            if len(splitted) != 3:
                await message.channel.send(embed=getWeather("calais"))
            else :
                await message.channel.send(embed=getWeather(splitted[2]))
        if (argType == "pokemon"):
            if len(splitted) != 3:
                await message.channel.send("Il faut renseigner un pokémon !")
            else :
                await message.channel.send(embed=getPokemon(splitted[2]))
client.run(config.discord_token)
