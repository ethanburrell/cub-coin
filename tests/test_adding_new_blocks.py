import pytest

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src/')
from block_structure import Block

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
