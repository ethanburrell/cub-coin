#!/usr/bin/env python
import asyncio
import websockets
import json
import time
import sys
from p2pmessenger import ConnectionManager
from blockchain import Blockchain
from block_structure import Block

#cm = ConnectionManager("ws://localhost:9000")
genesis_block = Block(0, 0, 0, b'0', 1577836800, "Let's see what hash of this is")
bc = Blockchain(genesis_block)
#print(cm.peers)

async def eval_requests(websocket, path):
    #print(websocket.remote_address)
    async for message in websocket:
        #print(message.remote_address)
        data = json.loads(message)
        if "request" in data:
            if data["request"] == "peers":
                print("its a peers request")
                print(bc.chain)
                d = {"peers": ["ws://localhost:9000"], "chain": [i.to_dict() for i in bc.chain]}
                await websocket.send(json.dumps(d))
            elif data["request"] == "new block":
                print("it's a new block request")


        #await websocket.send(message)

def start_server():
    asyncio.get_event_loop().run_until_complete(websockets.serve(eval_requests, 'localhost', sys.argv[1]))
    asyncio.get_event_loop().run_forever()

start_server()
