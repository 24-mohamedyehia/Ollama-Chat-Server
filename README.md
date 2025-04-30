# Ollama-Chat-Server

A lightweight chat server that leverages Ollama (LLM API) to generate intelligent, conversational responses. Designed for easy local deployment and multi-client support, this project is ideal for experimenting with LLM chatbots or building custom chat applications.

---
## screenshots 
![](./static/Screenshot%202025-05-01%20020706.png)
---

## Features

- **Multi-client Chat Server:** Supports multiple concurrent clients via TCP sockets.
- **LLM-Powered Responses:** Integrates with Ollama for AI-generated replies.
- **Customizable System Prompt:** Define the assistant's personality and behavior.
- **Simple Python Clients:** Two ready-to-use client scripts for easy testing.

---

## Getting Started

### Prerequisites
- Python 3.10+
- miniconda
- Ollama

## Installation

### Install Python Using Miniconda
1. Download and install MiniConda from [here](https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)

2. Create a new environment using the following command:
```bash
conda create --name ollama_chat_server python=3.10 -y
```

3. Activate the environment:
```bash
conda activate ollama_chat_server
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Clone the repository:
```bash
git clone https://github.com/24-mohamedyehia/Ollama-Chat-Server.git
```


### Install Ollama
1. Download and install Ollama from [here](https://ollama.com/).

### Running the Server

1. **Start your Ollama server** (ensure the model specified in `src/base_server.py` is available).

2. **Run the chat server:**
   ```bash
   python src/base_server.py
   ```

### Running a Client

Open a new terminal and run either client:
```bash
python src/client_one.py
# or
python src/client_two.py
```

---

## Usage
- Type your message and press Enter.
- Type `exit` to end the session.
- The server will respond with an AI-generated reply, always in English, concise, and with emojis.

---

## Configuration
- **Model:** Change the `model_llm` variable in `src/base_server.py` to use a different Ollama model.
- **System Prompt:** Customize the `system_message` variable to alter the assistant's behavior.
- **Port:** The server listens on `localhost:12345` by default. Edit in `start_server()` if needed.
- **Environment:** Use the `.env` or `.env.example` files if you want to manage environment variables (not strictly required for default setup).

---

## Technologies Used
- Python (socket, threading, requests)
- Ollama (LLM server)
- colorama (for colored client output)

---

## License
This project is licensed under MIT License - see the [LICENSE](LICENSE) file in this repository.

---

## Acknowledgements
- [Ollama](https://ollama.com/) for the LLM API
- Developed by Mohamed Yehia
