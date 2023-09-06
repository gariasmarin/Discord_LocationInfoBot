import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.response_handler(user_message)
        # send as a dm or within the channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE0NjE1NDk0ODE3OTAwNTQ3MA.G-r0Ui.S2_Sx_txskplR2_lXasK5IDzXE5ZBo__A2w1JQ'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} typed: '{user_message}' (in \"{channel}\")")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
