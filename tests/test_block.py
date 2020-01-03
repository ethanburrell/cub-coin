# some_file.py
# import sys
# import os
# # insert at 1, 0 is the script path (or '' in REPL)
# #sys.path.insert(1, '../src')
# sys.path.append(os.path.join(os.path.dirname( __file__ ), '..', '/src'))
# print(sys.path, os.path.join(os.path.dirname( __file__ ), '..', '/src'))

import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')
from block_structure import Block


def gensis_block_test():
    genesis_block = Block(0, 0, 0, 0, 1577836800, "Let's see what hash of this is")
    print(genesis_block.check_difficulty(2))
    assert genesis_block.check_difficulty(2) == True, "Difficulty and 0s did not match"
    assert genesis_block.check_difficulty(3) == False, "Difficulty and 0s did not match"
    assert genesis_block.check_difficulty(1) == False, "Difficulty and 0s did not match"
    assert genesis_block.check_difficulty(1) == False, "Difficulty and 0s did not match"


gensis_block_test()
#other()
