import json
import os


class BaseDB:
    def __init__(self):
        self.base_path = "data"
        self.file_path = "/".join((self.base_path, self.filename))

    def read(self):
        if not os.path.exists(self.file_path):
            print(f"File {self.file_path} does not exist.")
            return False

        with open(self.file_path, "r") as f:
            raw = f.readline()

        if len(raw) > 0:
            data = json.loads(raw)
        else:
            data = []
        return data

    def create(self, item):
        data = self.read()
        if data:
            data = data + item
        else:
            data = item

        with open(self.file_path, "w") as f:
            f.write(json.dumps(data))

    def delete(self, item_id):
        pass


class BlockchainDB(BaseDB):
    def __init__(self):
        self.filename = "blockchain"
        super().__init__()

    def last_block(self):
        data = self.read()
        if data:
            return data[-1]
        return None
