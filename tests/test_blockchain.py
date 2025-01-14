import time

from blockchain.blockchain import Blockchain
from blockchain.block import Block

def test_blockchain_validity():
    blockchain = Blockchain()
    new_block = Block(1, blockchain.get_latest_block().hash, time.time(), "Test Data")
    blockchain.add_block(new_block)

    assert blockchain.is_chain_valid() == True
