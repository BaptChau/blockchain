from block import Block
from time import time

class Blockchain:
    def __init__(self) -> None:
        self.chain = [self.create_genesis_block()]
        self.difficulty = 10

    #methods that create the original block of the blockchain
    def create_genesis_block(self) -> Block:
        return Block(0, time(), "Genesis Block", "0")

    #methods get teh last block of the chain
    def get_last_block(self) -> Block:
        return self.chain[-1]
    
    def add_block(self, new_block) -> None:
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        
    def is_chain_valid(self) -> bool:
        for i in range (1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True