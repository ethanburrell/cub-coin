import hashlib
import json
import base64

class BlockStruct():
    def __init__(self, index, difficulty, iv, prevHash, timestamp, data):
        self.index = index
        self.difficulty = difficulty
        self.iv = iv
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.data = data

    def to_dict(self):
        encoded = base64.b64encode(self.prevHash).decode('ascii')
        print("here", encoded)
        return {
            'index': self.index,
            'difficulty': self.difficulty,
            'iv': self.iv,
            'prevHash': encoded,
            'timestamp': self.timestamp,
            'data': self.data
        }
    def __dict__(self):
        encoded = base64.b64encode(self.prevHash).decode('ascii')
        return {
            'index': self.index,
            'difficulty': self.difficulty,
            'iv': self.iv,
            'prevHash': encoded,
            'timestamp': self.timestamp,
            'data': self.data
        }

class Block():
    def __init__(self, index, difficulty, iv, prevHash, timestamp, data):
        block_struct = BlockStruct(index, difficulty, iv, prevHash, timestamp, data)
        #hashlib.sha224
        self.struct = block_struct
        struct_hash = self.calc_hash()
        self.hash = struct_hash


    def calc_hash(self):
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

    def validate_new_block(self, prevBlock):
        if self.struct.index - 1 != prevBlock.struct.index:
            return False
        if self.struct.prevHash != prevBlock.hash:
        #self.struct.prevHash != prevBlock.struct.prevHash:
            return False
        if self.calc_hash() != self.hash:
            return False
        if not self.check_difficulty(self.struct.difficulty):
            return False
        return True

class BlockConstructor():
    def __init__(self):
        self.z = 0

    def unserialize(data):
        """
        Alternitave constructor
        """
        index = data["index"]
        difficulty = data["difficulty"]
        iv = data["iv"]
        prevHash = data["prevHash"]
        prevHashBytes =base64.b64decode(prevHash)
        #base64.b64encode(self.prevHash).decode('ascii')
        timestamp = data["timestamp"]
        block_data = data["data"]
        self.struct = BlockStruct(index, difficulty, iv, prevHashBytes, timestamp, block_data)
        #self.hash = self.calc_hash()
        return Block(index, difficulty, iv, prevHashBytes, timestamp, block_data)
