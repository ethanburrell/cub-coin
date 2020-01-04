import asyncio
import websockets
import json
import time
from concurrent.futures import ProcessPoolExecutor

from blockchain import Blockchain
from block_structure import Block

class ConnectionManager:
    def __init__(self, first_address):
        self.init_address = first_address
        get_peers(first_address)

    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"asdf":1}))
            response = await websocket.recv()

    async def get_peers(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"request": "peers"}))
            response = await websocket.recv()
            print(response)
            self.peers = json.endcode(response)["peers"]

    async def run_many_coroutines(f):
        input_coroutines = [f(i) for i in self.peers]
        #[f(argv[0])] * len(self.peers)
        res = await asyncio.gather(*input_coroutines, return_exceptions=True)
        return res

    def call_action_on_clients(self, f, *argv):
        list = [None] * len(self.peers)
        list = asyncio.get_event_loop().run_until_complete(run_many_coroutines(hello))

    async def rebroadcast_block(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"asdf":1}))
            response = await websocket.recv()


"""
async def multiple_tasks(dummy):
  input_coroutines = [get_peers(dummy), get_peers(dummy)]
  res = await asyncio.gather(*input_coroutines, return_exceptions=True)
  return res

res1, res2 = asyncio.get_event_loop().run_until_complete(multiple_tasks('ws://localhost:9000'))
res1, res2 = asyncio.get_event_loop().run_forever()
"""

# THE SERVER

async def echo(websocket, path):
    connected.add(websocket)
    async for message in websocket:
        print(message)
        data = json.loads(message)
        if "request" in data:
            if data["request"] == "peers":
                print("its a peers request")
                await websocket.send("ws://localhost:9000")
                time.sleep(5)
                await websocket.send("hello")
            elif data["request"] == "new block":
                print("it's a new block request")
                

        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 9000))
asyncio.get_event_loop().run_forever()
