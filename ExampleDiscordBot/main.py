import discord

# Define Discord Bot Client and Prefix (Ex. Prefix: "!")
bot = discord.Client()
prefix = "YOUR_PREFIX"


# Executed when bot is started
async def on_ready():
    print("Bot started as {0.client}".format(bot))


# Executed when Message is sent
async def on_message(message):
    if message.author == bot:
        return

    # Here you can add your own Command with Features
    if message.content.startswith(prefix + "YOUR_COMMAND"):
        await message.channel.send("Hello World!")


bot.run("YOUR_TOKEN_HERE")