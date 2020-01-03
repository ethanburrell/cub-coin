import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')
from block_structure import Block


def return_genesis_block():
    genesis_block = Block(0, 0, 0, b'0', 1577836800, "Let's see what hash of this is")
    #Block(0, 0, 0, 0, 1577836800, "Let's see what hash of this is")
    return genesis_block
