import numpy as np

class GridData:
    """
    Class to manage and store grid data for a 3D box with arbitrary dimensions and number of cells.
    It computes grid coordinates, cell sizes, and initializes the Phi and Eps arrays.
    """

    def __init__(self, Box, N):
        """
        Constructor for the GridData class.

        :param Box: List of box dimensions, [Lx, Ly, Lz].
        :param N: List of the number of cells in each direction, [Nx, Ny, Nz].

        This method initializes the box dimensions, grid size, and computes grid coordinates.
        It also checks for dimensional consistency between `Box` and `N`.
        """
        print("[GridData] Created with Box ", Box, " Ngrid ", N)
        if len(Box) != len(N):
            raise ValueError("Box and N must have the same number of dimensions.")

        self.Box = Box  # [Lx, Ly, Lz] or arbitrary dimensions
        self.N = N  # [Nx, Ny, Nz] or arbitrary number of cells

        # Calculate and store the cell distances
        self._check_errors()
        self.Phi = np.zeros(self.N)  # Initialize the Phi array with zeros
        self.Eps = np.ones(self.N)   # Initialize the Eps array with ones

        # Create the grid of coordinates
        x = []
        for L, N in zip(self.Box, self.N):
            x.append(np.linspace(-L/2, L/2, N))  # *x returns unpacked arrays in a list of arrays

        self.pos = np.meshgrid(*x, indexing="ij")  # Create grid positions

        self.newPhi = self.Phi * 1  # Copy of the Phi array

    def _check_errors(self):
        """
        Checks for errors in grid configuration and calculates the cell sizes.

        This function verifies that the number of cells in each direction is an integer
        and that all cells are of uniform size. It also stores the size of the cells.
        """
        for n in self.N:
            if n % 1 != 0:
                raise ValueError("Ncells must be an integer.")

        # Calculate the size of the cells in each dimension
        d = [self.Box[i] / self.N[i] for i in range(len(self.Box))]
        self.h = d[0]  # Store the size of the cells (assuming homogeneous grid)

        # Check if cells are homogeneous in size
        for i in range(len(d) - 1):
            if d[i] != d[i + 1]:
                raise ValueError("Cells are not homogeneous in size.")
