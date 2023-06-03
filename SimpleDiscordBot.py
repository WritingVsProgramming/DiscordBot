import discord

# Erstelle eine Application unter: https://discord.com/developers/applications
# Erstelle einen Bot
# Schreibe hier den Token hinein, der generiert wird wenn man den "Reset Token" Knopf drueckt
TOKEN = "<Token>"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


# Sachen die passieren sollen, bevor der Bot startet
# ==================================================
print("Ich bin ein Discord Bot")


# Bot Functions:
# ==============

# Das passiert, wenn der Bot startet:
@client.event
async def on_ready():
	print(f'{client.user} ist jetzt online!')


# Das passiert, wenn auf dem Server eine Nachricht geschrieben wird
@client.event
async def on_message(message):
    # Stelle sicher, dass der Bot nicht auf seine eigenen Nachrichten reagiert
    if message.author == client.user:
        return

    # Hole die Information der Nachricht: 
    author = message.author			    # Autor
    username = str(message.author)		# Benutzername
    user_message = str(message.content)	# Nachrichten Inhalt
    channel = str(message.channel)		# Channel in dem die Nachricht geschickt wurde

    # Gebe diese Infos einmal im Terminal aus:
    print(f"{username} said: '{user_message}' ({channel})")

    # Wenn die Nachricht mit einem '!' beginnt, regaiere darauf
    if user_message[0] == '!': 

	    # Schicke eine oeffentliche Nachricht in den Channel zurueck
        await message.channel.send("Kuchen")
	
	    # Schicke eine private Nachricht an den Author der original Nachricht
        await message.author.send("Kuchen nur für dich, "+ username)


# Startet den Bot:
# ================
client.run(TOKEN)

