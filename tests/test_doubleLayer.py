
def numericalSolution(x,A,B,L):
    return B*(L/2-x)/(A+L)

def test_doubleLayerX():
    import numpy as np
    import adaptable_fdm as fdm
    Lx = 1
    Ly = 0.01
    Lz = 0.01

    Nx = 100
    Ny = 1
    Nz = 1

    Box = [Lx,Ly,Lz]
    Ngrid = [Nx,Ny,Nz]

    V0 = 1
    ZDL = 1 + 1j
    tol = 1e-7

    gd = fdm.GridData(Box,Ngrid)
    gd.values = numericalSolution(gd.pos[0], ZDL, V0, Lx+gd.h)
    gd.new_values = gd.values.copy()
    tolCheck = fdm.toleranceChecker(tol,100000,1)

    bcList = [

        fdm.Periodic(2, name="PeriodicZ"),
        fdm.Periodic(1, name="PeriodicY"),
        fdm.DoubleLayerX(0, gd.h, 1, gd.pos[0]<=Lx, V0, ZDL, name="DoubleLayer"),
        ]

    sim = fdm.Simulation(gd,fdm.Poisson3D(),bcList,tolCheck)
    sim.start()

    phi = numericalSolution(gd.pos[0], ZDL, V0, Lx+0.01)
    diff = (phi-gd.values)
    max_diff = np.max(np.abs(diff))
    if max_diff>tol:
        raise ValueError(f"Double Layer don't reach the exact solution, tolerance is {tol:.2e} but max error is {max_diff:.2e}")
    # Calcular el campo eléctrico
    return None

def test_doubleLayerY():
    import numpy as np
    import adaptable_fdm as fdm
    Lx = 0.01
    Ly = 1
    Lz = 0.01

    Nx = 1
    Ny = 100
    Nz = 1

    Box = [Lx,Ly,Lz]
    Ngrid = [Nx,Ny,Nz]

    V0 = 1
    ZDL = 1 + 1j
    tol = 1e-7

    gd = fdm.GridData(Box,Ngrid)
    gd.values = numericalSolution(gd.pos[1], ZDL, V0, Ly+gd.h)
    gd.new_values = gd.values.copy()
    tolCheck = fdm.toleranceChecker(tol,100000,1)

    bcList = [

        fdm.Periodic(2, name="PeriodicZ"),
        fdm.Periodic(0, name="PeriodicY"),
        fdm.DoubleLayerY(0, gd.h, 1, gd.pos[0]<=Lx, V0, ZDL, name="DoubleLayer"),
        ]

    sim = fdm.Simulation(gd,fdm.Poisson3D(),bcList,tolCheck)
    sim.start()

    phi = numericalSolution(gd.pos[1], ZDL, V0, Ly+0.01)
    diff = (phi-gd.values)
    max_diff = np.max(np.abs(diff))
    if max_diff>tol:
        raise ValueError(f"Double Layer don't reach the exact solution, tolerance is {tol:.2e} but max error is {max_diff:.2e}")
    # Calcular el campo eléctrico
    return None

def test_doubleLayerZ():
    import numpy as np
    import adaptable_fdm as fdm
    Lx = 0.01
    Ly = 0.01
    Lz = 1

    Nx = 1
    Ny = 1
    Nz = 100

    Box = [Lx,Ly,Lz]
    Ngrid = [Nx,Ny,Nz]

    V0 = 1
    ZDL = 1 + 1j
    tol = 1e-7

    gd = fdm.GridData(Box,Ngrid)
    gd.values = numericalSolution(gd.pos[2], ZDL, V0, Lz+gd.h)
    gd.new_values = gd.values.copy()
    tolCheck = fdm.toleranceChecker(tol,100000,1)

    bcList = [

        fdm.Periodic(0, name="PeriodicX"),
        fdm.Periodic(1, name="PeriodicY"),
        fdm.DoubleLayerZ(0, gd.h, 1, gd.pos[0]<=Lx, V0, ZDL, name="DoubleLayer"),
        ]

    sim = fdm.Simulation(gd,fdm.Poisson3D(),bcList,tolCheck)
    sim.start()

    phi = numericalSolution(gd.pos[2], ZDL, V0, Lz+0.01)
    diff = (phi-gd.values)
    max_diff = np.max(np.abs(diff))
    if max_diff>tol:
        raise ValueError(f"Double Layer don't reach the exact solution, tolerance is {tol:.2e} but max error is {max_diff:.2e}")
    # Calcular el campo eléctrico
    return None
