class HuffmanNode:
    def __init__(self, val=0, ch=None):
        self.value = val
        self.leftNode = None
        self.rightNode = None
        self.isLeaf = False
        self.char = ch
        if self.char is not None:
            self.isLeaf = True
