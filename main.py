# main.py

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from typing import List
import uvicorn
import asyncio

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the static HTML file
app.mount("/", StaticFiles(directory="static", html=True), name="static")


# WebSocket manager to handle connections
class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def send_notification(self, message: str):
        for connection in self.connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_notification(f"Message from {client_id}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.send_notification(f"Client {client_id} disconnected")


# API endpoint to send push notifications
@app.post("/send_notification/{client_id}")
async def send_notification(client_id: str, message: str):
    await manager.send_notification(f"Notification for {client_id}: {message}")
    return {"message": "Notification sent"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
