# Push Notification System

This project is a Push Notification System built using Python, FastAPI for the backend, and Streamlit for the frontend. It allows users to send push notifications to clients connected via WebSocket.

## Overview

The Push Notification System enables real-time communication between the server and connected clients using WebSocket technology. Clients can connect to the WebSocket endpoint, and the server can send push notifications to specific clients or broadcast messages to all connected clients.

### Features

- **WebSocket Communication:** Real-time bidirectional communication between the server and clients.
- **Client Registration:** Clients can connect to the WebSocket endpoint and register with a unique client ID.
- **Push Notifications:** Server can send push notifications to individual clients or broadcast messages to all clients.
- **Simple UI:** Streamlit frontend for testing and interacting with the Push Notification System.

## Deployment on Streamlit Cloud

The Push Notification System is deployed on Streamlit Cloud. You can access the live application and test its features by visiting the following link:

[![Open in Streamlit][([https://share.streamlit.io/your-username/push-notification-system/main/app.py](https://janali-socool-pns-app-wxhmij.streamlit.app/))](https://janali-socool-pns-app-wxhmij.streamlit.app/)

## Setup Locally

For local setup and development, follow the instructions in the [Setup](#setup) section of the README.

## Usage

- **WebSocket Connection:** Connect to the WebSocket endpoint using a WebSocket client or script.
- **Client Registration:** Register with a unique client ID when connecting to the WebSocket.
- **Send Push Notifications:** Use the provided API endpoint to send push notifications to specific clients.
- **Broadcast Messages:** Broadcast messages to all connected clients.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
