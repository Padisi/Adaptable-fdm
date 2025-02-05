import numpy as np
import json
import os
import adaptable_fdm as fdm

def constructTabulated(params):

    Lx = params["Lx"]
    Ly = params["Lx"]
    Lz = params["Lx"]

    Nx = params["Nx"]
    Ny = params["Ny"]
    Nz = params["Nz"]

    h  = params["height"]
    w  = params["width"]
    Ew = params["electrodeWidth"]

    Box = [Lx,Ly,Lz]
    Ngrid = [Nx,Ny,Nz]

    gd = fdm.GridData(Box,Ngrid)

    tolCheck = fdm.toleranceChecker((gd.h**3)*1e-2,100000,1)

    dielectricMask = (np.abs(gd.pos[0])>=w+Ew)*(np.abs(gd.pos[1])>=w+Ew)

    bcList = [

        fdm.Neumann(2, 0, name="Techo"),
        fdm.Neumann(2,-1, name="Suelo"),
        fdm.Neumann(0,0, name="ParedX"),
        fdm.Neumann(0,-1, name="ParedX-"),
        fdm.Neumann(1,0, name="ParedY"),
        fdm.Neumann(1,-1, name="ParedY-"),

        fdm.NeumannFlatZ(h     , gd.h,  1, dielectricMask, name="Techo dielectrico1"),

        fdm.Dirichlet((gd.pos[2] <= -Lz/2+h)*(gd.pos[0]>=w) *(gd.pos[1]>=w) *np.logical_not(dielectricMask),    -.1, "Electrodo_Negativo1"),
        fdm.Dirichlet((gd.pos[2] <= -Lz/2+h)*(gd.pos[0]>=w) *(gd.pos[1]<=-w)*np.logical_not(dielectricMask),     .1, "Electrodo_Negativo1"),
        fdm.Dirichlet((gd.pos[2] <= -Lz/2+h)*(gd.pos[0]<=-w)*(gd.pos[1]>=w) *np.logical_not(dielectricMask),     .1, "Electrodo_Negativo1"),
        fdm.Dirichlet((gd.pos[2] <= -Lz/2+h)*(gd.pos[0]<=-w)*(gd.pos[1]<=-w)*np.logical_not(dielectricMask),    -.1, "Electrodo_Negativo1"),
    ]

    sim = fdm.Simulation(gd,fdm.Poisson3D(),bcList,tolCheck)
    sim.start()
    # Calcular el campo eléctrico
    Ex, Ey, Ez = np.gradient(-gd.Phi, gd.h, gd.h, gd.h)
    Energy = (Ex*Ex + Ey*Ey + Ez*Ez)
    Fx, Fy, Fz = np.gradient(-Energy, gd.h, gd.h, gd.h)
    return Energy,Fx,Fy,Fz

with open("./parameters.json") as f:
    inputData = json.load(f)

E, Fx, Fy, Fz = constructTabulated(inputData)
np.save("./tabulated.npy",[E,Fx,Fy,Fz])
