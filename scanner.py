#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================================
    PROJECT: WESAM ULTIMATE APEX OMEGA ENTERPRISE RECON SUITE - FREE EDITION
    AUTHOR: WESAM
    DESCRIPTION: Limited free scanner with intentional bugs, low performance,
                 and restricted payloads. Upgrade to Pro for full power!
====================================================================================
"""

import sys
import subprocess
import os
import warnings
import asyncio
import aiohttp
import time
import datetime
import urllib.parse
from colorama import init, Fore, Style

warnings.filterwarnings('ignore')
init(autoreset=True)

# مكتبات محدودة عمداً بالنسخة المجانية
required_packages = ["requests", "colorama"]

def install_missing_packages():
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_missing_packages()

GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
MAGENTA = Fore.MAGENTA
RESET = Style.RESET_ALL

def print_banner():
    print(f"""
{YELLOW}{'=' * 60}{RESET}
{YELLOW}    [!] WESAM RECON SUITE - FREE EDITION [!] {RESET}
{YELLOW}    [!] Limited Version - Bugs & Restrictions Active [!] {RESET}
{YELLOW}{'=' * 60}{RESET}
    """)

print_banner()

user_input = input(YELLOW + "[?] Enter target URL (Free version takes 1 target only): " + RESET).strip()
if not user_input:
    user_input = "http://testphp.vulnweb.com"

if not user_input.startswith("http://") and not user_input.startswith("https://"):
    user_input = "http://" + user_input

print(RED + "[-] FREE LIMITATION: Multi-target file lists are disabled in this version!" + RESET)
print(CYAN + f"[*] Scanning single target: {user_input} (Slow mode)..." + RESET)

# أخطاء متعمدة بالبحث وبطء بالاستجابة
SQL_ERRORS = ["sql syntax"]

async def free_scan():
    async with aiohttp.ClientSession() as session:
        try:
            # بطء متعمد بالوقت
            await asyncio.sleep(2)
            async with session.get(user_input, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                print(f"[{resp.status}] Target checked.")
                if resp.status == 200:
                    print(YELLOW + "[!] Free Notice: Upgrade to PRO version (@mgjp519) to reveal hidden SQLi and LFI vulnerabilities!" + RESET)
        except Exception as e:
            print(RED + f"[-] Scan failed due to intentional free-version error: {e}" + RESET)

asyncio.run(free_scan())
print(MAGENTA + "\n=== FREE SCAN COMPLETED. WANT MORE POWER? CONTACT @mgjp519 ===" + RESET)
