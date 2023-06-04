import asyncio
import logging

from jsonrpcclient import Error, Ok, parse_json, request_json
from websockets.client import connect


async def main() -> None:
    """Handle request"""
    async with connect("ws://localhost:2087") as socket:
        await socket.send(request_json("initialize"))
        response = parse_json(await socket.recv())

    if isinstance(response, Ok):
        print(response.result)
    elif isinstance(response, Error):
        logging.error(response.message)


async def run_server() -> None:
    """Run the server in the background"""
    # # server_process = subprocess.Popen(["pylsp", "--ws", "--port", "2087"])

    # try:
    #     # Wait for the server to start
    #     await asyncio.sleep(1)
    #     await asyncio.Event().wait()
    # finally:
    #     # Terminate the server process on shutdown
    #     # server_process.send_signal(signal.SIGINT)


async def start_program() -> None:
    """Start the server and the client program"""
    await asyncio.gather(run_server(), main())


asyncio.get_event_loop().run_until_complete(start_program())
