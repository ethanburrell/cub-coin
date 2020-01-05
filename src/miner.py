from block_structure import Block


async def main(index, difficulty, prevHash):
    #index, difficulty, iv, prevHash, timestamp, data
    b = Block(index, difficulty, 0, prevHash, "mining block")
    while True:
        if b.check_difficulty(difficulty):
            break
        b.struct.random_nonce()
    return b
