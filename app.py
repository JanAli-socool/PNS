# app.py

import streamlit as st
import requests
import threading
import asyncio

# Replace with your backend server URL
SERVER_URL = "http://localhost:8000"

st.title("Push Notification System")

client_id = st.text_input("Enter your client ID:")
message = st.text_input("Enter a message:")

# Streamlit is not designed to handle WebSocket connections, so we'll use threading and asyncio.
# The WebSocket connection will be handled in the background thread.
if st.button("Connect"):
    async def receive_notifications():
        try:
            async with st.websocket(f"{SERVER_URL}/ws/{client_id}") as ws:
                while True:
                    message = await ws.receive_text()
                    st.write(message)
        except Exception as e:
            st.error(f"Error: {e}")

    def background_task():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(receive_notifications())

    thread = threading.Thread(target=background_task)
    thread.start()

# Button to send a notification
if st.button("Send Notification"):
    response = requests.post(f"{SERVER_URL}/send_notification/{client_id}", data={"message": message})
    st.write(response.json())
