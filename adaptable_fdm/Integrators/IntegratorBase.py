class IntegratorBase():

    def __init__(self):
        """
        Minimum version of Integrator so simulation can perform
        """
        self.name = "Integrator"

    def initialize_auxiliary_grids(self, gridData):
        """
        Initialize here auxiliary values that your update() function need
        such as temperature for instance.

        This line is performed once at the beggining of the program.
        """
        # gridData.add_grid(name,initial_value=0)
        return 0

    def update(self,gridData):
        """
        Do nothing
        """
        gridData.new_values = gridData.values*1
