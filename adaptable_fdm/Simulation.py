class Simulation:
    """
    Class to run a simulation using grid data, a specified integrator, and boundary conditions.
    This class manages the simulation process by iteratively updating the system state.
    """

    def __init__(self, gridData, integrator, boundaryConditionsList, Checker):
        """
        Constructor for the Simulation class.

        :param gridData: An instance of the GridData class containing the grid information.
        :param integrator: An object responsible for updating the simulation state.
        :param boundaryConditionsList: A list of boundary condition objects to apply during the simulation.
        :param Checker: An object used to check for convergence or tolerance in the simulation.

        This method initializes the simulation parameters and prepares for execution.
        """
        self.gridData = gridData  # Grid data for the simulation
        self.integrator = integrator  # Integrator for updating the state
        self.bcList = boundaryConditionsList  # List of boundary conditions
        self.toleranceChecker = Checker  # Tolerance checker for convergence

    def start(self):
        """
        Start the simulation process.

        This method runs the simulation loop, continuing until the tolerance checker indicates convergence.
        """
        while self.toleranceChecker.checker == False:  # Continue until tolerance is met
            self.step()  # Perform a simulation step

    def step(self):
        """
        Execute a single simulation step.

        This method updates the simulation state using the integrator and applies boundary conditions.
        It also updates the tolerance checker after each step.
        """
        self.integrator.update(self.gridData)  # Update the state with the integrator

        # Apply boundary conditions
        for boundary in self.bcList:
            boundary.apply(self.gridData)

        # Update the tolerance checker
        self.toleranceChecker.actualize(self.gridData)
