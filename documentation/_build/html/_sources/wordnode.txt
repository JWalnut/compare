class wordnode:
    
    def __init__(self, text = ""):
        self.text = text
        self.neighbors = []

    def addNeighbor(self, theNode, distance=1):
        self.neighbors.append((theNode, distance))
