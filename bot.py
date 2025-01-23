import discord
from bot_logic import gen_pass
import random  

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/hello'):
        await message.channel.send("🤝")
    elif message.content.startswith('/bye'):
        await message.channel.send("👋")
    elif message.content.startswith('/genpass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('/coinflip'):
       
        result = "Cara" if random.choice([True, False]) else "Cruz"
        await message.channel.send(f"Resultado del lanzamiento: {result}")
    elif message.content.startswith('/randomemoji'):
       
        emojis = ["😊", "😂", "😎", "🥺", "💯", "🤔", "❤️", "🔥", "✨"]
        random_emoji = random.choice(emojis)
        await message.channel.send(f"Emoji al azar: {random_emoji}")
    else:
        await message.channel.send(message.content)

client.run("Your TOKEN")
