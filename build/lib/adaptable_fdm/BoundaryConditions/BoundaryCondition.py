class BoundaryCondition:
    def __init__(self, name):
        self.name = name

    def apply(self,grid):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"BoundaryCondition: {self.name}"
