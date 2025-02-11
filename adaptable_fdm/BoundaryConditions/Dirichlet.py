import numpy as np
from .BoundaryCondition import BoundaryCondition

class Dirichlet(BoundaryCondition):
    """
    Class representing a Dirichlet boundary condition for a simulation.

    This boundary condition sets specified values on a defined region of the grid
    based on a mask.
    """

    def __init__(self, mask, value, name):
        """
        Constructor for the Dirichlet class.

        :param mask: A boolean array or index array indicating the grid points to which
                     the boundary condition will be applied.
        :param value: The value to set at the specified boundary points.
        :param name: The name of the boundary condition for identification purposes.

        This method initializes the boundary condition and prints its representation.
        """
        super().__init__(name)  # Initialize the parent class with the boundary name
        self.value = value  # Value to set at the boundary
        self.mask = mask  # Mask indicating where to apply the boundary condition
        print("[BoundaryConditions] " + str(self))  # Print the boundary condition details

    def apply(self, gridData):
        """
        Apply the Dirichlet boundary condition to the grid data.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the boundary condition has been applied.
        """
        gridData.new_values[self.mask] = self.value  # Set the boundary condition value in the grid
        return f"Applying Dirichlet boundary condition with value {self.value}"

    def __str__(self):
        """
        Return a string representation of the Dirichlet boundary condition.

        :return: A string describing the boundary condition, including its name and value.
        """
        return f"Dirichlet: {self.name}, value={self.value}"
