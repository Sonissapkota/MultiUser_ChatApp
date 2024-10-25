# Multi-User Chat System

This project is a simple multi-user chat system built using Python's `socket` and `threading` modules. It consists of a server that handles multiple clients and allows them to communicate with each other in a group chat format.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Code Structure](#code-structure)
- [Possible Improvements](#possible-improvements)
- [License](#license)

## Features
- Real-time chat for multiple clients connected to a server.
- Broadcasts messages from one client to all others.
- Notifies all clients when a new user joins or leaves the chat.
- Uses threading to handle multiple clients concurrently.

## Requirements
- Python 3.x

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/multi-user-chat-system.git
   cd multi-user-chat-system
   ```
   
2. **Make sure you have Python 3 installed on your system.** You can check by running:
   ```bash
   python3 --version
   ```

3. **Install any necessary dependencies.**
   This project uses standard libraries (`socket`, `threading`), so no additional dependencies are required.

## Usage

### 1. Run the Server
Start the server by running the `server.py` file:
```bash
python3 server.py
```
The server will start listening on the host's IP and port `12345` (by default).

### 2. Run the Client
Start a client by running the `client.py` file in a new terminal window:
```bash
python3 client.py
```
- When prompted, enter your nickname.
- You can now start sending and receiving messages.

### 3. Multiple Clients
You can start multiple instances of `client.py` to simulate multiple users in the chat.

## How It Works
1. **Server:**
   - Accepts incoming connections and manages a list of connected clients.
   - Uses a separate thread for each connected client to handle their messages.
   - Broadcasts messages to all connected clients.
   - Handles client disconnection and notifies others when a client leaves the chat.

2. **Client:**
   - Connects to the server.
   - Sends the nickname to the server when prompted.
   - Can send messages to the chat, which will be broadcast to all other connected clients.
   - Receives messages from the server and displays them.

## Code Structure
- **`server.py`**: The server script that accepts connections, manages clients, and broadcasts messages.
- **`client.py`**: The client script that connects to the server and allows the user to chat with others.

### Key Functions

#### `server.py`
- **`broadcast_message(message)`**: Sends a message to all connected clients.
- **`receive_message(client_socket)`**: Listens for messages from a specific client and handles disconnections.
- **`connect_client()`**: Accepts new client connections and starts a new thread for each client.

#### `client.py`
- **`send_message()`**: Sends user input to the server.
- **`receive_message()`**: Listens for incoming messages from the server.

## Possible Improvements
- **Private Messaging**: Add support for private messages between users.
- **Encryption**: Implement message encryption for secure communication.
- **GUI**: Create a graphical user interface (GUI) using a library like `Tkinter` or `PyQt`.
- **Database Integration**: Add a backend database to log messages or support user authentication.
- **Better Error Handling**: Improve the code to handle socket errors and disconnections more gracefully.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
