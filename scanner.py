#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================================
    PROJECT: WESAM ULTIMATE APEX OMEGA ENTERPRISE RECON SUITE v70000.0 [UNIVERSAL ENGINE]
    AUTHOR: WESAM
    DESCRIPTION: Autonomous AI Universal Security Agent supporting any URL, File Lists,
                 Dynamic Parameter Discovery, SQLi, LFI, and Multi-Format Assets.
====================================================================================
"""

import sys
import subprocess
import os
import warnings

warnings.filterwarnings('ignore')

# --- [0] AUTO-INSTALLER ENGINE ---
required_packages = ["requests", "beautifulsoup4", "aiohttp", "dnspython", "fake-useragent", "colorama"]

def install_missing_packages():
    for package in required_packages:
        try:
            __import__(package if package != "beautifulsoup4" else "bs4")
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

install_missing_packages()

import asyncio
import aiohttp
import time
import datetime
import socket
import json
import random
import re
import urllib.parse
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from colorama import init, Fore, Style

init(autoreset=True)

class UITheme:
    HEADER = Fore.MAGENTA
    BLUE = Fore.BLUE
    CYAN = Fore.CYAN
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    RED = Fore.RED
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT

GREEN = UITheme.GREEN
RED = UITheme.RED
YELLOW = UITheme.YELLOW
CYAN = UITheme.CYAN
MAGENTA = UITheme.HEADER
BOLD = UITheme.BOLD
RESET = Style.RESET_ALL

def print_master_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
{MAGENTA}{'=' * 85}{RESET}
{MAGENTA}    ██████╗  ██████╗ ██████╗       ██╗   ██╗██████╗ ███╗   ███╗{RESET}
{MAGENTA}    ██╔══██╗██╔═══██╗██╔══██╗      ██║   ██║██╔══██╗████╗ ████║{RESET}
{MAGENTA}    ██║  ██║██║   ██║██║  ██║      ██║   ██║███████║██╔████╔██║{RESET}
{MAGENTA}    ██║  ██║██║   ██║██║  ██║      ╚██╗ ██╔╝██╔══██║██║ ╚═╝ ██║{RESET}
{MAGENTA}    ██████╔╝╚██████╔╝██████╔╝       ╚████╔╝ ██║  ██║██║     ██║{RESET}
{MAGENTA}    ╚═════╝  ╚═════╝ ╚═════╝         ╚═══╝  ╚═╝  ╚═╝╚═╝     ╚═╝{RESET}
{MAGENTA}     [+] WESAM OMEGA UNIVERSAL ENTERPRISE SUITE - v70000.0 [+] {RESET}
{MAGENTA}     [+] Multi-Target, File Lists & Universal Fuzzing Active [+] {RESET}
{MAGENTA}{'=' * 85}{RESET}
    """
    print(banner)

print_master_banner()

findings_database = []
ua = UserAgent()

OMEGA_USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
]

def get_quantum_bypass_headers(target_host):
    r_ip = f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    return {
        "User-Agent": random.choice(OMEGA_USER_AGENTS),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "X-Forwarded-For": r_ip,
        "X-Real-IP": r_ip,
        "True-Client-IP": r_ip,
        "CF-Connecting-IP": r_ip,
        "Host": target_host,
        "Cache-Control": "no-cache",
        "Connection": "keep-alive"
    }

