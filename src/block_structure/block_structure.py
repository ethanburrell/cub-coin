import hashlib
import json

class BlockStruct():
    def __init__(self, index, difficulty, iv, prevHash, timestamp, data):
        self.index = index
        self.difficulty = difficulty
        self.iv = iv
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.data = data

    def __dict__(self):
        return {
            "index": self.index,
            "difficulty": self.difficulty,
            "iv": self.iv,
            "prevHash": self.prevHash,
            "timestamp": self.timestamp,
            "data": self.data
        }

class Block():
    def __init__(self, index, difficulty, iv, prevHash, timestamp, data):
        block_struct = BlockStruct(index, difficulty, iv, prevHash, timestamp, data)
        #hashlib.sha224
        struct_hash = hashlib.sha256(block_struct)
        print(struct_hash)
        self.hash = struct_hash
        self.struct = block_struct

    def hash(self):
        sha256 = hashlib.sha256()
        sha256.update(dict(self.struct))
        #output = sha256.digest()
        output = sha256.hexdigest()
        return output

genesis_block = Block(0, 0, 0, 0, 0, b"asdf")
