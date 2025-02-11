def test_construct():
    import adaptable_fdm as fdm
    integrator = fdm.Poisson3D()
    integrator = fdm.Poisson3D_eps(eps=1)
    integrator = fdm.Tester()

def test_Poisson3D_eps():
    import adaptable_fdm as fdm
    import numpy as np
    N = 10
    L = 1
    eps = 1
    gd = fdm.GridData([L],[N])
    integrator = fdm.Poisson3D_eps(eps=eps)
    integrator.initialize_auxiliary_grids(gd)
    if (gd.get_grid("eps")!=eps).any():
        raise RuntimeError("Error: 'eps' is not stored at gridData")
    if hasattr(integrator, 'eps'):
        raise RuntimeError("Error: Integrator hasn't liberated 'eps' memory")

    ### Test eps to be a matrix ###
    gd = fdm.GridData([L,L],[N,N])
    eps = gd.pos[0]**2 #ε = χ**2
    integrator = fdm.Poisson3D_eps(eps=eps)
    integrator.initialize_auxiliary_grids(gd)
    if (gd.get_grid("eps")!=eps).any():
        raise RuntimeError("Error: 'eps' is not stored at gridData")
    if hasattr(integrator, 'eps'):
        raise RuntimeError("Error: Integrator hasn't liberated 'eps' memory")


