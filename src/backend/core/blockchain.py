import sys

sys.path.append("/Users/Murtazo/Desktop/mxurramov/personal/demo-blockchain")

import time
from xml.etree.ElementTree import VERSION

from src.backend.core.block import Block
from src.backend.core.block_header import BlockHeader
from src.backend.core.database.database import BlockchainDB
from src.backend.util.util import hash_string

ZERO_HASH = "0" * 64
VERSION = 1  # noqa


class Blockchain:
    def __init__(self):
        self.genesis_block()

    def write_on_disk(self, block):
        db = BlockchainDB()
        db.create(block)

    def fetch_last_block(self):
        db = BlockchainDB()
        return db.last_block()

    def genesis_block(self):
        block_hight = 0
        prev_block_hash = ZERO_HASH
        self.add_block(block_hight, prev_block_hash)

    def add_block(self, block_height, prev_block_hash):
        timestamp = int(time.time())
        transaction = f"Codies Alert sent {block_height} BTC to Murtazo"
        merkle_root = hash_string(transaction.encode()).hex()
        bits = "1d00ffff"  # Difficulty target
        block_header = BlockHeader(
            version=VERSION,
            prev_block_hash=prev_block_hash,
            merkle_root=merkle_root,
            timestamp=timestamp,
            bits=bits,
        )
        block_header.mine()
        self.write_on_disk(
            [
                Block(
                    block_header=block_header.__dict__,
                    height=block_height,
                    block_size=1,
                    tx_count=1,
                    txs=transaction,
                ).__dict__
            ]
        )

    def main(self):
        while True:
            last_block = self.fetch_last_block()
            block_height = last_block["height"] + 1
            prev_block_hash = last_block["block_header"]["block_hash"]
            self.add_block(block_height, prev_block_hash)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()