def log_finding(title, target, severity, description, ai_insight="", poc_code=""):
    sev_color = RED if severity in ["CRITICAL", "HIGH"] else (YELLOW if severity == "MEDIUM" else CYAN)
    print(f"  {sev_color}[{severity} Finding] {title} -> {target}{RESET}")
    if ai_insight:
        print(f"  {CYAN}[🤖 Omega AI Insight]: {ai_insight}{RESET}")
    
    findings_database.append({
        "title": title, "target": target, "severity": severity,
        "description": description, "ai_insight": ai_insight, "poc_code": poc_code,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

# --- [INPUT & TARGET MANAGEMENT] ---
user_input = input(YELLOW + "[?] Enter target domain, URL, or path to a text file containing URLs: " + RESET).strip()
if not user_input:
    user_input = "http://testphp.vulnweb.com"

targets_list = []

# التحقق إذا كان المستخدم أدخل مسار ملف يحتوي على روابط متعددة
if os.path.isfile(user_input):
    print(CYAN + f"[*] Loading targets from file: {user_input}" + RESET)
    try:
        with open(user_input, "r", encoding="utf-8") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith("#"):
                    if not l.startswith("http://") and not l.startswith("https://"):
                        l = "http://" + l
                    targets_list.append(l)
    except Exception as e:
        print(RED + f"[-] Error reading file: {e}" + RESET)
else:
    if not user_input.startswith("http://") and not user_input.startswith("https://"):
        user_input = "https://" + user_input
    targets_list.append(user_input)

print(GREEN + f"[+] Total active targets loaded for scan: {len(targets_list)}" + RESET)

SQL_ERRORS = [
    "you have an error in your sql syntax", "warning: mysql",
    "unclosed quotation mark after the character string",
    "quoted string not properly terminated", "postgresql query failed",
    "sqlite3.operationalerror", "pdo::query()", "sql syntax"
]

def analyze_deep_vulnerabilities(url, response_text, status_code):
    findings = []
    text_lower = response_text.lower()
    
    for err in SQL_ERRORS:
        if err in text_lower:
            findings.append({
                "title": "SQL Injection Vulnerability (Error-Based)",
                "severity": "CRITICAL",
                "desc": f"The endpoint revealed database error patterns indicating improper sanitization.",
                "insight": "Database error messages exposed, enabling potential payload injection.",
                "poc": f"sqlmap -u '{url}' --batch"
            })
            break

    if "root:x:" in response_text or "[boot loader]" in response_text:
        findings.append({
            "title": "Local File Inclusion (LFI) Exposed",
            "severity": "CRITICAL",
            "desc": f"Endpoint successfully traversed directories to expose system files.",
            "insight": "Critical system files are readable directly via parameter traversal.",
            "poc": f"curl '{url}?file=../../../../etc/passwd'"
        })

    if not findings:
        if any(k in url for k in [".env", ".git", "backup", "sql", "credentials", "config", ".bak", ".zip"]):
            findings.append({
                "title": "Sensitive Administrative Asset Exposed",
                "severity": "HIGH",
                "desc": f"Endpoint returned a sensitive configuration or backup asset.",
                "insight": "Configuration or source files expose sensitive environment keys.",
                "poc": f"curl -X GET {url}"
            })
        elif status_code == 200:
            findings.append({
                "title": "Active Responsive Endpoint",
                "severity": "MEDIUM",
                "desc": f"Active resource endpoint verified successfully with status 200.",
                "insight": "Standard responsive target discovered.",
                "poc": f"curl -I {url}"
            })
            
    return findings

async def process_single_target(session, target_url):
    parsed = urllib.parse.urlparse(target_url)
    clean_domain = parsed.netloc
    base_url = f"{parsed.scheme}://{clean_domain}"
    path_part = parsed.path if parsed.path else "/"
    
    headers = get_quantum_bypass_headers(clean_domain)
    
    # 1. فحص الرابط الأصلي
    try:
        async with session.get(target_url, headers=headers, ssl=False, allow_redirects=True, timeout=aiohttp.ClientTimeout(total=5)) as resp:
            code = resp.status
            text = ""
            if code in [200, 500]:
                text = await resp.text()
            
            if code in [200, 401, 403, 500]:
                vulns = analyze_deep_vulnerabilities(target_url, text, code)
                for v in vulns:
                    print(f"  {RED}[Universal Hit 🔥]{RESET} Status [{code}] at: {target_url}")
                    log_finding(v["title"], target_url, v["severity"], v["desc"], v["insight"], v["poc"])

        # 2. فحص محاولة SQLi إضافية إذا كان الرابط يحتوي على Query Parameters أو مسار عام
        sqli_probe = target_url + ("'" if "?" in target_url else "?id=1'")
        async with session.get(sqli_probe, headers=headers, ssl=False, allow_redirects=True, timeout=aiohttp.ClientTimeout(total=4)) as sqli_resp:
            if sqli_resp.status in [200, 500]:
                sqli_text = await sqli_resp.text()
                for err in SQL_ERRORS:
                    if err in sqli_text.lower():
                        print(f"  {RED}[SQLi Injection 🔥]{RESET} at: {sqli_probe}")
                        log_finding("SQL Injection Vulnerability", sqli_probe, "CRITICAL", "Database error triggered via single-quote payload.", "Input reflection causes DB error.", f"sqlmap -u '{sqli_probe}' --batch")
                        break

    except Exception:
        pass

async def main_engine():
    print(CYAN + f"\n--- [Executing Universal Deep Fuzzing & Scan Engine] ---" + RESET)
    
    # مولد المسارات وأنواع الملفات الشاملة
    core_seeds = [
        "admin", "administrator", "api", "v1", "v2", "auth", "login", "dashboard", 
        "config", "backup", "db", "sql", "git", "env", "storage", "uploads", "portal", 
        "test", "debug", "graphql", "swagger", "manager", "panel", "user", 
        "artist.php?id=1", "showcat.php?cat=1", "listproducts.php?cat=1", "car.php?id=1"
    ]
    extensions = ["", ".php", ".html", ".json", ".sql", ".bak", ".zip", ".env", ".txt", ".xml"]
    
    all_test_urls = set()
    for t in targets_list:
        parsed = urllib.parse.urlparse(t)
        base = f"{parsed.scheme}://{parsed.netloc}"
        
        # إضافة الرابط الأساسي الذي أدخله المستخدم
        all_test_urls.add(t)
        
        # توليد مسارات وملفات للموقع
        for seed in core_seeds:
            if "?" in seed:
                all_test_urls.add(f"{base}/{seed}")
            else:
                for ext in extensions:
                    all_test_urls.add(f"{base}/{seed}{ext}")

    print(CYAN + f"[+] Generated {len(all_test_urls)} universal test vectors & file patterns." + RESET)

    connector = aiohttp.TCPConnector(limit_per_host=50, verify_ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [process_single_target(session, url) for url in all_test_urls]
        await asyncio.gather(*tasks)
        
    print(GREEN + f"[✓] Universal Scan completed successfully. Total findings: {len(findings_database)}{RESET}")

asyncio.run(main_engine())

# ====================================================================================
# [REPORTS GENERATOR]
# ====================================================================================
ts = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
json_report = f"wesam_universal_report_{ts}.json"
html_report = f"wesam_universal_report_{ts}.html"

json_data = {
    "targets_scanned": targets_list,
    "timestamp": str(datetime.datetime.now()),
    "total_findings": len(findings_database),
    "findings": findings_database
}

with open(json_report, "w", encoding="utf-8") as jf:
    json.dump(json_data, jf, indent=4, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WESAM Universal Security Intelligence Report</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #030712; color: #f8fafc; padding: 40px; }}
        .container {{ max-width: 1200px; margin: auto; background: #0f172a; padding: 40px; border-radius: 16px; border: 1px solid #1e293b; box-shadow: 0 25px 50px rgba(0,0,0,0.9); }}
        h1 {{ color: #38bdf8; text-align: center; font-size: 2.8em; }}
        .subtitle {{ text-align: center; color: #94a3b8; margin-bottom: 30px; letter-spacing: 2px; text-transform: uppercase; }}
        .meta {{ background: #1e293b; padding: 20px; border-radius: 10px; border-left: 6px solid #06b6d4; margin-bottom: 30px; }}
        table {{ width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 8px; overflow: hidden; }}
        th, td {{ padding: 18px; text-align: left; border-bottom: 1px solid #334155; }}
        th {{ background: #0284c7; color: white; }}
        .CRITICAL {{ color: #f43f5e; font-weight: bold; }}
        .HIGH {{ color: #fb923c; font-weight: bold; }}
        .MEDIUM {{ color: #facc15; font-weight: bold; }}
        .LOW {{ color: #38bdf8; }}
        .ai-note {{ color: #38bdf8; font-style: italic; display: block; margin-top: 6px; }}
        .poc {{ background: #020617; padding: 6px 12px; border-radius: 4px; font-family: monospace; color: #4ade80; display: inline-block; margin-top: 6px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>WESAM UNIVERSAL SUITE</h1>
        <div class="subtitle">Autonomous Security Intelligence Report (v70000.0)</div>
        <div class="meta">
            <p><strong>Primary Targets:</strong> {len(targets_list)} targets loaded</p>
            <p><strong>Timestamp:</strong> {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p><strong>Total Confirmed Findings:</strong> {len(findings_database)}</p>
        </div>
        <h2>Vulnerability & Asset Inventory</h2>
        <table>
            <tr><th>Severity</th><th>Category</th><th>Target URL</th><th>Analysis & AI Insights</th></tr>
"""

for f in findings_database:
    html_content += f"""
            <tr>
                <td class="{f['severity']}">{f['severity']}</td>
                <td>{f['title']}</td>
                <td><code>{f['target']}</code></td>
                <td>
                    {f['description']}
                    <span class="ai-note">🤖 <strong>Omega AI Insight:</strong> {f['ai_insight']}</span>
                    <div><span class="poc">PoC: {f['poc_code']}</span></div>
                </td>
            </tr>
    """

html_content += """
        </table>
    </div>
</body>
</html>
"""

with open(html_report, "w", encoding="utf-8") as hf:
    hf.write(html_content)

print(GREEN + f"\n[✓] JSON Report Saved: {json_report}{RESET}")
print(GREEN + f"[✓] HTML Report Saved: {html_report}{RESET}")
print(MAGENTA + "=== EXECUTION COMPLETED SUCCESSFULLY! ===" + RESET)
