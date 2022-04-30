import socket
import threading
import re
import sys

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 1234))


# Listening to Server and Sending Nickname
def receive():
    while True:

        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if re.search('\/help', message):
                print('''USERS - Show all users in the ''')
            elif re.search('\/users', message):
                print('In users')
            elif re.search('\/dm', message):
                print('In DM')
            elif re.search('\/bc', message):
                # print('In BC')
                client.send(message.encode('ascii'))
            elif re.search('\/quit', message):
                client.close()
                # print('QUIT!')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break


# Sending Messages To Server
def write():
    while True:
        # message = '{}:{}'.format(nickname, input(''))
        message = input('{}: '.format(nickname))
        client.send(message.encode('ascii'))
        


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
