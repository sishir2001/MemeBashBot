#bot.py

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
# dotenv library for parsing .env files 
# ! random movie dialogues 
movieDialoguesTelugu = ["I like the way you breathe preethi ...",
"Common preethi dont do this to me !",
"I curse you to marry a tulu guy !",
"Veera Shankar Reddy… Mokke Kada Ani Peekeste Peeka Kostaa",
"Tappu Naa Vaipu Undi Kabatti Tala Dinchukuni Veltunna, Ledante Talalu Teesukellevaadni ",
"Chudu Oka Vaipe Chudu Inko Vaipu Chudalanukoku Tattukolevu",
"Naa Saavu Nenu Sasta Neekenduku",
"Atiga Aashapade Magavaadu… Atiga Aavashapade Aadadi Sukhapadinatlu Charitralo Ledu",
"Sar Sarle Enno Anukuntam… Anni Avutaya Enti",
"Okka Saari Commit Ayite Naa Maata Nene Vinanu",
"Evadu Kodite Dimma Tirigi Mind Block Ayipoddo Aade Pandu Gaadu ",
"Commissioner Kooturani Chepte Bhayapadipotama… Commissioner Kooturlani Preminchakudada… Commissioner Kooturlaki Mogudlu Raara",
"City Ki Entho Mandi Commissioner Lu Vastuntaru Pothuntaru.. Chanti Gaadu Eppudu Ikkade Untadu Local",
"Eppudochamani Kaadannayya Bullet Diginda Leda",
"Naa Peru Daya… Naku Lenide Adi",
"Iddaru Kottukunte Yuddham… Ade Okadu Meedadipothe Dandayaatra Idi Daya Gaadi Dandayaatra",
"Neeku Ego Lopale Untademo Naku Naa Chuttu Wifi La Untadi",
"Ooru Maarite Tine Food Maaruddi Padukune Bed Maaruddi Blood Enduku Maaruddi Ra Bloody Fool",
"Flute Jinka Mundu Oodu Simham Mundu Kaadu",
"Seat Kaadu Kada Assembly Gate Kuda Daatanivvanu",
"Any Centre Single Hand Ganesh",
"Mass Tho Pettukunte Madatha Madathadipoddi ",
"Tagore… Tongue Teguddi ",
"Na Daari Rahadari.. Better Don’t Come In My way ",
"Yuddham Chetakaanode Dharmam Gurinchi Maatladatadu Sir",
]

movieDialoguesEnglish = [
"Frankly, my dear, I don't give a damn.",
"Bond ... James Bond",
"Baba Yaga .. He is man of utmost concerntration .",
"I'm going to make him an offer he can't refuse",
"My name is Fish Mooney, bitch!",
"Do you have any idea who you're talking to?",
"Friends don't lie.",
"I am the danger.",
"... then maybe your best course would be to tread lightly.",
"I am the one who knocks.",
"When you play the Game of Thrones, you win or you die.",
"If you want justice, you've come to the wrong place.",
"Valar Morghulis.",
"I demand a trial by combat!",
"Who wants to be king?",
"Winter is coming.",
"The Lannisters send their regards.",
"By order of the peaky blinders...",
"You know nothing Jon Snow.",
"Fear cuts deeper than swords.",
"Everything before the word ‘but’ is horseshit.",
"A lion doesn’t concern himself with the opinions of a sheep.",
"The man who passes the sentence should swing the sword.",
"Any man who must say ‘I am the king’ is no true king.",
"A ruler who kills those devoted to her is not a ruler who inspires devotion.",
"Never forget what you are. The rest of the world will not. Wear it like armour, and it can never be used to hurt you.",
"A Lannister always pays his debts.",
"Nothing f***s you harder than time.",
"All men must die, but we are not men",
"The night is dark and full of terrors",
"Dreams didnt make us kings , dragons did .... You motherfuckers!"
]
movieDialoguesHindi = [
"Our Bussiness is our Bussiness , its none of your bussiness",
"Rishtey mein toh hum tumhare baap lagte hai, naam hai Shahenshaah!",
"How’s the josh?",
"Madarchoood , Tu vahi rukh mei ah raha hoon !!",
"Saala , shanthi se chodh bhi nehi dete !",
"Mata ji yahan hai, Behen yahan hai, Maa-Behen ek karne mein aasani hogi.",
"Attack me bhi gun, defense me bhi gun, Hum banayenge Mirzapur ko Amrica!",
"Neta banna hai toh Gundey paalo. Gundey mat bano.",
"Darr ki yahi dikkat hai, ki kabhi bhi Khatam ho sakta hai.",
"Suru majboori mein kiye the….. Ab maza aa raha hai.",
"Izzat nahi karte hain… Darte hain sab.",
"Chutiya hain tumhara ladka. ..... Chutiya hain woh important nahi hai. Hamara ladka hai, Woh important hai.",
"Agli baar Munna Bhaiya ghar aaye… Zinda wapas hi nahi laute toh?",
"Oh Bhosidi waley Chacha. Rest kariye, varna Rest in Peace ho jaoge!",
"Middle class aadmi, aadmi nahi chutiya hota hai. Chutiya.",
]

