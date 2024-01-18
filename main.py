import os
import sys
import json
import requests
import time
import webbrowser
from pystyle import *
from colorama import *

os.system("cls || clear")

intro = """ 
            ██╗██████╗     ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
            ██║██╔══██╗    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
            ██║██████╔╝    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
            ██║██╔═══╝     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
            ██║██║         ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
            ╚═╝╚═╝         ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                 
                              [+] github.com/ZekromDev

                             >> Press Enter <<"""

Anime.Fade(Center.Center(intro), Colors.white_to_blue, Colorate.Vertical, interval=0.035, enter=True)
webbrowser.open_new_tab("https://github.com/ZekromDev")

def aff():
    print(f"""{Fore.LIGHTRED_EX} 
_____  _____               _____   _____  _     _ _     _  _____ 
   |   |_____]      |      |     | |     | |____/  |     | |_____]
 __|__ |            |_____ |_____| |_____| |    \_ |_____| |      
                                                             By ZekromDev
        """)

    time.sleep(1)

def ip():
    Write.Print("\n[+] >> Enter an ip to lookup : ", Colors.white_to_blue, end='')
    ip_addr = input()
    print("\n")

    req1 = requests.get(f"http://ipinfo.io/{ip_addr}")
    req2 = requests.get(f"http://ip-api.com/json/{ip_addr}")
    req3 = requests.get(f"http://api.db-ip.com/v2/free/{ip_addr}")

    resp1 = req1.text
    resp2 = req2.text
    resp3 = req3.text

    Write.Print(f"[!] {resp3}", Colors.white_to_blue)
    print("\n")
    Write.Print(f"[!] {resp1}", Colors.white_to_blue)
    print("\n")
    Write.Print(f"[!] {resp2}", Colors.white_to_blue)
    print("\n")
    Write.Print("[#] Results will be deleted in 25s [#]", Colors.blue_to_white)
    time.sleep(25)
    os.system("clear || cls")
while True:
    aff()
    ip()
