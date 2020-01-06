#!/usr/bin/env python
import asyncio
import websockets
import json
import time
import sys
from p2pmessenger import ConnectionManager
from blockchain import Blockchain
from block_structure import Block, BlockConstructor
import ipaddress

genesis_block = Block(0, 0, 0, b'0', 1577836800, "Let's see what hash of this is")
bc = Blockchain(genesis_block)
cm = ConnectionManager("ws://localhost:9000", bc, auto_connect = False)
#print(cm.peers)

async def eval_requests(websocket, path):
    compressed_ipv6 = websocket.remote_address[0]
    port = str(websocket.remote_address[1])
    print(websocket.remote_address, ipaddress.IPv6Address(compressed_ipv6).exploded)
    full_address = ipaddress.IPv6Address(websocket.remote_address[0]).exploded
    cm.add_peer(full_address + ":" + port)
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
                print("new block is ", data["data"])
                if not data["data"]["index"] <= bc.length:
                    print("already seen this")
                else:
                    new_block = BlockConstructor().unserialize(data["data"])
                    #if new_block not in bc.chain:
                    if new_block.validate_new_block(bc.chain[-1]):
                        bc.add(new_block)
                        # TODO
                        # have my connection manager broadcast to peers
                        # minus this one
                        await cm.call_action_on_clients_2(cm.broadcast_block, new_block.to_dict())
                        #asyncio.ensure_future(cm.call_action_on_clients_2(cm.broadcast_block, new_block.to_dict()))
                        print(bc.chain, cm.peers)



        #await websocket.send(message)

def start_server():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(eval_requests, 'localhost', sys.argv[1]))
    #asyncio.get_event_loop().run_until_complete(cm.mine(1, 1, genesis_block.hash))
    cm.loop = loop
    #cm.mine(1, 1, genesis_block.hash)
    loop.run_forever()
    #asyncio.get_event_loop().run_forever()

start_server()

"""
import asyncio
import websockets
import json
import time
import sys
from p2pmessenger import ConnectionManager
from blockchain import Blockchain
from block_structure import Block, BlockConstructor
import
#cm = ConnectionManager("ws://localhost:9000")
genesis_block = Block(0, 0, 0, b'0', 1577836800, "Let's see what hash of this is")
bc = Blockchain(genesis_block)
#print(cm.peers)

async def eval_requests(websocket, path):
    print(websocket.remote_address)
    async for message in websocket:
        data = json.loads(message)
        if "request" in data:
            if data["request"] == "peers":
                print("its a peers request")
                print(bc.chain)
                d = {"peers": ["ws://localhost:9000"], "chain": [i.to_dict() for i in bc.chain]}
                await websocket.send(json.dumps(d))
            elif data["request"] == "new block":
                print("it's a new block request")
                print("new block is ", data["data"])
                if not data["data"]["index"] <= bc.length:
                    print("already seen this")
                else:
                    new_block = BlockConstructor().unserialize(data["data"])
                    #if new_block not in bc.chain:
                    if new_block.validate_new_block(bc.chain[-1]):
                        bc.add(new_block)
                        # TODO
                        # have my connection manager broadcast to peers
                        # minus this one





        #await websocket.send(message)

def start_server():
    asyncio.get_event_loop().run_until_complete(websockets.serve(eval_requests, 'localhost', sys.argv[1]))
    asyncio.get_event_loop().run_forever()

start_server()
"""
