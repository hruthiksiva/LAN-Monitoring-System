# LAN Monitoring System

## Introduction
The LAN Monitoring System is a network tool designed to monitor and manage client computers on a Local Area Network (LAN). This system facilitates monitoring, video streaming, IP blocking, and more through a graphical user interface (GUI) and command-line interface (CLI). It is a useful tool for network administrators and security personnel to maintain and secure the LAN environment.

## Features

### client_main.py
This module serves as the client-side component of the LAN Monitoring System. It includes the following functionalities:

1. **Video Streaming**: Captures the client's screen and streams the video to the server using the VidGear library.
2. **IP Blocking**: Blocks access to specific websites by modifying the client's hosts file.
3. **Client Connectivity**: Establishes a connection to the server, sends client information, and receives commands.

### gui-client.py
A graphical user interface (GUI) for the client-side of the LAN Monitoring System. This GUI provides a user-friendly way to interact with the system's functionalities, including:

1. **Peek into Client Screen**: Initiates video streaming from a selected client's screen.
2. **List Connected Clients**: Displays a list of clients connected to the LAN.
3. **Block IP**: Blocks access to a specific IP address or website on a client's computer.
4. **Allow IP**: Removes IP blocking for a specific IP address or website.
5. **Help**: Provides information about available commands.

### guiserver.py
The server-side GUI for the LAN Monitoring System. It enables administrators to manage and control connected clients using a graphical interface. Features include:

1. **List Connected Clients**: Displays a list of clients connected to the LAN.
2. **Peek into Client Screen**: Initiates video streaming from a selected client's screen.
3. **Block IP**: Blocks access to a specific IP address or website on a client's computer.
4. **Allow IP**: Removes IP blocking for a specific IP address or website.
5. **Help**: Provides information about available commands.
6. **Exit**: Closes the GUI and terminates the program.

## Usage
1. Run `client_main.py` on the client machines you want to monitor. Provide a name for the client and follow the on-screen instructions.
2. Run `guiserver.py` on the server machine to launch the server-side GUI.
3. Use the GUI to monitor and manage the connected clients, including video streaming and IP blocking.

## Requirements
Ensure the following dependencies are installed:

- `vidgear`: A powerful python library that provides various video & audio handling mechanisms.
- `socket`: A library for network communication.
- `cv2`: OpenCV library for video processing.
- `tkinter`: Python's standard GUI package.

## Future Enhancements
1. **Enhanced Security**: Implement stronger encryption and authentication mechanisms to secure communication between clients and server.
2. **Remote Command Execution**: Allow administrators to remotely execute commands on client machines.
3. **Real-Time Alerts**: Implement real-time notifications and alerts for specific events or triggers.
4. **User Authentication**: Add user authentication to ensure authorized access to the system.
5. **Improved GUI**: Enhance the GUI for a more intuitive and user-friendly experience.

## License
This project is open-source and provided under the [MIT License](LICENSE). Feel free to use, modify, and distribute it according to the terms of the license.
