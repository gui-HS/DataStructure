class ArestaDP:
    def __init__(self):
        self._prevEdge = None
        self._nextEdge = None
        self._EulerEdge = None

    # Getters
    def getPrevEdge(self):
        return self._prevEdge

    def getNextEdge(self):
        return self._nextEdge

    def getEulerEdge(self):
        return self._EulerEdge

    # Setters
    def setPrevEdge(self, edge):
        self._prevEdge = edge

    def setNextEdge(self, edge):
        self._nextEdge = edge

    def setEulerEdge(self, edge):
        self._EulerEdge = edge