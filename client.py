import socket

#HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    #msg_length = len(message)
    #send_length = str(msg_length).encode(FORMAT)
    #send_length += b' ' * (HEADER - len(send_length))
    #client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


#input()
#send("Hello Everyone!")
#input()
#send("Hello Tim!")

#try:
#payload='Hey server'
send("hey server")
while True:
    more=input('Do you want to continue(y/n): ')
    if more.lower() =='y':
        payload= input('enter question: ')
        #print(payload)
        send(payload)
    else:
        send(DISCONNECT_MESSAGE)
        break
#except KeyboardInterrupt:
#    print('exited by the user')
#client.close()