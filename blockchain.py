from hashlib import sha512
class Block:
    def __init__(self,id, data, p_hash):
        self.id=id 
        self.data = data
        self.p_hash = p_hash
        self.hash = sha512((str(id)+data+p_hash).encode()).hexdigest()
    
    def __str__(self):
        return '{}:::{};{}'.format(self.id,self.hash, self.data)

class Blockchain:
    def __init__(self):
        genesisBlock= Block(0,'Genesis','0*64')
        self.blocks=[genesisBlock]

    def append(self,data):
        self.blocks.append(
            Block(
                len(self.blocks),
                data,
                self.blocks[len(self.blocks)-1].hash
            )
        )
    def __str__(self) -> str:
        res= ''
        for block in self.blocks:
            res+='{}\n'.format(block)
        return res

bc=Blockchain()
bc.append('erste Blockchain4')
bc.append('3 block inder Blockchain')
print(bc)