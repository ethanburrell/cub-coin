import asyncio
import websockets
import json
import time
from concurrent.futures import ProcessPoolExecutor

#from blockchain import Blockchain
from block_structure import Block
#from server import start_server

class ConnectionManager:
    def __init__(self, first_address, bc, auto_connect = True):
        self.init_address = first_address
        self.bc = bc
        if auto_connect:
            asyncio.get_event_loop().run_until_complete(self.get_peers())
        else:
            self.peers = []
        self.loop=None

    def add_peer(self, peer):
        self.peers.append(peer)

    async def hello(uri):
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"request": ""}))
            response = await websocket.recv()

    async def get_peers(self):
        async with websockets.connect(self.init_address) as websocket:
            await websocket.send(json.dumps({"request": "peers"}))
            response = await websocket.recv()
            print(response)
            self.peers = json.loads(response)["peers"]
            temp_chain = json.loads(response)["chain"]
            self.bc.unserialize_blockchain(temp_chain)


    async def call_action_on_clients(self, f, *argv):
        list = [None] * len(self.peers)
        list = await asyncio.get_event_loop().run_until_complete(self.run_many_coroutines(f))

    async def call_action_on_clients_2(self, f, param):
        list = [None] * len(self.peers)
        #list = await asyncio.get_event_loop().run_until_complete(self.run_many_coroutines_2(f, param))
        #list = await self.loop.run_until_complete(self.run_many_coroutines_2(f, param))
        print("call_action_on_clients_2")
        list = self.loop.create_task(self.run_many_coroutines_2(f, param))

    async def broadcast_block(self, uri, data):
        async with websockets.connect(uri) as websocket:
            d = {"request": "new block"}
            d["data"] = data
            print("send to websocket", data)
            await websocket.send(json.dumps(d))
            #response = await websocket.recv()

    def mine(self, index, difficulty, prevHash):
        #index, difficulty, iv, prevHash, timestamp, data
        b = Block(index, difficulty, 0, prevHash, 4983934 ,"mining block")
        b.struct.random_nonce()
        while True:
            if b.check_difficulty(difficulty):
                print("asdf")
                break
            b.struct.random_nonce()
        print("done with this block")
        #asyncio.get_event_loop().create_task(self.call_action_on_clients_2(self.broadcast_block, b.to_dict()))
        self.loop.create_task(self.call_action_on_clients_2(self.broadcast_block, b.to_dict()))
        return b

    async def run_many_coroutines(self, f):
        input_coroutines = [f(i) for i in self.peers]
        #[f(argv[0])] * len(self.peers)
        res = await asyncio.gather(*input_coroutines, return_exceptions=True)
        return res

    async def run_many_coroutines_2(self, f, param):
        print("run_many_coroutines_2", f, param)
        input_coroutines = [f(i, param) for i in self.peers]
        print("input_coroutines", input_coroutines)
        #[f(argv[0])] * len(self.peers)
        res = await asyncio.gather(*input_coroutines, return_exceptions=True)
        print("after", self.peers)
        return res
#cm = ConnectionManager("ws://localhost:9000")
#print(cm.peers)
"""
async def multiple_tasks(dummy):
  input_coroutines = [get_peers(dummy), get_peers(dummy)]
  res = await asyncio.gather(*input_coroutines, return_exceptions=True)
  return res

res1, res2 = asyncio.get_event_loop().run_until_complete(multiple_tasks('ws://localhost:9000'))
res1, res2 = asyncio.get_event_loop().run_forever()
"""



# THE SERVER
"""
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
    websockets.serve(echo, 'localhost', 8999))
asyncio.get_event_loop().run_forever()
"""
