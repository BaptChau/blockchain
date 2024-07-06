import json
import hashlib

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0) -> None:
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()
        self.nonce = nonce
        self.previous_hash = previous_hash
        
    def calculate_hash(self) -> str:
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
