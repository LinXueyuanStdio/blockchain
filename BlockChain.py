from Block import *

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
