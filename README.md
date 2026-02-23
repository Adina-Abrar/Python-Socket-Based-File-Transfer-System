# Python Socket-Based File Transfer System

##  Project Overview
This project implements a **Client–Server File Transfer System** using **Python Socket Programming**.  
It demonstrates fundamental concepts of **Data Communication and Networking (DCN)** by enabling reliable file transfer between systems over a network.

The system uses TCP sockets to establish a connection between a server and multiple clients, allowing users to send and receive files efficiently.

---

## Objectives
- To understand socket programming in Python  
- To implement a client–server architecture  
- To demonstrate reliable file transfer using TCP protocol  
- To apply DCN concepts in a practical networking application  

---

##  Features
-  Client–Server architecture  
-  Reliable file transfer using TCP  
-  Supports multiple clients  
-  Send and receive files over a network  
-  Efficient and simple communication  

---

##  Technologies Used
- **Python**
- **Socket Programming**
- **TCP/IP Protocol**
- **Client–Server Model**

---

##  DCN Concepts Implemented
This project demonstrates the following networking concepts:

- TCP/IP communication  
- Client–Server architecture  
- Data transmission over a network  
- Socket programming  
- Reliable file transfer  

---

##  Project Structure
server.py # Server program
client.py # Client program
files/ # Directory for transferred files
README.md # Project documentation


---

## How It Works

1. The server starts and listens for incoming client connections.  
2. The client connects to the server using IP address and port number.  
3. The client selects a file to send.  
4. The server receives the file and stores it in the designated directory.  
5. The connection closes after successful transfer.  

---

##  How to Run the Project

###  Step 1: Start the Server
```bash
python server.py
### Step 2: Run the Client
```bash
python client.py

### Enter Server Details

Provide the following information when prompted:

- **Server IP Address**
- **Port Number**
- **File Path to Send**
