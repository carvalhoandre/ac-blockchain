import time
from blockchain.block import Block
from blockchain.blockchain import Blockchain

if __name__ == "__main__":
    my_blockchain = Blockchain()
    block_length = 4

    print("Creating AC Blockchain...")
    print(my_blockchain.chain[0])

    # Add block
    for i in range(1,block_length):
        print(f"Mining block {i}...")
        new_block = Block(i, "", time.time(), f"Block data: {i}")
        my_blockchain.add_block(new_block)

    # showing all blocks
    print("\nAC Blockchain:")
    for block in my_blockchain.chain:
        print(block)

    #Validating the chain
    print("\nThe Blockchain is valid?", my_blockchain.is_chain_valid())
