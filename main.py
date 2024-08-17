from gettext import find
from re import split

import time,pyfiglet,webbrowser,requests

ASCII = pyfiglet.figlet_format("SPY IDE")
print(ASCII)

# Not done. A placeholder
InjectionStatus = 0


print("[+] spypie. All rights are reserved")
print("[+] Welcome to Spy IDE")
print("------------------")
print("[+] inject - 'Injects into Roblox process'")
print("[+] execute <string> - 'Executes provided script. use after injecting.'")
print("[+] httpget <string> - 'Executes script from website's content.'")
print("[+] discord - 'Opens our Discord in your browser.'")
print("------------------")

while 1==1:
	Cmd = str(input())
	
	if Cmd == "inject":
		print("Soon")
	elif Cmd == "discord":
		print("[+] Thank you for joining our community")
		webbrowser.open('https://discord.gg/JegzVs3ENV')
	elif Cmd.find("httpget") == 0:
		Splitted = Cmd.split(" ")
		print("[+] Getting body from " + Splitted[1] + "...")
		print(requests.get(Splitted[1]).content)
	else:
		print("[+] Unknown command '" + Cmd + "'.")
