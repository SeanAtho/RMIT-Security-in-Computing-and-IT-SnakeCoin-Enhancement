import hashlib
import datetime

class Block:
    """Defines the structure of a block in the blockchain."""

    def __init__(self, index, timestamp, data, previous_hash):
        """Initializes the block with index, timestamp, data, previous_hash."""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        """Generates the hash for the block using SHA256."""
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    """Creates the first block, called the genesis block."""
    return Block(0, datetime.datetime.now(), "Genesis Block", "0")

def next_block(last_block):
    """Creates the next block in the blockchain."""
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = f"Hey! I'm block {str(this_index)}"
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

num_of_blocks_to_add = 20  # Number of blocks to add to the chain after the genesis block

for _ in range(num_of_blocks_to_add):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print(f"Block #{block_to_add.index} has been added to the blockchain!")
    print(f"Hash: {block_to_add.hash}\n")
