from blockchain.block import Block

def test_block_hash():
    block = Block(0, "0", 1234567890, "Genesis Block", 0)
    assert block.calculate_hash() == block.hash
    