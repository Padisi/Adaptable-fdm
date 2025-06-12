import numpy as np

class GridData:
    """
    Class to manage and store grid data for a 3D box with arbitrary dimensions and number of cells.
    It computes grid coordinates, cell sizes, and initializes the values.


    For now, grids in afdm are regular, homogeneus grids. With one phantom cell in each border of the dimensions.
    Values are centered at the grid faces, and phantom cells are beyond the limits. So phantom cell is collocated at
    -L/2-h/2 and L/2+h/2, and first real cell is collocated at -L/2+h/2.

       |  P  |  P |  P |  P |  P  |
       |  P  |  1 |  2 |  3 |  P  |
       |  P  |  4 |  5 |  6 |  P  |
       |  P  |  7 |  8 |  9 |  P  |
       |  P  |  P |  P |  P |  P  |
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
        self.values = np.zeros([n+2 for n in self.N])  # Initialize the values array with zeros

        # Create the grid of coordinates
        x = []
        for L, N in zip(self.Box, self.N):
            x.append(np.linspace(-L/2-self.h/2, L/2+self.h/2, N+2))  # *x returns unpacked arrays in a list of arrays

        self.pos = np.meshgrid(*x, indexing="ij")  # Create grid positions

        self.new_values = self.values.copy()  # Copy of the values array

        self.auxiliar_grids = {}

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
        d = [self.Box[i] / (self.N[i]) for i in range(len(self.Box))]
        self.h = d[0]  # Store the size of the cells (assuming homogeneous grid)

        # Check if cells are homogeneous in size
        if not all(np.isclose(d[i], d[0]) for i in range(1, len(d))):
            raise ValueError(f"Cells must be homogeneous in size, but h is {d}.")
    def add_grid(self, name, initial_value=0):
        """Add a new grid withe the same lenght of values"""
        self.auxiliar_grids[name] = np.full_like(self.values, initial_value)

    def get_grid(self, name):
        """Get a grid with its name"""
        return self.auxiliar_grids.get(name, None)
