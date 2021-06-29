import datetime
import hashlib

class Block:
    def __init__(self, index, data, hashprevious):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.data = data
        self.hashprevious = hashprevious
        self.hash = self.caculateHash()

    def update(self, dic):
        self.__dict__ = dic
        return self

    def caculateHash(self):
        return hashlib.sha256(str(self.index).encode('utf-8')
                    + self.hashprevious.encode('utf-8')
                    + str(self.data).encode('utf-8')
                    + self.timestamp.encode('utf-8')).hexdigest()

    def isValid(self):
        return self.hash == self.caculateHash()

    def printBlock(self):
        return ("\nBlock #" + str(self.index)
                + "\nData: " + str(self.data)
                + "\nTimeStamp: " + str(self.timestamp)
                + "\nHash: " + str(self.hash)
                + "\nHashPrevious: " + str(self.hashprevious))




Blockchain = [print(Block(0, "Giao dịch 1", "000").printBlock())]

print(Blockchain)
# Blockchain.append(print(Block(1,"Hi i am Đông", Blockchain[len(Blockchain)-1].hash)))
#
# print(Blockchain)
