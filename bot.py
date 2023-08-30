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
    TOKEN = 'MTE0NjE1NDk0ODE3OTAwNTQ3MA.GkrnVt.B1AaIpLifcHp67mhPQNGMb7xajuPvfbhM0Jajc'
    client = discord.Client(intents=discord.Intents.all())


    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    client.run(TOKEN)
