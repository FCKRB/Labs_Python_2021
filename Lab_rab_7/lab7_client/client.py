import socket
import os

s = socket.socket()
HOST = '127.0.0.1'
PORT = 12345
s.connect((HOST, PORT))
while True:
    print("Input mail:")
    mail = input("C: ")

    s.send(mail.encode())
    answer = s.recv(1024).decode()
    if answer == "OK":
        print("S:", answer)
        break
    print("S:", answer)
print("Input message:")
message = input("C: ")
s.send(message.encode())
s.close()
