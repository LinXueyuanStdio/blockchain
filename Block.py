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
    
class Blockchain():
    def __init__(self):
        self.blocks = []
    
    def AddBlock(self, data):
        prevBlock = self.blocks[len(self.blocks)-1]
        newBlock = NewBlock(data, prevBlock.Hash)
        self.blocks.append(newBlock)
    
def NewGenesisBlock():
    return NewBlock("Genesis Block", "")

def NewBlockchain():
    bc = Blockchain()
    bc.blocks = [NewGenesisBlock()]
    return bc
    
def main():
	bc = NewBlockchain()

	bc.AddBlock("Send 1 BTC to Ivan")
	bc.AddBlock("Send 2 more BTC to Ivan")

	for block in bc.blocks:
		print("Prev. hash: %s"%(block.PrevBlockHash))
		print("Data: %s"%(block.Data))
		print("Hash: %s\n"%(block.Hash))

if __name__ == "__main__": 
    main()
