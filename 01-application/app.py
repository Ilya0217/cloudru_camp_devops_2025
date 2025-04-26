from fastapi import FastAPI
import socket
import os

app = FastAPI()

@app.get("/")
def get_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    author = os.getenv("AUTHOR", "Unknown")

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "author": author,
    }