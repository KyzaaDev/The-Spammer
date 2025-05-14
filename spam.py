import requests
import os
import colorama 
from colorama import Fore, Style, Back, init
import time
import argparse

colorama.init(autoreset=True)

## digunakan untuk menampilkan banner
def banner():
    print(Fore.MAGENTA + r"""
  _____ _          ___                                
 |_   _| |_  ___  / __|_ __  __ _ _ __  _ __  ___ _ _ 
   | | | ' \/ -_) \__ \ '_ \/ _` | '  \| '  \/ -_) '_|
   |_| |_||_\___| |___/ .__/\__,_|_|_|_|_|_|_\___|_|  
                      |_|                             
        """ + Fore.WHITE + "Made by: KyzaaDev\n")


## membuat parser untuk user
parser = argparse.ArgumentParser()
parser.add_argument("--url", type=str, required=True, help="Masukkan url disini")
parser.add_argument("--loop", type=int, required=False, default=1, help="Masukkan jumlah looping (default: 250)")
parser.add_argument("--delay", type=int, required=False,default=2, help="Masukkan delay setiap pesan (default: 2 detik)")
args = parser.parse_args()

def api():
    ## meminta dan melakukan validasi API yg dimasukkan user
    global urls
    urls = args.url

    if not urls.startswith("https://api.telegram.org/"):
        print(Fore.RED + "\n[!] Pastikan API kamu dari telegram!")
        time.sleep(2)
        os.system('clear' if os.name == 'posix' else 'cls')
        exit()


## variable yg digunakna untuk menampung pesan dan jumlah req yg akan dikirim
messages = []   

## Fungsi yang digunakan untuk meminta pesan yang akan dikirim ke API
def minta_pesan():
    while True:
        tambah_pesan = input(Fore.BLUE + "Masukkan pesan anda disini (quit untuk berhenti): " + Style.RESET_ALL)
        if tambah_pesan == "quit":
            print(Fore.YELLOW + "\n[~] MEMULAI PENGIRIMAN PESAN!\n")
            break
        messages.append(tambah_pesan)

## function untuk membuat variable yang memuat banyak looping
def loopAmount():
    global message_amount
    message_amount = args.loop

## function untuk memuat berapa delay setiap pesan
def delay():
    global dely
    dely = args.delay


def validate_input():
    errors = []
    if args.loop <= 0:
        errors.append("[!] Jumlah loop harus lebih dari 0.")
    if args.delay <= 0:
        errors.append("[!] Delay harus lebih dari 0 detik.")


    if errors:
        for err in errors:
            print(Fore.RED + err)
        exit()
## memproses spamming
def sendingMesssage(pesan):

    pesan = pesan.replace(" ", "%20") 
    url = urls + pesan

    try:
        response = requests.post(url)
    except requests.exceptions.RequestException as e:
        print(f"[!] Gagal mengirim pesan: {e}")
        return
   
    print(response.json())

    if response.status_code == 200:
        print(Fore.GREEN + f"[✓] Berhasil mengirimkan pesan!!. Status code: {response.status_code}\n")
    else:
        print(Fore.RED + f"[✗] Gagal mengirim pesan!!. Status code: {response.status_code}\n")

## function yang melakukan looping spamming
def send_mess(jumReq=250):
    try:
        for i in range(jumReq):
            for message in messages:
                sendingMesssage(message)
                time.sleep(dely)

        print(Fore.MAGENTA + "\n[✔ ] Semua pesan berhasil dikirim!")
        print(Fore.CYAN + "Terima kasih sudah menggunakan tools ini!!")
    except KeyboardInterrupt:
        print(Fore.RED + "\nProgram dihentikan oleh pengguna")                                                                                                           

#send_mess(message_amount)

if __name__ == "__main__":
    banner()
    api()
    loopAmount()
    delay()
    validate_input()
    minta_pesan()
    send_mess(message_amount)
