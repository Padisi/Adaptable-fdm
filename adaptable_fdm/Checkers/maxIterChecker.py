import numpy as np
from .CheckerBase import checkerBase

class maxitersChecker(checkerBase):
    """
    Class for checking maximum iterations.
    This class inherits from checkerBase and implements the logic to determine
    if the solution has converged within the given tolerance.
    """

    def __init__(self, max_iter):
        """
        Constructor for the maxIterChecker class.

        :param tol: The tolerance level for convergence. The simulation stops if the difference
                    between the new and old values is less than this value.
        :param max_iter: The maximum number of iterations allowed before stopping the simulation.
        :param relaxation_factor: The factor used to update the grid data, controlling the
                                  influence of the new values.
        """
        super().__init__()  # Initialize the base class
        print("[maxIterChecker] Created with tol=", tol, " max_iter=", max_iter, " relaxation_factor=", relaxation_factor)  # Print initialization details
        self.max_iter = max_iter  # Set maximum iterations

    def check(self, gridData):
        """
        Check if the solution has converged based on the current grid data.

        If the maximum absolute difference between the new and old values is less than the tolerance,
        the checker status is set to True.

        :param gridData: An instance of the GridData class that contains the current state of the grid.
        """
        if np.max(np.abs(gridData.new_values - gridData.values)) < self.tol:  # Check for convergence
            print(f'Convergence achieved in {self.iters} iterations.')  # Print convergence message
            self.checker = True  # Update checker status

    def actualize(self, gridData):
        """
        Update the grid data and check for convergence. Increment the iteration count.

        :param gridData: An instance of the GridData class that contains the current state of the grid.
        """
        self.checkTol(gridData)  # Check if convergence is achieved
        gridData.values = (self.relaxation_factor * gridData.new_values +
                        (1 - self.relaxation_factor) * gridData.values)  # Update grid data using relaxation factor
        if self.iters > self.max_iter:  # Check if maximum iterations are reached
            print(f"Reached Max Iter without convergence")  # Print message for maximum iterations
            self.checker = True  # Update checker status
        self.iters += 1  # Increment iteration count
