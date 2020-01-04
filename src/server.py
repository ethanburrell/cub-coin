#!/usr/bin/env python
import asyncio
import websockets
import json
import time

connected = set()
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

        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 9000))
asyncio.get_event_loop().run_forever()


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
