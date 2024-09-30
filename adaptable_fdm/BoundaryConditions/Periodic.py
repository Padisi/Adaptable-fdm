import numpy as np
from .BoundaryCondition import BoundaryCondition

class Periodic(BoundaryCondition):
    """
    Class representing a periodic boundary condition for a simulation.
    This boundary condition links the values at the edges of the domain,
    creating a continuous loop in the specified coordinate direction.
    """

    def __init__(self, coordinate, name):
        """
        Constructor for the Periodic class.

        Periodic boundary conditions require a coordinate where the system is periodic.
        The coordinate must be provided as an integer (coordinate position).

        :param coordinate: The coordinate axis (0 for x, 1 for y, 2 for z) where the periodic condition is applied.
        :param name: The name of the boundary condition for identification purposes.

        This method initializes the boundary condition and prints its representation.
        """
        super().__init__(name)  # Initialize the parent class with the boundary name
        self.coord = coordinate  # Coordinate axis for the periodic condition
        print("[BoundaryConditions] " + str(self))  # Print the boundary condition details

    def _periodic_axis(self, array):
        """
        Move the selected coordinate to the first position and apply the periodic transformation.

        :param array: The array representing the grid data.
        :return: The transformed array with applied periodic boundary condition.
        """
        array = np.moveaxis(array, self.coord, 0)  # Move the selected coordinate to the front
        array[0] = array[-2]  # Set the first element to the second-to-last
        array[-1] = array[1]  # Set the last element to the second
        return np.moveaxis(array, 0, self.coord)  # Move back the coordinate

    def apply(self, gridData):
        """
        Apply the periodic boundary condition to the grid data.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the periodic boundary condition has been applied.
        """
        gridData.newPhi = self._periodic_axis(gridData.newPhi)  # Apply the periodic transformation
        return "Applying Periodic boundary condition"

    def __str__(self):
        """
        Return a string representation of the Periodic boundary condition.

        :return: A string describing the boundary condition, including its name and coordinate.
        """
        return f"Periodic: {self.name}, coordinate: {self.coord}"


class AntiPeriodic(Periodic):
    """
    Class representing an anti-periodic boundary condition.
    This boundary condition links the values at the edges of the domain
    but inverts the values at the boundaries.
    """

    def _periodic_axis(self, array):
        """
        Move the selected coordinate to the first position and apply the anti-periodic transformation.

        :param array: The array representing the grid data.
        :return: The transformed array with applied anti-periodic boundary condition.
        """
        array = np.moveaxis(array, self.coord, 0)  # Move the selected coordinate to the front
        array[0] = -array[-2]  # Set the first element to the negative of the second-to-last
        array[-1] = -array[1]  # Set the last element to the negative of the second
        return np.moveaxis(array, 0, self.coord)  # Move back the coordinate

    def __str__(self):
        """
        Return a string representation of the AntiPeriodic boundary condition.

        :return: A string describing the boundary condition, including its name and coordinate.
        """
        return f"AntiPeriodic: {self.name}, coordinate: {self.coord}"
