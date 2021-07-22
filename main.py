import math
import os
import discord
import random
import requests
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path="config")

srfcPath = "C:/Users/Rango/Documents/Dev/Moi/Po.py/srfc/"
split = " "


class Popy(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="|")

    async def on_ready(self):
        print(f"{self.user} is connected")

    async def on_message(self, message):
        if message.content.lower() == popy.command_prefix + 'oui':
            await message.channel.send("non")

        # Envoie un gif random du SRFC
        if message.content.lower() == popy.command_prefix + "srfc":
            await message.channel.send(file=discord.File(srfcPath + str(random.randint(1, 6)) + ".gif"))

        # Envoie un nombre contenu entre les 2 paramètres renseignés
        if message.content.lower().startswith(f"{popy.command_prefix}random"):
            try:
                min_val = int(message.content.split(" ", 3)[1:2][0])
                max_val = int(message.content.split(" ", 3)[2:3][0])
                await message.channel.send(random.randint(min_val, max_val))
            except ValueError:
                await message.channel.send("Format non valide")
        if message.content.lower().startswith(f"{popy.command_prefix}meteo"):
            try:
                searched_city = message.content.split(" ", 3)[1:2][0]
                response = requests.get(
                    os.getenv("BASE_URL") + searched_city + "&lang=fr&appid=" + os.getenv("API_KEY"))
                data = response.json()
                temp = math.floor(data['main']['temp'] - 273)
                await message.channel.send(f"Il fait {temp}°C à {data['name']}, {data['sys']['country']}")

            except KeyError:
                await message.channel.send('Ville non trouvée')


popy = Popy()

popy.run(os.getenv("TOKEN"))
