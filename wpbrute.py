# ... (import dan warna tetap sama)
import requests
import re
import os
import time
import sys

# Warna
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Animasi teks
def ketik(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ASCII Art
ascii_art = f"""{GREEN}
██╗    ██╗██████╗ ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██║    ██║██╔══██╗██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██║ █╗ ██║██████╔╝██████╔╝██████╔╝██║   ██║   ██║   █████╗  
██║███╗██║██╔═══╝ ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  
╚███╔███╔╝██║     ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
 ╚══╝╚══╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
{YELLOW}WordPress Bruteforce by LangitDev{RESET}
"""

# Tampilkan menu utama
def menu_awal():
    print(f"\n{BLUE}=== MENU UTAMA ==={RESET}")
    print(f"{YELLOW}[1]{RESET} Mulai Bruteforce")
    print(f"{YELLOW}[2]{RESET} Lihat Info Tools")
    print(f"{YELLOW}[3]{RESET} Keluar")

    while True:
        pilihan = input(f"{YELLOW}[?] Pilih menu: {RESET}")
        if pilihan in ['1', '2', '3']:
            return pilihan
        else:
            print(f"{RED}[!] Pilihan tidak valid. Coba lagi.{RESET}")

# Info tools
def info_tools():
    print(f"\n{GREEN}📄 Info Tools:{RESET}")
    print(f"Nama       : LangitDev WP Bruteforce")
    print(f"Versi      : 1.0")
    print(f"Author     : LangitDev")
    print(f"Fungsi     : Menemukan username dan mencoba bruteforce login WordPress.")
    input(f"\n{YELLOW}Tekan Enter untuk kembali ke menu...{RESET}")

# (Fungsi get_usernames, pilih_username, bruteforce_wp tetap sama)

# Main logic
if __name__ == "__main__":
    os.system("clear")
    ketik(f"{YELLOW}🔐 Starting WordPress Bruteforce Tool by LangitDev...\n{RESET}", delay=0.03)
    time.sleep(0.5)
    print(ascii_art)

    while True:
        pilihan = menu_awal()

        if pilihan == '1':
            target_url = input(f"{YELLOW}Masukkan URL target (contoh: https://example.com): {RESET}")
            password_file = input(f"{YELLOW}Masukkan path file password list: {RESET}")

            print(f"\n{BLUE}[🔎] Mencari username...{RESET}")
            usernames_ditemukan = get_usernames(target_url)

            username_terpilih = pilih_username(usernames_ditemukan)

            if username_terpilih:
                print(f"\n{GREEN}[🚀] Memulai brute-force dengan username: {username_terpilih}{RESET}")
                bruteforce_wp(target_url, username_terpilih, password_file)
            else:
                print(f"{RED}[❌] Tidak ada username yang bisa digunakan.{RESET}")
        elif pilihan == '2':
            info_tools()
        elif pilihan == '3':
            print(f"{BLUE}Terima kasih telah menggunakan tools ini!{RESET}")
            break
