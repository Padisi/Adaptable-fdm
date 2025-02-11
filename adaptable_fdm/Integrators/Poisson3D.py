from .IntegratorBase import IntegratorBase

class Poisson3D(IntegratorBase):

    def __init__(self):
        """
        Poisson3D solve by a iterative method the Poisson equation withour charges
        ∇φ = 0
        """
        super().__init__()
        print("[Poisson3D] Integrator created")
        self.name = "poisson3D"

    def update(self,gridData):
        values = gridData.values
        gridData.new_values[1:-1,1:-1,1:-1] = (1 / 6) * (values[1:-1,2:,1:-1] +
                                                        values[1:-1,0:-2,1:-1] +
                                                        values[2:,1:-1,1:-1] +
                                                        values[0:-2,1:-1,1:-1]+
                                                        values[1:-1,1:-1,2:] +
                                                        values[1:-1,1:-1,0:-2])
class Poisson3D_eps(IntegratorBase):

    def __init__(self,eps):
        """
        Poisson3D solve by a iterative method the Poisson equation withour charges
        nabla(phi) = 0
        """
        super().__init__()
        self.name = "Poisson3D_eps"
        print("["+self.name+"] Created")
        self.eps  = eps

    def initialize_auxiliary_grids(self, gridData):
        """
        Stores eps at gridData to be accesible from all the simulation.
        """
        gridData.add_grid("eps", initial_value=self.eps)
        del self.eps
        print("["+self.name+"] Initialized 'eps' in [GridData]")

    def update(self,gridData):
        values = gridData.values
        Eps = gridData.get_grid("eps")

        EpsX2 = (Eps[:-1,:,:]+Eps[1:,:,:])/2
        EpsY2 = (Eps[:,:-1,:]+Eps[:,1:,:])/2
        EpsZ2 = (Eps[:,:,:-1]+Eps[:,:,1:])/2

        gd.new_values[1:-1,1:-1,1:-1] = (EpsX2[1:,1:-1,1:-1]*values[2:,1:-1,1:-1]+EpsX2[:-1,1:-1,1:-1]*values[:-2,1:-1,1:-1]+
                                     EpsY2[1:-1,1:,1:-1]*values[1:-1,2:,1:-1]+EpsY2[1:-1,:-1,1:-1]*values[1:-1,:-2,1:-1]+
                                     EpsZ2[1:-1,1:-1,1:]*values[1:-1,1:-1,2:]+EpsZ2[1:-1,1:-1,:-1]*values[1:-1,1:-1,:-2])/(
                                     EpsX2[1:,1:-1,1:-1]+EpsX2[:-1,1:-1,1:-1] + EpsY2[1:-1,1:,1:-1]+EpsY2[1:-1,:-1,1:-1] + EpsZ2[1:-1,1:-1,1:]+EpsZ2[1:-1,1:-1,:-1])

