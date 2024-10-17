import discord
import json
from src.model import generate_response
from src.moderation import is_toxic
from src.memory import update_memory, get_memory
from src.role_manager import change_user_role

# Load config
with open('../config/config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot {client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Moderation: Check if message is toxic
    if is_toxic(message.content):
        await message.channel.send("Pesan Anda mengandung konten berbahaya.")
        return

    # Responding to messages
    if "rena" in message.content.lower():
        response = generate_response(message.content)
        await message.channel.send(response)

    # Memory system
    if "salam kenal" in message.content.lower():
        update_memory(message.author.id, message.author.name)
        await message.channel.send(f"Halo {message.author.name}!")

    if "siapa aku" in message.content.lower():
        username = get_memory(message.author.id)
        await message.channel.send(f"Kamu adalah {username}")

    # Role management
    if "ubah role" in message.content.lower():
        await change_user_role(message)

client.run(config["token"])
