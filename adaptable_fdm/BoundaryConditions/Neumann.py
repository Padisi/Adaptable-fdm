import numpy as np
from .BoundaryCondition import BoundaryCondition

class Neumann(BoundaryCondition):
    """
    Class representing a Neumann boundary condition, which can be periodic in a specified direction.
    This condition relates the value at the boundary to the value at an adjacent coordinate.
    """

    def __init__(self, axis, wall, name):
        """
        Constructor for the Neumann class.

        Neumann boundary conditions require a coordinate where the system is periodic.
        The coordinate must be provided as an integer (coordinate position).

        :param axis: The coordinate axis (0 for x, 1 for y, 2 for z) where the Neumann condition is applied.
        :param wall: The wall index, which must be 0 or -1 to indicate the boundary.
        :param name: The name of the boundary condition for identification purposes.

        This method initializes the boundary condition and determines the next wall index.
        """
        super().__init__(name)  # Initialize the parent class with the boundary name
        self.coord = axis  # Coordinate axis for the Neumann condition
        self.wall = wall  # Wall index
        if wall == 0:
            self.next = 1
        elif wall == -1:
            self.next = -2
        else:
            raise ValueError(f"[Boundary Conditions] wall must be 0 or -1")
        print("[BoundaryConditions] " + str(self) + f" wall: {self.wall}")

    def _neumann_wall(self, array):
        """
        Move the selected coordinate to the first position and apply the periodic transformation.

        :param array: The array representing the grid data.
        :return: The transformed array with applied Neumann boundary condition.
        """
        array = np.moveaxis(array, self.coord, 0)  # Move the selected coordinate
        array[self.wall] = array[self.next]  # Apply the boundary condition
        return np.moveaxis(array, 0, self.coord)  # Move back the coordinate

    def apply(self, gridData):
        """
        Apply the Neumann boundary condition to the grid data.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the periodic boundary condition has been applied.
        """
        gridData.new_values = self._neumann_wall(gridData.new_values)  # Apply the Neumann wall transformation
        return "Applying Periodic boundary condition"

    def __str__(self):
        """
        Return a string representation of the Neumann boundary condition.

        :return: A string describing the boundary condition, including its name and coordinate.
        """
        return f"Periodic: {self.name}, coordinate: {self.coord}"


class NeumannFlatX(BoundaryCondition):
    """
    Class representing a flat Neumann boundary condition along the X-axis.
    This condition sets a zero derivative wall that is perpendicular to the X coordinate.
    """

    def __init__(self, height, cellSize, add, mask, name):
        """
        Constructor for the NeumannFlatX class.

        :param height: Position of the wall measured in terms of cellSize.
        :param cellSize: Unit of length in the system.
        :param add: Direction of the derivative from the wall (-1 or 1).
        :param mask: Mask for the perpendicular components. Domain of the plane.
        :param name: Name to differentiate the boundary condition.

        This method initializes the boundary condition and prints its representation.
        """
        super().__init__(name)  # Initialize the parent class with the boundary name
        self.h = int(np.ceil(height / cellSize)) - 1  # Calculate the wall index
        if self.h < 0:
            self.h = 0  # Ensure the index is non-negative
        if (add != -1) and (add != 1):
            raise ValueError("[BoundaryConditions] " + name + " add parameter must be -1 or 1")
        self.add = add  # Direction of the derivative
        self.mask = mask  # Mask for applying the condition
        print("[BoundaryConditions] " + str(self) + " boundary cell index = ", self.h)

    def apply(self, gridData):
        """
        Apply the flat Neumann boundary condition to the grid data.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the Neumann boundary condition has been applied.
        """
        gridData.new_values[self.h, :, :][self.mask[self.h, :, :]] = gridData.values[self.h + self.add, :, :][self.mask[self.h + self.add, :, :]]
        return f"Applying Neumann boundary condition with value"

    def __str__(self):
        """
        Return a string representation of the NeumannFlatX boundary condition.

        :return: A string describing the boundary condition, including its name.
        """
        return f"NeumannFlat: {self.name}"


class NeumannFlatY(NeumannFlatX):
    """
    Class representing a flat Neumann boundary condition along the Y-axis.
    This class inherits from NeumannFlatX and overrides the apply method for Y-axis specifics.
    """

    def apply(self, gridData):
        """
        Apply the flat Neumann boundary condition to the grid data along the Y-axis.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the Neumann boundary condition has been applied.
        """
        gridData.new_values[:, self.h, :][self.mask[:, self.h, :]] = gridData.values[:, self.h + self.add, :][self.mask[:, self.h + self.add, :]]
        return f"Applying Neumann boundary condition with value"


class NeumannFlatZ(NeumannFlatX):
    """
    Class representing a flat Neumann boundary condition along the Z-axis.
    This class inherits from NeumannFlatX and overrides the apply method for Z-axis specifics.
    """

    def apply(self, gridData):
        """
        Apply the flat Neumann boundary condition to the grid data along the Z-axis.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the Neumann boundary condition has been applied.
        """
        gridData.new_values[:, :, self.h][self.mask[:, :, self.h]] = gridData.values[:, :, self.h + self.add][self.mask[:, :, self.h + self.add]]
        return f"Applying Neumann boundary condition with value"
