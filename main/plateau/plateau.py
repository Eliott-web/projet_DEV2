class Plateau:
    def __init__(self):
        self._path = []

    def __str__(self):
        return f"Plateau(path='{self.getPathArray}')\n"

    # Setters

    def addPath(self, path):
        self.setPathArray(self.getPathArray + [path])

    def setPathArray(self,path): ## !!! Ca doit être un array
        self._path = path

    # Getters

    @property
    def getPathArray(self):
        return self._path