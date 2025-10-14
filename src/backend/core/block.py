class Block:
    """
    Block is a storage container that stores transactions.
    """

    def __init__(self, height, block_size, block_header, tx_count, txs):
        self.height = height
        self.block_size = block_size
        self.block_header = block_header
        self.tx_count = tx_count
        self.transactions = txs if txs is not None else []

    def __repr__(self):
        return f"Block(height={self.height}, block_size={self.block_size}, block_header={self.block_header}, tx_count={self.tx_count}, transactions={self.transactions})"
