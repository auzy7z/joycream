import discord

async def change_user_role(message):
    if message.author.guild_permissions.administrator:
        role_name = "mod"
        role = discord.utils.get(message.guild.roles, name=role_name)
        user = message.mentions[0]  # User yang disebutkan di pesan
        await user.add_roles(role)
        await message.channel.send(f"Role {user.name} telah diubah menjadi {role_name}")
    else:
        await message.channel.send("Anda tidak memiliki izin untuk mengubah role.")
