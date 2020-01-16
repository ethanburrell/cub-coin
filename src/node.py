#!/usr/bin/env python
import asyncio
import websockets
import json
import time
import sys
from p2pmessenger import ConnectionManager
from blockchain import Blockchain
from block_structure import Block, BlockConstructor

genesis_block = Block(0, 0, 0, b'0', 1577836800, "Let's see what hash of this is")
bc = Blockchain(genesis_block)
cm = ConnectionManager("ws://localhost:9000", bc)
print(bc.chain)
#print(cm.peers)

async def eval_requests(websocket, path):
    #print(websocket.remote_address)
    async for message in websocket:
        #print(message.remote_address)
        print(message)
        data = json.loads(message)
        if "request" in data:
            if data["request"] == "peers":
                print("its a peers request")
                print(bc.chain)
                d = {"peers": [""], "chain": [i.to_dict() for i in bc.chain]}
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
                        #self.call_action_on_clients_2(self.broadcast_block, new_block.to_dict())



        #await websocket.send(message)

def start_server():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(eval_requests, '127.0.0.1', sys.argv[1]))
    #asyncio.get_event_loop().run_until_complete(cm.mine(1, 1, genesis_block.hash))
    #cm.loop = loop
    cm.loop = loop
    cm.mine(1, 1, genesis_block.hash)
    loop.run_forever()
    #loop.get_event_loop().run_forever()

start_server()


"""

import cherrypy
from ws4py.server.cherrypyserver import WebSocketPlugin, WebSocketTool
from ws4py.websocket import EchoWebSocket

cherrypy.config.update({'server.socket_port': 9000})
WebSocketPlugin(cherrypy.engine).subscribe()
cherrypy.tools.websocket = WebSocketTool()

class Root(object):
    @cherrypy.expose
    def index(self):
        return 'some HTML with a websocket javascript connection'

    @cherrypy.expose
    def ws(self):
        # you can access the class instance through
        handler = cherrypy.request.ws_handler

cherrypy.quickstart(Root(), '/', config={'/ws': {'tools.websocket.on': True,
                                                 'tools.websocket.handler_cls': EchoWebSocket}})
"""
