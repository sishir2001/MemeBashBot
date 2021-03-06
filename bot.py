#bot.py

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
# for saving the image 
import requests
import uuid # for unique naming of the image 
import shutil
# from local files 
from dialogFiles.movieDialoguesEnglish import movieDialoguesEnglish
from dialogFiles.movieDialoguesTelugu import movieDialoguesTelugu
from dialogFiles.movieDialoguesHindi import movieDialoguesHindi
from dialogFiles.cussWords import cussWords
# dotenv library for parsing .env files 


# loads the environment variables from .env file into shell environment variable 
load_dotenv()
# Get the token from environment varible 
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
# client - an object that represents the connection to discord 
# ! client = discord.Client(intents = intents)
# convering all clients to bot
bot = commands.Bot(command_prefix='!',intents=intents)

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
    await member.send(f"Welcome to Our Server {member.name.mention} 🤙🏻!!")
    print(f"A new member {member.name} joined !")


# responding to messages from the channel in the guild 
@bot.event
async def on_message(message):
    if(message.author == bot.user):
        return

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
@bot.command(name='get.dialog.telugu',help="gives you random telugu movie dialogues")
async def getDialoguesTelugu(ctx):
    # ? @param ctx : context - contains the information of channel and guild from where the command came from 
    randomDialogue = f"{ctx.author.mention} be like : " + random.choice(movieDialoguesTelugu)
    print(f"A Telugu dialogue replied to {ctx.author} ")
    await ctx.send(randomDialogue)
    

@bot.command(name='get.dialog.english',help="gives you random english movie dialogues")
async def getDialoguesTelugu(ctx):
    # ? @param ctx : context - contains the information of channel and guild from where the command came from 
    randomDialogue = f"{ctx.author.mention} be like : " + random.choice(movieDialoguesEnglish)
    print(f"A Telugu dialogue replied to {ctx.author} ")
    await ctx.send(randomDialogue)
    
@bot.command(name='get.dialog.hindi',help="gives you random hindi movie dialogues")
async def getDialoguesTelugu(ctx):
    # ? @param ctx : context - contains the information of channel and guild from where the command came from 
    randomDialogue = f"{ctx.author.mention} be like : " + random.choice(movieDialoguesHindi)
    print(f"A Telugu dialogue replied to {ctx.author} ")
    await ctx.send(randomDialogue)

@bot.command()
async def test(ctx,*args):
    # * here args variable is a tuple . variable no of arguments 
    print(f"Members in server : {ctx.guild} are {ctx.guild.members}")
    await ctx.send(f"{len(args)} arguments : {','.join(args)} , server: {ctx.guild}")

# ! command for creating a new channel 
# only with admin roles can create a channel 
@bot.command(name="create_text_channel",help="Creates a new channel . Arg : nameOfTheChannel")
@commands.has_role('admin')
async def createTextChannel(ctx,channelName="None"):
    if(channelName == "None"):
        await ctx.send(f"{ctx.author.mention} , You need to specify the text-channel name ! !create_text_channel <Channel Name>")
    guild = ctx.guild
    # !checking whether the given channel exists 
    existing_channel = discord.utils.get(guild.channels,name=channelName)
    if not existing_channel:
        # create a new channel
        print(f"Creating a text channel : {channelName}")
        await guild.create_text_channel(channelName)
    else : 
        await ctx.send(f"{ctx.author.mention} , A text channel with these name already exists!")

# ! test : Saving and Sending images 
#bot commands for saving an uploaded image 
@bot.command(name = "upload_image",help="Upload Your selfie to generate an amazing meme! ")
async def saveUploadedImage(ctx):
    try:
        # saving the image 
        imageName = str(uuid.uuid4()) + '.jpg'
        # folderPath = 'uploadedPics/'
        await ctx.message.attachments[0].save(imageName)
        print(f"Saved uploaded Image successfuly : {imageName}")
        await ctx.send(f"{ctx.author.mention},Image saved successfully !")
        # sending an image back 
        await ctx.send("Here is your meme !",file = discord.File(imageName))
        print(f"Sent a image : {imageName} to the channel !")
    except IndexError :
        print("No attachments of images")
        await ctx.send(f"{ctx.author.mention}, there is no image uploaded !")


# handling exceptions 
@bot.event
async def on_error(event,*args,**kwargs):
    with open('err_log','a') as f:
        print("error occured")
        f.write(f"Unhandled Error : {args[0]} \n ")

# handling command errors
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.errors.CheckFailure):
        await ctx.send(f"{ctx.author.mention} , You dont have the correct role for this !")

#run the client 
bot.run(TOKEN) 


