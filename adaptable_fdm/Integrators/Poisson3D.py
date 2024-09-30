class Poisson3D():

    def __init__(self):
        """
        Poisson3D solve by a iterative method the Poisson equation withour charges
        nabla(phi) = 0
        """

        print("[Poisson3D] Created")
        self.name = "poisson3D"

    def update(self,gridData):
        Phi = gridData.Phi
        gridData.newPhi[1:-1,1:-1,1:-1] = (1 / 6) * (Phi[1:-1,2:,1:-1] +
                                                    Phi[1:-1,0:-2,1:-1] +
                                                    Phi[2:,1:-1,1:-1] +
                                                    Phi[0:-2,1:-1,1:-1]+
                                                    Phi[1:-1,1:-1,2:] +
                                                    Phi[1:-1,1:-1,0:-2])
