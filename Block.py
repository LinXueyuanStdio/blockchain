import time
import hashlib

class Block():
    def __init__(self):
        self.Timestamp = 0
        self.Data = ""
        self.PrevBlockHash = ""
        self.Hash = ""
    
    def SetHash(self):
        timestamp = int(self.Timestamp)
        headers = str(self.PrevBlockHash) + self.Data + str(timestamp)
        headers = headers.encode('utf-8')
        m = hashlib.sha256()
        m.update(headers)
        self.Hash = m.hexdigest()

def NewBlock(data, prevBlockHash):
    b = Block()
    b.Timestamp = int(time.time())
    b.Data = data
    b.PrevBlockHash = prevBlockHash
    b.SetHash()
    return b
    

