#!/usr/bin/env python
import asyncio
import websockets
import json
from concurrent.futures import ProcessPoolExecutor

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
            poll_until_next()



async def poll_until_next():
    async with websockets.connect(uri) as websocket:
        response = await websocket.recv()


async def get_peers(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({"request": "peers"}))
        response = await websocket.recv()
        print(response)
        self.peers = json.endcode(response)["peers"]
        poll_until_next()

async def multiple_tasks(dummy):
  input_coroutines = [get_peers(dummy), get_peers(dummy)]
  res = await asyncio.gather(*input_coroutines, return_exceptions=True)
  return res

res1, res2 = asyncio.get_event_loop().run_until_complete(multiple_tasks('ws://localhost:9000'))
res1, res2 = asyncio.get_event_loop().run_forever()


"""
from ws4py.client import WebSocketBaseClient
from ws4py.manager import WebSocketManager
from ws4py import format_addresses, configure_logger
import time
logger = configure_logger()

m = WebSocketManager()

print(m)
class EchoClient(WebSocketBaseClient):
    def handshake_ok(self):
        #logger.info("Opening %s" % format_addresses(self))
        m.add(self)

    def received_message(self, msg):
        #logger.info(str(msg))
        print(str(msg))




for i in range(5):
    client = EchoClient('ws://localhost:9000')
    client.connect()
print(m)
m.run()
#m.join()
logger.info("%d clients are connected" % i)
time.sleep(3)
m.broadcast("hi")
"""
"""
if __name__ == '__main__':
    import time
    print("ih")
    try:
        m.start()
        for i in range(5):
            client = EchoClient('ws://localhost:9000')
            client.connect()
        m.join()
        logger.info("%d clients are connected" % i)
        m.broadcast("hi")
"""
"""
        while True:
            for ws in m.websockets.itervalues():
                if not ws.terminated:
                   break
            else:
                break
            time.sleep(3)
"""
"""
    except KeyboardInterrupt:
        m.close_all()
        m.stop()
        m.join()
"""


"""
asyncio.get_event_loop().run_until_complete(
    [hello('ws://localhost:8765'),
    hello('ws://localhost:8765')]
    )
"""
