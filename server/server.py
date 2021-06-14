import socket
import os
import random
def list():
    string = ' '
    for dir in os.listdir():
        if '.' not in dir:
            string +='>   '+dir+'   '+str(os.path.getsize(dir))
        else:
            string += dir  +'   '+str(os.path.getsize(dir))
        string+='\n'
    return string

def pwd():
    path = os.getcwd()
    path = path[path.find('files')+len('files'):]+'/'
    return path


def cd_dirname(path):
    list_directoris = ['files','dir1','inner']
    current_path = pwd()
    if  path == '..':
        print('current path',current_path)
        if current_path=='/':
            print('file name rules violation from client :',addr)
            return 'Could not change directory!'
        else:
            os.chdir('..')
            x = pwd()
            s = f'Changing directory to : {x}'
            return s
    elif path in list_directoris:
        try:
            os.chdir(path)
            x = pwd()
            s = f'Changing directory to : {x}'
            return s
        except:
            print('Bad request!')
            return 'Could not change directory!'

    elif 'server/files' in path:
        try:
            os.chdir(path)
            x = pwd()
            s = f'Changing directory to : {x}'
            return s
        except:
            return 'Could not change directory!'
            print('Bad request!')
    else:
        print('file name rules violation from client :',addr)
        return 'Could not change directory!'

def dwld(file_path):
        new_port = random.randrange(3000,50000)
        new_serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_serversocket.bind(('127.0.0.1', new_port))
        new_serversocket.listen(5)

        connectionsocket.send(str(new_port).encode())
        new_connectionsocket, new_addr = new_serversocket.accept()
        try:
            f = open(file_path,'rb')
            l = f.read(2000000)

            new_connectionsocket.send(l)

            f.close()
            new_connectionsocket.close()
        except:
            print('incorrect file name!')

os.chdir('files')
serverport = 2121
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', serverport))
serversocket.listen(5)
print("server is listening...")

while True:
     connectionsocket , addr = serversocket.accept()
     msg = connectionsocket.recv(1024).decode()
     #connectionsocket.send('Client is connected to server!'.encode())
     print(msg)

     if msg == 'list':
         print(list())
         connectionsocket.send(list().encode())

     elif msg == 'pwd':
         print(pwd())
         connectionsocket.send(pwd().encode())
     elif 'cd' in msg:
         x = msg.replace('cd ', '')
         connectionsocket.send(cd_dirname(x).encode())
     elif 'dwld' in msg :
         x = msg.replace('dwld ', '')
         dwld(x)
