import socket

def HELP():
    print('Call one of the FTP client.')
    print('help\t\t',': show this help')
    print('list\t\t',': List files')
    print('pwd\t\t',': show current dir')
    print('cd\t\t',': Change directory')
    print('dwld file_path\t\t',': Download file')
    print('quit\t\t',': EXit')
    return

def dwld(file_path):

    new_port = clinetsocket.recv(1024).decode()
    new_clinetsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    new_clinetsocket.connect(('127.0.0.1', int(new_port)))
    with open(file_path,'wb') as f:
            while True:
                data = new_clinetsocket.recv(65000)
                if data:
                    f.write(data)
                else:
                    f.close()
                    break
    return


print('Welcome to FTP client!')
HELP()
command = ['list','pwd']
while True:
    clinetsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clinetsocket.connect(('127.0.0.1', 2121))
    input_str = input('Enter a command:')
    if input_str == 'quit':
        break
    elif input_str == 'help':
        HELP()
    elif 'dwld' in input_str:
        x = input_str.replace('dwld ', '')

        clinetsocket.send(input_str.encode())
        dwld(x)
    elif input_str in command:
        clinetsocket.send(input_str.encode())
        response = clinetsocket.recv(1024).decode()
        print(response)
    elif 'cd ' in input_str:
        clinetsocket.send(input_str.encode())
        response = clinetsocket.recv(1024).decode()
        print(response)
    else:
        print('incorrect command!')