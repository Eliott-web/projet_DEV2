class Path:
    def __init__(self):
        self._cases = None

    def __str__(self):
        return f"Path(cases='{self.listCases}')\n"

    @property
    def listCases(self):
        return self._cases