#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, httplib, sys, re, time, os
from platform import system

def slowprint(s):
	for c in s + '\n':
	    sys.stdout.write(c)
	    sys.stdout.flush()
	    time.sleep(2. / 100)


def banner12():
	print("""\033[95m
	                             _       _       _  ___ _ _____      
	   / \   _ __ ___   __ _ ___(_) __ _| |__   | |/ (_) |___ / _ __ 
	  / _ \ | '_ ` _ \ / _` |_  / |/ _` | '_ \  | ' /| | | |_ \| '__|
	 / ___ \| | | | | | (_| |/ /| | (_| | | | | | . \| | |___) | |   
	/_/   \_\_| |_| |_|\__,_/___|_|\__, |_| |_| |_|\_\_|_|____/|_|   
	                               |___/                             
			  
	                                  Script Name : Simple Recon ^_^
	                	Greetz To : \033[93mAll \033[92mNoobs  \033[91m|D\033[92mz| \033[91mHackerOne \033[92mResearchers
	                                     """)
	slowprint("\n\t\t\t\t\tPowered By : Trojan Kil3r Amazigh" + "\n\t\t\t\t\t\t            Contact Me : t.me/noobiste")
	print("""
		\033[1;92m[01] \033[1;91m~ \033[1;96mHosts Status Code Checker
		\033[1;92m[02] \033[1;91m~ \033[1;96mFast Sudomains Finder 
		\033[1;92m[03] \033[1;91m~ \033[1;96mNmap Scan Ports
	""")


def print_logo():
	print(b'\33]0;Powered By Trojan Kil3r Amazigh | Kabyle Hacker | Algeria Hacker |\a')
	print("""
		\033[1;91m		

		 █████╗ ███╗   ███╗ █████╗ ███████╗██╗ ██████╗ ██╗  ██╗    ██╗  ██╗██╗██╗     ██████╗ ██████╗ \033[1;92m
		██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██║██╔════╝ ██║  ██║    ██║ ██╔╝██║██║     ╚════██╗██╔══██╗ \033[1;93m	
		███████║██╔████╔██║███████║  ███╔╝ ██║██║  ███╗███████║    █████╔╝ ██║██║      █████╔╝██████╔╝ \033[1;94m	
		██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║██║   ██║██╔══██║    ██╔═██╗ ██║██║      ╚═══██╗██╔══██╗ \033[1;96m	
		██║  ██║██║ ╚═╝ ██║██║  ██║███████╗██║╚██████╔╝██║  ██║    ██║  ██╗██║███████╗██████╔╝██║  ██║ \033[1;95m	
		╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝\033[1;95m	

		\033[1;93m
	                                  Script Name : \033[1;91m| \033[1;92mM\033[1;93ma\033[1;96mt\033[1;95mo\033[1;96mu\033[1;91mb \033[1;92mL\033[1;93mo\033[1;96mu\033[1;95mn\033[1;94me\033[1;93ms\033[1;92m |  \033[1;93m^_^\033[1;96m
	                	Greetz To : \033[1;93mAll\033[0;92m\033[1;92m Noobs  \033[5;91m|D\033[5;92mz| \033[0;96m\033[1;96mHackerOne \033[1;92mResearchers
	""")
	slowprint("\t\t\t\t\tPowered By : Trojan Kil3r Amazigh " + "\n\t\t\t\t\t\t            Contact Me : t.me/noobiste")
	print("""
		\033[1;92m[01] \033[1;91m~ \033[1;96mHosts Status Code Checker
		\033[1;92m[02] \033[1;91m~ \033[1;96mFast Sudomains Finder 
		\033[1;92m[03] \033[1;91m~ \033[1;96mNmap Scan Ports
	""")

def clearscrn():
	if system() == 'Linux':
		os.system('clear')
		print_logo()
	if system() == 'Windows':
		os.system('cls')
		os.system('color a')
		os.system('title [+] Powered By Trojan Kil3r Amazigh Kabyle Hacker Algeria Hacker [+]')
		banner12()
clearscrn()

try:
	mama = int(raw_input("\033[1;93m[+] root@kil3r~# \033[1;93mChose Number: "))
except:
	print("\033[1;91m[-] Chose Number -_-")

def check():
	qaqa = raw_input("\t\033[1;94m[+] \033[1;92mEntre Your List Sub/Domains \033[1;95m: ")
	url = open(qaqa, 'r')
	for urls in url:
		urls = urls.rstrip()
		if urls[:7] == "http://":
			urls = urls.replace("http://","")
		if urls[:8] == "https://":
			urls = urls.replace("https://", "")
		if urls[-1] == "/":
			urls = urls.replace("/","")
		try:
			conn = httplib.HTTPConnection(urls, timeout=10)
			conn.request("HEAD", "")
			res = conn.getresponse()
			print ("\033[1;92m[+] \033[1;96m" + urls + '\t'),'\033[1;92m[',res.status, res.reason ,']'
		except:
			print("\033[1;91m[-] \033[1;91m" + urls), '\t \033[1;91m[Error Host] OR [You Slow Internet]'

def subfinder():
	url2 = "https://api.hackertarget.com/hostsearch/?q="
	dzdz = "http://api.hackertarget.com/nmap/?q="

	kok = raw_input("\n\033[1;93m\t [+] Entre Your Host/IP Without (www.): ")
	if kok[:7] == "http://":
		kok = kok.replace("http://","")
	if kok[:8] == "https://":
		kok = kok.replace("https://", "")
	if kok[-1] == "/":
		kok = kok.replace("/","")
	if mama == 2:
		try:
			opendz = requests.get(url2 + kok).content
			dz12 = re.findall('(.+?),', opendz)
			for i3 in dz12:
				i3 = i3.rstrip()
				print("\033[1;92m[+] \033[1;96m" + i3)
				with open(kok+'.txt','a') as s:
					s.writelines(i3 + '\n')
		except:
			pass
	elif mama == 3:
		print("\033[1;92m[+] Please Waiting To Scan Ports : \033[1;96m"), kok
		try:
			opendz = requests.get(dzdz + str(kok)).content
			print("\033[1;92m" + opendz)
		except:
			pass
	else:
		pass

def Run():
	if mama == 1:
		check()
	elif mama == 2:
		subfinder()
	elif mama == 3:
		subfinder()
	else:
		print("\033[1;91m[-] Ur Ass !!")
if __name__ == '__main__':
	Run()
