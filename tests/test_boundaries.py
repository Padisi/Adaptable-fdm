def test_construct():
    import adaptable_fdm as fdm
    bc_list = [
            fdm.Neumann(2,0,name="afa"),
            fdm.Dirichlet(1,1,name="Dirichlet1"),
            fdm.Periodic(0,name = "Periodic"),
            fdm.DoubleLayerX(1,1,1,1,1,1,name="DoubleLayer")
            ]
