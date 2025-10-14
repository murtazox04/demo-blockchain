from src.backend.util.util import hash_string


class BlockHeader:
    def __init__(self, version, prev_block_hash, merkle_root, timestamp, bits):
        self.version = version
        self.prev_block_hash = prev_block_hash
        self.merkle_root = merkle_root
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = 0  # Nonce is initialized to 0
        self.block_hash = ""  # Block hash is initialized to an empty string

    def __repr__(self):
        return (
            f"BlockHeader(version={self.version}, prev_block_hash={self.prev_block_hash}, "
            f"merkle_root={self.merkle_root}, timestamp={self.timestamp}, bits={self.bits})"
        )

    def mine(self):
        while self.block_hash[0:4] != "0000":
            self.block_hash = hash_string(
                f"{self.version}{self.prev_block_hash}{self.merkle_root}{self.timestamp}{self.bits}{self.nonce}".encode()
            ).hex()
            self.nonce += 1
            print(f"Mining started {self.nonce}", end="\r")
