class checkerBase:
    """
    Base class for implementing a tolerance checker for simulations.
    This class keeps track of whether a certain tolerance has been met
    and counts the number of iterations.
    """

    def __init__(self):
        """
        Constructor for the checkerBase class.

        This method initializes the checker status to False and the iteration count to 0.
        """
        print("[Checker] created")  # Print message indicating that the checker has been created
        self.checker = False  # Status of the checker
        self.iters = 0  # Count of iterations

    def check(self):
        """
        Set the checker status to True, indicating that the condition has been met.
        """
        self.checker = True  # Update the checker status

    def actualize(self, gridData):
        """
        Update the checker based on the current grid data and increment the iteration count.

        :param gridData: An instance of the GridData class that contains the current state of the grid.
        """
        self.check()  # Check tolerance (assumes this will be implemented in a subclass)
        self.iters += 1  # Increment the iteration counter
