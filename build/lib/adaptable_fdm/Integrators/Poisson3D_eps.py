class Poisson3D_eps():

    def __init__(self):
        """
        Poisson3D solve by a iterative method the Poisson equation withour charges
        nabla(phi) = 0
        """

        print("[Poisson3D_eps] Created")
        self.name = "poisson3D"

    def update(self,gridData):
        Phi = gridData.Phi
        Eps = gridData.Eps

        EpsX2 = (Eps[:-1,:,:]+Eps[1:,:,:])/2
        EpsY2 = (Eps[:,:-1,:]+Eps[:,1:,:])/2
        EpsZ2 = (Eps[:,:,:-1]+Eps[:,:,1:])/2

        gd.newPhi[1:-1,1:-1,1:-1] = (EpsX2[1:,1:-1,1:-1]*Phi[2:,1:-1,1:-1]+EpsX2[:-1,1:-1,1:-1]*Phi[:-2,1:-1,1:-1]+
                                     EpsY2[1:-1,1:,1:-1]*Phi[1:-1,2:,1:-1]+EpsY2[1:-1,:-1,1:-1]*Phi[1:-1,:-2,1:-1]+
                                     EpsZ2[1:-1,1:-1,1:]*Phi[1:-1,1:-1,2:]+EpsZ2[1:-1,1:-1,:-1]*Phi[1:-1,1:-1,:-2])/(
                                     EpsX2[1:,1:-1,1:-1]+EpsX2[:-1,1:-1,1:-1] + EpsY2[1:-1,1:,1:-1]+EpsY2[1:-1,:-1,1:-1] + EpsZ2[1:-1,1:-1,1:]+EpsZ2[1:-1,1:-1,:-1])

