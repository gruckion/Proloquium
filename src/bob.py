import json
import os
from threading import Thread

from pylsp_jsonrpc.streams import JsonRpcStreamReader, JsonRpcStreamWriter


def start_io_lang_server(reader, writer):
    # Implement your server logic here
    # This is just a sample implementation that echoes the received message

    def message_handler(message):
        if "method" in message:
            method = message["method"]
            if method == "textDocument/didOpen":
                # Handle the 'textDocument/didOpen' method
                # You can extract the necessary information from the message
                # and perform any required processing
                print("Received textDocument/didOpen method:", message)
                # Respond to the client if needed

    # Create a separate thread to read messages from the client
    def read_messages():
        while True:
            try:
                message = reader.read_message()
                if message is None:
                    return
                message_handler(message)
            except Exception as ex:
                print("Error reading message:", ex)
                return

    # Start the message reader thread
    read_thread = Thread(target=read_messages)
    read_thread.daemon = True
    read_thread.start()

    # Wait for the read thread to finish
    read_thread.join()

# Create a pair of pipes for communication
r, w = os.pipe()

# Wrap the pipes with JsonRpcStreamReader and JsonRpcStreamWriter
reader = JsonRpcStreamReader(os.fdopen(r, "r", encoding="utf-8"))
writer = JsonRpcStreamWriter(os.fdopen(w, "w", encoding="utf-8"))

# Start the server
start_io_lang_server(reader, writer)

# Send a message to the server to check if it's working
# Here, we're sending a 'textDocument/didOpen' method
request = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "textDocument/didOpen",
    "params": {
        "textDocument": {
            "uri": "file:///path/to/file.py",
            "languageId": "python",
            "version": 1,
            "text": 'print("Hello, server!")'
        }
    }
}

# Convert the request to a JSON string and write it to the output stream
request_str = json.dumps(request)
writer.write(request_str)
