# client_one.py
import socket
from colorama import Fore, Style , init
init(autoreset=True)

def send_data(connection, message):
    connection.send(message.encode())

def receive_data(connection):
    return connection.recv(1024).decode()

if __name__ == '__main__':
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect(('localhost', 12345))

    print("Type a message to send to server (type 'exit' to quit):")
    while True:
        msg = input("> ").strip()
        if not msg:
            print("⚠️ Please type a message before sending.")
            continue
        send_data(connection, msg)
        if msg.lower() == "exit":
            break
        response = receive_data(connection)
        print(f"{Fore.GREEN}ChatGPT:\n{response}{Style.RESET_ALL}")

    connection.close()
