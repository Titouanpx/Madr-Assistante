import discord
import sqlite3

from bdayClasses import *
from generalClasses import *
from datetime import datetime
import asyncio

# print(discord.__version__)  # check to make sure at least once you're on the right version!
token = open("token.txt", "r").read()  # Saving my token into a text file.
client = discord.Client()  # starts the discord client.

conn = sqlite3.connect('my_database.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS bday(id INT, name TEXT, date DATE)''')
print("Table created or updated")

# Save (commit) the changes
conn.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
print("Result saved")

creator = "Madra#0779"


@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

    if datetime.today().strftime('%H:%M') == '15:20':
        print("hello")
        channel = client.get_channel(353882527657885699)
        await channel.send('happy bday')

    # today = datetime.today().strftime('%m-%d')
    # print(today)
    # if (today == c.execute('SELECT date FROM bday WHERE date =' + today)):
    #     channel = client.get_channel(353882527657885699)
    #     await channel.send('happy bday')


# @client.event
# async def display_date():
#     loop = asyncio.get_running_loop()
#     end_time = loop.time() + 86400
#     while True:
#         print(datetime.now())
#         if (loop.time() + 1.0) >= end_time:
#             break
#        await asyncio.sleep(1)
#        channel = client.get_channel(12324234183172)
#        await channel.send('happy bday')
#
# asyncio.run(display_date())


@client.event
async def on_message(message):  # event that happens per any message.
    if str(message.author) == 'Madr\'Assistante#6999':
        log(message)

    if str(message.author) == creator and message.content == "ping" in message.content.lower():
        log(message)
        await message.channel.send('pong')

    pseudo_id = message.author.id
    pseudo_name = message.author.name

    if message.content.startswith("$new"):
        log(message)
        # Insert a row of data
        c.execute("INSERT INTO bday VALUES (?, ?, ?)", (pseudo_id, pseudo_name, addmessage_to_date(message)))
        await message.channel.send('Votre pseudo : ' + pseudo_name + ' et votre anniversaire : '
                                   + sql_date_to_french_date(addmessage_to_date(message)) + ' ont bien été stockés.')
        conn.commit()

    if message.content == "$list":
        log(message)
        await message.channel.send("Attention, cela peut prendre un peu de temps")
        for row in c.execute('SELECT name, date FROM bday ORDER BY name, date'):
            await message.channel.send(row)
        await message.channel.send("Et voila :smile:")

    if message.content.startswith("$remove"):
        log(message)
        c.execute("DELETE FROM bday WHERE date = ?", (addmessage_to_date(message),))
        conn.commit()
        await message.channel.send('Votre anniversaire du ' + sql_date_to_french_date(removemessage_to_date(message))
                                   + ' a bien été supprimé')

    if message.content == "$clear" and str(message.author) == creator:
        log(message)
        # await message.channel.send('Est-tu sur de vouloir vider entierement la table? (y/n)')
        # if message.content == "y" or message.content == "Y":
        c.execute("DELETE FROM bday")
        conn.commit()
        await message.channel.send('Table vidée')

    if message.content == "$code":
        log(message)
        await message.channel.send(code())

    if message.content == "$help":
        log(message)
        await message.channel.send(help())


@client.event
async def on_member_join(member):
    channel = client.get_channel(336991381081817088)
    await channel.send(server_joined(member))


@client.event
async def on_member_remove(member):
    channel = client.get_channel(336991381081817088)
    await channel.send(server_left(member))

client.run(token)  # recall my token was saved!
