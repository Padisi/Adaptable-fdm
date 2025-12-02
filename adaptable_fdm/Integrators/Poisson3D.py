from .IntegratorBase import IntegratorBase

class Poisson3D(IntegratorBase):

    def __init__(self, mixing=1.0):
        """
        Poisson3D solve by a iterative method the Poisson equation withour charges
        ∇φ = 0
        """
        super().__init__()
        print("[Poisson3D] Integrator created")
        self.name = "poisson3D"
        self.mixing = mixing

    def update(self,gridData):
        values = gridData.values.copy()
        gridData.new_values[1:-1,1:-1,1:-1] = (1 / 6) * (values[1:-1,2:,1:-1] +
                                                        values[1:-1,0:-2,1:-1] +
                                                        values[2:,1:-1,1:-1] +
                                                        values[0:-2,1:-1,1:-1]+
                                                        values[1:-1,1:-1,2:] +
                                                        values[1:-1,1:-1,0:-2]) * self.mixing + values[1:-1,1:-1,1:-1] * (1 - self.mixing)


class Poisson3D_eps(IntegratorBase):

    def __init__(self,eps, mixing=1.0):
        """
        Poisson3D solve by a iterative method the Poisson equation withour charges
        nabla(phi) = 0
        """
        super().__init__()
        self.name = "Poisson3D_eps"
        print("["+self.name+"] Created")
        self.eps  = eps
        self.mixing = mixing

    def initialize_auxiliary_grids(self, gridData):
        """
        Stores eps at gridData to be accesible from all the simulation.
        """
        gridData.add_grid("eps", initial_value=self.eps)
        del self.eps
        print("["+self.name+"] Initialized 'eps' in [GridData]")

    def update(self,gridData):
        values = gridData.values
        try :
            Eps = gridData.get_grid("eps")
        except KeyError:
            raise KeyError("["+self.name+"] eps grid not found in GridData. Please, initialize it before calling update().")

        EpsX2 = (Eps[:-1,:,:]+Eps[1:,:,:])/2
        EpsY2 = (Eps[:,:-1,:]+Eps[:,1:,:])/2
        EpsZ2 = (Eps[:,:,:-1]+Eps[:,:,1:])/2

        gd.new_values[1:-1,1:-1,1:-1] = (EpsX2[1:,1:-1,1:-1]*values[2:,1:-1,1:-1]+EpsX2[:-1,1:-1,1:-1]*values[:-2,1:-1,1:-1]+
                                     EpsY2[1:-1,1:,1:-1]*values[1:-1,2:,1:-1]+EpsY2[1:-1,:-1,1:-1]*values[1:-1,:-2,1:-1]+
                                     EpsZ2[1:-1,1:-1,1:]*values[1:-1,1:-1,2:]+EpsZ2[1:-1,1:-1,:-1]*values[1:-1,1:-1,:-2])/(
                                     EpsX2[1:,1:-1,1:-1]+EpsX2[:-1,1:-1,1:-1] + EpsY2[1:-1,1:,1:-1]+EpsY2[1:-1,:-1,1:-1] + EpsZ2[1:-1,1:-1,1:]+EpsZ2[1:-1,1:-1,:-1])


class Poisson3D_Inhomogeneous(IntegratorBase):
    def __init__(self, inh_part, mixing=1.0):
        """
        Poisson3D solve by a iterative method the Poisson equation with charges
        ∇φ = - ρ/ε0
        """
        super().__init__()
        print("[Poisson3D_Inhomogeneus] Integrator created")
        self.name = "poisson3D_inhomogeneus"
        self.inh_part = inh_part
        self.mixing = mixing

    def update(self, gridData):
        values = gridData.values.copy()
        gridData.new_values[1:-1,1:-1,1:-1] = (1 / 6) * (values[1:-1,2:,1:-1] +
                                                        values[1:-1,0:-2,1:-1] +
                                                        values[2:,1:-1,1:-1] +
                                                        values[0:-2,1:-1,1:-1]+
                                                        values[1:-1,1:-1,2:] +
                                                        values[1:-1,1:-1,0:-2] +
                                                        self.inh_part[1:-1,1:-1,1:-1]*gridData.h*gridData.h) * self.mixing + values[1:-1,1:-1,1:-1] * (1 - self.mixing)
