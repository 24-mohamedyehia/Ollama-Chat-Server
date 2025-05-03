# base_server.py
import socket
import threading
import requests
import os
import datetime

model_llm = "qwen2.5:1.5b-instruct-q3_K_L"

system_message = '\n'.join([
    "System Prompt:",
    "If user ask what is Your name? answer (my name is ChatGPT 🤖).",
    "If user ask what are create you? answer with the following (developed and created by Mohamed Yehia 😎.)",
    "You are a friendly and helpful assistant.",
    "Always reply ONLY in English.",
    "Speak clearly and simply, like you're talking to a friend.",
    "Always use different Emojis in your answers.",
    "Reply with short answer only.",
    "\nUser Message: "
])

def ask_ollama(prompt):
    url = "http://127.0.0.1:11434/api/generate"

    payload = {
        "model": model_llm,
        "prompt": system_message + prompt,
        "stream": False 
    }

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return "Error getting response from Ollama"
    
def log_chat(addr, user_msg=None, bot_response=None, event=None, error=None):
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_filename = datetime.datetime.now().strftime("logs/chat_log_%Y-%m-%d.txt")

    with open(log_filename, "a", encoding="utf-8") as log_file:
        if event:
            log_file.write(f"[{timestamp}] [{addr}] --- {event} ---\n")
        elif error:
            log_file.write(f"[{timestamp}] [ERROR] [{addr}] {error}\n")
        elif user_msg and bot_response:
            log_file.write(f"[{timestamp}] [{addr}] User: {user_msg}\n")
            log_file.write(f"[{timestamp}] [{addr}] Bot: {bot_response}\n\n")


def handle_client(conn, addr):
    print(f"[+] Connected to: {addr}")
    log_chat(addr, event="Session started")

    def send_data(connection, message):
        connection.send(message.encode())

    def receive_data(connection):
        return connection.recv(1024).decode()

    while True:
        try:
            message = receive_data(conn)
            print(f"[Client {addr}]: {message}")


            if message.lower() == "exit":
                send_data(conn, "👋 Goodbye!") 
                break

            response = ask_ollama(message)
            print(f"[Response {addr}]: {response}")
            send_data(conn, response)
            print("Logging chat...")
            log_chat(addr, message, response)

        except Exception as e:
            print(f"[!] Error: {e}")
            log_chat(addr, error=str(e))
            break

    conn.close()
    print(f"[-] Disconnected from {addr}")
    log_chat(addr, event="Session ended")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen()
    print("[*] Server listening...")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()


if __name__ == '__main__':
    start_server()

