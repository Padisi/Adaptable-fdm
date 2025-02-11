class firstPassageTime3D():

    def __init__(self,D):
        """
        First passage time solver in 3D. Solves the distribution G(t,x,y,z) probability of survive
        including Diffusion and Advection.

        Reflecting boundaries == Neumann
        Absorbing == Dirichlet (Escape zone)

        Time is axis=0, positions are axis = 1,2,3

        Equation:
        d_t(G) = F(t,x,y,z)*grad(G) + D(t,x,y,z) * Laplacian (G)

        F takes gd.Force, but must have units of velocity. (so in a Brownian description we must set gd.Force as mu*Force)
        """

        print("[firstPassageTime3D] Created")
        self.name = "firstPassageTime3D"
        self.D    = D2

    def update(self,gridData):
        preFactor = 1/(self.D*6/(gridData.dx*gridData.dx)+1/gridData.dt)
        values = gridData.values
        F   = gridData.Force
        gridData.new_values[1:,1:-1,1:-1,1:-1] = preFactor * (self.D*( # Solo derivada primera del tiempo, usamos derivada hacia atras para poder poner la CI en el inicio
                                                            values[1:,2:,1:-1,1:-1] + values[1:,:-2,1:-1,1:-1] + values[1:,1:-1,2:,1:-1] + values[1:,1:-1,0:-2,1:-1] + values[1:,1:-1,1:-1,2:] + values[1:,1:-1,1:-1,:-2])/(gridData.dx**2) +
                                                            F[1:,1:-1,1:-1,1:-1]/(2*gridData.dx)*(values[1:,2:,1:-1,1:-1]-values[1:,:-2,1:-1,1:-1]+values[1:,1:-1,2:,1:-1]-values[1:,1:-1,1:-1,:-2]+values[1:,1:-1,1:-1,2:]-values[1:,1:-1,1:-1,:-2])+
                                                            values[:-1,1:-1,1:-1,1:-1]/gridData.dt)