cussWords = [
"fuck",
"fucking",
"bitch",
"asshole",
"tits",
"bastard",
"Vagina",
"gudda",
"bollocks",
"puka",
"pooka",
"yedava",
"lanje",
"lanja",
"kodaka",
"fuckers",
"motherfuckers",
"motherfucker"
]

# loads the environment variables from .env file into shell environment variable 
load_dotenv()
# Get the token from environment varible 
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
# client - an object that represents the connection to discord 
# ! client = discord.Client(intents = intents)
# convering all clients to bot
bot = commands.Bot(command_prefix='$',intents=intents)

# an event handler , which handles the event when connected to discord
@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to discord!")
    # ? The below code is for knowing the guilds the client is in and users in the guid 
    # print("Guild in which the client is there :  ")
    # for guild in client.guilds :
    #     print(f"\nname : {guild.name}, id : {guild.id}")
    #     GuildMembers = "\n - ".join([member.name for member in guild.members])
    #     print(f"Guild Members : \n - {GuildMembers}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to Our Server {member.name.mention}, Sukhibhawa 🤙🏻!!")
    print(f"A new member {member.name} joined !")


# responding to messages from the channel in the guild 
@bot.event
async def on_message(message):
    if(message.author == bot.user):
        return
    # ! need to be placed in bot commands 
    # elif message.content == "bot_get_dialogues_english":
    #     randomDialogue = f"{message.author} be like : " + random.choice(movieDialoguesEnglish)
    #     await message.channel.send(randomDialogue)
    #     print(f"A English dialogue replied to {message.author.name} ")

    # elif message.content == "bot_get_dialogues_hindi":
    #     randomDialogue = f"{message.author} be like : " + random.choice(movieDialoguesHindi)
    #     await message.channel.send(randomDialogue)
    #     print(f"A Hindi dialogue replied to {message.author.name} ")

    if message.content.lower() in cussWords:
        await message.channel.send(f'Well {message.author.mention}, you need to control your tongue .And you that {message.content} 🤣')
        print(f"Warned {message.author.name} . ")

    elif message.content.lower() == "raise-exception":
        print("Exception raised !")
        raise discord.DiscordException

    # Warning the users using cussWords 
    else:
        words = message.content.split()
        for cuss in words:
            if(cuss.lower() in cussWords):
                await message.channel.send(f'Well {message.author.mention}, you need to control your tongue .And you are that {cuss} 👺')
                print(f"Warned {message.author.name} . ")
                break
    # without the below line of code , bot commands dont work 
    await bot.process_commands(message)

# commands for the bot 
@bot.command(name='get_dialogues_telugu')
async def getDialoguesTelugu(ctx):
    # ? @param ctx : context - contains the information of channel and guild from where the command came from 
    randomDialogue = f"{ctx.author.mention} be like : " + random.choice(movieDialoguesTelugu)
    print(f"A Telugu dialogue replied to {ctx.author} ")
    await ctx.send(randomDialogue)
    

@bot.command(name='get_dialogues_english')
async def getDialoguesTelugu(ctx):
    # ? @param ctx : context - contains the information of channel and guild from where the command came from 
    randomDialogue = f"{ctx.author.mention} be like : " + random.choice(movieDialoguesEnglish)
    print(f"A Telugu dialogue replied to {ctx.author} ")
    await ctx.send(randomDialogue)
    
@bot.command(name='get_dialogues_hindi')
async def getDialoguesTelugu(ctx):
    # ? @param ctx : context - contains the information of channel and guild from where the command came from 
    randomDialogue = f"{ctx.author.mention} be like : " + random.choice(movieDialoguesHindi)
    print(f"A Telugu dialogue replied to {ctx.author} ")
    await ctx.send(randomDialogue)

# handling exceptions 
@bot.event
async def on_error(event,*args,**kwargs):
    with open('err_log','a') as f:
        print("error occured")
        f.write(f"Unhandled Error : {args[0]} \n ")

#run the client 
bot.run(TOKEN) 


