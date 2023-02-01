import hashlib


class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        # A simple hash function to calculate the hash of a block
        return hashlib.sha256(str(self.data).encode() + str(self.previous_hash).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        # The first block in the blockchain
        return Block("Genesis block", "0")
    
    def add_block(self, data):
        previous_hash = self.chain[-1].hash
        block = Block(data, previous_hash)
        self.chain.append(block)
    
    def is_valid(self):
        # Validate the blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Initialize the blockchain
blockchain = Blockchain()

# Add blocks to the blockchain
blockchain.add_block("Block 1")
blockchain.add_block("Block 2")

# Validate the blockchain
if blockchain.is_valid():
    print("The blockchain is valid")
else:
    print("The blockchain is not valid")
