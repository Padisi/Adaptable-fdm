import numpy as np
from .BoundaryCondition import BoundaryCondition

class DoubleLayerX(BoundaryCondition):
    """
    Class representing a flat complex boundary proposed to model an electrode inside a electrolite envoriment
    Propposed by Green and Ramos in PHYSICAL REVIEW E 66, 026305 (2002).

    σ dφ/dy = (φ - V_0)/Z

    Combine Neumann and Dirichlet with parameters V, σ and Z. But σ and Z contribute equals, so we only uses a multiplicative factor A.

    dφ/dy = (φ - V_0)/A

    This is implemented by doing:

    φ(i) = [φ(i+1)*self.constant-self.V_0*h]/[A-h]

    where h is the cellSize
    """

    def __init__(self, height, cellSize, add, mask, V_0, constant ,name):
        """
        Constructor for the DoubleLayer class.

        :param height: Position of the wall measured in terms of cellSize.
        :param cellSize: Unit of length in the system.
        :param add: Direction of the derivative from the wall (-1 or 1).
        :param mask: Mask for the perpendicular components. Domain of the plane.
        :param V_0: amplitude of the voltage conected to the electrode
        :param constant: impedance times conductivity, constant A in the description method.
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
        self.constant = constant
        self.V_0 = V_0
        print("[BoundaryConditions] " + str(self) + " boundary cell index = ", self.h, "Impedance value = ", self.constant, "Voltage = ", self.V0)

    def apply(self, gridData):
        """
        Apply the flat DoubleLayer boundary condition to the grid data.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the DoubleLayer boundary condition has been applied.
        """
        gridData.new_values[self.h, :, :][self.mask[self.h, :, :]] = (gridData.values[self.h + self.add, :, :][self.mask[self.h + self.add, :, :]]*self.constant-self.V_0*gridData.h)/(self.constant-gridData.h)
        return f"Applying DoubleLayer boundary condition with value"

    def __str__(self):
        """
        Return a string representation of the DoubleLayer boundary condition.

        :return: A string describing the boundary condition, including its name.
        """
        return f"DoubleLayer: {self.name}"


class DoubleLayerY(DoubleLayerX):
    """
    Class representing a flat DoubleLayer boundary condition along the Y-axis.
    This class inherits from DoubleLayerX and overrides the apply method for Y-axis specifics.
    """

    def apply(self, gridData):
        """
        Apply the flat DoubleLayer boundary condition to the grid data along the Y-axis.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the DoubleLayer boundary condition has been applied.
        """
        gridData.new_values[:, self.h, :][self.mask[:, self.h, :]] = (gridData.values[:, self.h + self.add, :][self.mask[:, self.h + self.add, :]]*self.constant-self.V_0*gridData.h)/(self.constant-gridData.h)
        return f"Applying DoubleLayer boundary condition with value"


class DoubleLayerZ(DoubleLayerX):
    """
    Class representing a flat DoubleLayer boundary condition along the Z-axis.
    This class inherits from DoubleLayerX and overrides the apply method for Z-axis specifics.
    """

    def apply(self, gridData):
        """
        Apply the flat DoubleLayer boundary condition to the grid data along the Z-axis.

        :param gridData: An instance of the GridData class to which the boundary condition is applied.
        :return: A string indicating that the DoubleLayer boundary condition has been applied.
        """
        gridData.new_values[:, :, self.h][self.mask[:, :, self.h]] = (gridData.values[:, :, self.h + self.add][self.mask[:, :, self.h + self.add]]*self.constant-self.V_0*gridData.h)/(self.constant-gridData.h)
        return f"Applying DoubleLayer boundary condition with value"
