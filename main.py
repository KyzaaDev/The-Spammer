import requests
import os
import colorama 
from colorama import Fore, Style, Back, init
import time
import argparse
from tqdm import tqdm

colorama.init(autoreset=True)

## digunakan untuk menampilkan banner
asciiBanner =  print(Fore.MAGENTA + r""" 
  ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓  ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░    ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░      ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░      ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
      ░  ░  ░  ░    ░ ░        ░                 ░    ░           ░  ░       ░                               
        """ + Fore.WHITE + "Made by: KyzaaDev\n")


## membuat parser untuk user
parser = argparse.ArgumentParser(description=asciiBanner, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("--url", type=str, required=True, help="Enter your URL here")
parser.add_argument("--loop", type=int, required=False, default=1, help="Enter the number of loops (default: 250)")
parser.add_argument("--delay", type=int, required=False,default=2, help="Enter the delay for each message (default: 2 second)")
args = parser.parse_args()

def validate_api():
    ## meminta dan melakukan validasi API yg dimasukkan user
    global urls
    urls = args.url

    if not urls.startswith("https://api.telegram.org/"):
        print(Fore.RED + "\n[!] Make sure your API is from telegram!")
        time.sleep(2)
        os.system('clear' if os.name == 'posix' else 'cls')
        exit()


## variable yg digunakna untuk menampung pesan dan jumlah req yg akan dikirim
messages = []   

## Fungsi yang digunakan untuk meminta pesan yang akan dikirim ke API
def get_user_messages():
    while True:
        add_messages = input(Fore.BLUE + "Input your messages here (q for stop): " + Style.RESET_ALL)

        if add_messages.lower() == "q":
            print(Fore.YELLOW + "\n[~] START SENDING MESSAGES!\n")
            break

        messages.append(add_messages)

def validate_input():
    errors = []
    
    if args.loop <= 0:
        errors.append("[!] The number of loops must be greater than 0.")
    if args.delay <= 0:
        errors.append("[!] Delay must be more than 0 seconds.")


    if errors:
        for err in errors:
            print(Fore.RED + err)
        exit()

## variable untuk menampung pesan berhasil dan gagal
success = 0
failed = 0

## memproses spamming
def sending_messsage(pesan):
    global success, failed

    pesan = pesan.replace(" ", "%20") 
    url = urls + pesan

    try:
        response = requests.post(url)
    except requests.exceptions.RequestException as e:
        tqdm.write(f"[!] Failed to sent messages: {e}")
        return

    tqdm.write(str(response.json()))

    if response.status_code == 200:
        tqdm.write(Fore.GREEN + f"[✓] Successfully sent the message!!. Status code: {response.status_code}\n")
        success += 1
    else:
        tqdm.write(Fore.RED + f"[✗] Failed to sent messages!!. Status code: {response.status_code}\n")
        failed += 1

    return response

## function yang melakukan looping spamming
def send_mess(jumReq=250):

    for i in tqdm(range(jumReq), desc="sending message", colour="magenta"):
        for message in messages:
            sending_messsage(message)
        time.sleep(args.delay)
                

    tqdm.write(Fore.MAGENTA + f"\n[✔ ] {success} Messages sent successfully")
    tqdm.write(Fore.RED + f"[✗] {failed} Message not sent successfully")
    tqdm.write(Fore.CYAN + "Thanks for using this tool!!")

def main():
    validate_api()
    validate_input()
    get_user_messages()
    
    while not messages:
        print("[!] Messages can not be blank")
        inputMess = input("Want to input messages first? (y/n): ").lower().strip()
        if inputMess in ["yes", "y"]:
            get_user_messages()
            send_mess(args.loop)
            return

        elif inputMess in ["no", "n"]:
            print("Bye Byee")
            return

        else: 
            print("Please enter 'y' or 'n'.")
            

    send_mess(args.loop)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram stoped by user")