# base_server.py
import socket
import threading
import requests

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


def handle_client(conn, addr):
    print(f"[+] Connected to: {addr}")

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
            send_data(conn, response)

        except Exception as e:
            print(f"[!] Error: {e}")
            break

    conn.close()

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
