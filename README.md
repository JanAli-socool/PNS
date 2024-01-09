# Push Notification System

This project is a Push Notification System built using Python, FastAPI for the backend, and Streamlit for the frontend. It allows users to send push notifications to clients connected via WebSocket.

## Overview

The Push Notification System enables real-time communication between the server and connected clients using WebSocket technology. Clients can connect to the WebSocket endpoint, and the server can send push notifications to specific clients or broadcast messages to all connected clients.

### Features

- **WebSocket Communication:** Real-time bidirectional communication between the server and clients.
- **Client Registration:** Clients can connect to the WebSocket endpoint and register with a unique client ID.
- **Push Notifications:** Server can send push notifications to individual clients or broadcast messages to all clients.
- **Simple UI:** Streamlit frontend for testing and interacting with the Push Notification System.

## Setup

### Prerequisites

- Python 3.7 or higher
- Pip package manager

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/push-notification-system.git
    cd push-notification-system
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **On Linux/Mac:**

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI backend:**

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI server at http://localhost:8000.

2. **Open a new terminal and start the Streamlit frontend:**

    ```bash
    streamlit run app.py
    ```

    This will launch the Streamlit app at http://localhost:8501.

3. **Access the Streamlit app in your web browser to test and send push notifications.

## Usage

- **WebSocket Connection:** Connect to the WebSocket endpoint using a WebSocket client or script.
- **Client Registration:** Register with a unique client ID when connecting to the WebSocket.
- **Send Push Notifications:** Use the provided API endpoint to send push notifications to specific clients.
- **Broadcast Messages:** Broadcast messages to all connected clients.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
