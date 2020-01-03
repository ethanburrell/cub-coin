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

    def to_dict(self):
        return {
            'index': self.index,
            'difficulty': self.difficulty,
            'iv': self.iv,
            'prevHash': self.prevHash,
            'timestamp': self.timestamp,
            'data': self.data
        }
    def __dict__(self):
        return {
            'index': self.index,
            'difficulty': self.difficulty,
            'iv': self.iv,
            'prevHash': self.prevHash,
            'timestamp': self.timestamp,
            'data': self.data
        }

class Block():
    def __init__(self, index, difficulty, iv, prevHash, timestamp, data):
        block_struct = BlockStruct(index, difficulty, iv, prevHash, timestamp, data)
        #hashlib.sha224
        self.struct = block_struct
        struct_hash = self.hash()
        self.hash = struct_hash


    def hash(self):
        object_dict = self.struct.to_dict()
        print(object_dict)
        json_object = json.dumps(object_dict)
        struct_hash = hashlib.sha256(json_object.encode('utf-8')).digest()
        #print(struct_hash)
        return struct_hash

    def check_difficulty(self, difficulty):
        num_indicies = difficulty // 32
        num_bytes_leftover = difficulty % 8
        print("string", self.hash[0])
        c = 0
        flag = False
        for item in self.hash:
            byte = '{0:08b}'.format(item)
            print(byte)
            for i in byte:
                if i == '0':
                    c += 1
                else:
                    flag = True
                    break
            if flag:
                break
        return c == difficulty


# genesis_block = Block(0, 0, 0, 0, 1577836800, "Let's see what hash of this is")
# print(genesis_block.check_difficulty(2))
