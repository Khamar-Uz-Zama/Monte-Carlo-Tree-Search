import Nodee as nd

class Tree:
    
    def __init__(self,root=None):
        if root is None:
            self.root = nd.Nodee()
        else:
            self.root = root
    def getRoot(self):
        return self.root
    def setRoot(self,root):
        self.root = root
    def addChild(parent,child):
        parent.getChildArray().append(child)