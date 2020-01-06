import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')
from block_structure import Block
from blockchain import Blockchain

from utils import return_genesis_block
from freezegun import freeze_time

@freeze_time("01/03/2020 10:36:00")
def test_add_1_new_block():
    genesis_block = return_genesis_block()
    b = Block(1, 0, 213123123123123,
    b'2\x84\x0f\xf6<\x88\xeb\xbej\xcc\xa6C\x02\xc47\x89J!\x93\xf5\x14S\xc6<Y=\xe2?\xf3\xe5\xae\xa2',
    1577836800, "first block")
    # first of this is 10011100
    assert b.check_difficulty(0) == True, "Difficulty should be 0, aka 1 in the first place"

    assert b.validate_new_block(genesis_block) == True, "should validate"


@freeze_time("01/03/2020 10:36:00")
def test_add_new_block_to_chain():
    genesis_block = return_genesis_block()
    b = Block(1, 0, 213123123123123,
    b'2\x84\x0f\xf6<\x88\xeb\xbej\xcc\xa6C\x02\xc47\x89J!\x93\xf5\x14S\xc6<Y=\xe2?\xf3\xe5\xae\xa2',
    1577836800, "first block")
    # first of this is 10011100
    bc = Blockchain(genesis_block, b)
    bc_short = Blockchain(genesis_block, b)

    assert bc.validate_chain() == True, "Chain Doesn't Validate"

    b1 = Block(2, 0, 6477374,
    b'\x8a\x1c\x88T;\x86\x99\xe7i\xa1\xf9Y\x11\x9a\x9675\xd4^^ae+\x10h\x9f\x1f\x91{v\x99n',
    1577836845, "second block")

    assert b1.check_difficulty(0) == True, "still in first block of difficulty"

    bc.add(b1)

    assert bc.validate_chain() == True, "Chain Doesn't Validate"

    longer_chain = bc.chain

    new_blockchain = bc.resolve_via_length(bc_short)
    assert new_blockchain.chain == longer_chain, "The chain is not the longer one"

    new_chain = bc_short.resolve_via_length(bc)
    assert new_blockchain.chain == longer_chain, "The chain is not the longer one"

def init_chain():
    genesis_block = return_genesis_block()
    b = Block(1, 0, 213123123123123,
    b'2\x84\x0f\xf6<\x88\xeb\xbej\xcc\xa6C\x02\xc47\x89J!\x93\xf5\x14S\xc6<Y=\xe2?\xf3\xe5\xae\xa2',
    1577836800, "first block")
    # first of this is 10011100
    bc = Blockchain(genesis_block, b)

    b1 = Block(2, 0, 6477374,
    b'\x8a\x1c\x88T;\x86\x99\xe7i\xa1\xf9Y\x11\x9a\x9675\xd4^^ae+\x10h\x9f\x1f\x91{v\x99n',
    1577836845, "second block")

    bc.add(b1)

    return bc
