# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:30:10 2020

@author: ABC
"""

from  gen_velocity import *
def forces(RX,RY,RZ):
    FX = np.zeros(n_atom)
    FY = np.zeros(n_atom)
    FZ = np.zeros(n_atom)
    EPOT = 0
    for i in range(n_atom-1):
        for j in range((i+1),n_atom):
            RXIJ = RX[i] - RX[j]
            RXIJ = RXIJ - BOXL * round(RXIJ/BOXL) ###! Minimum image condition
            RYIJ = RY[i] - RY[j]
            RYIJ = RYIJ - BOXL * round(RYIJ/BOXL)
            RZIJ = RZ[i] - RZ[j]
            RZIJ = RZIJ - BOXL * round(RZIJ/BOXL)
            R2 = RXIJ * RXIJ + RYIJ * RYIJ + RZIJ * RZIJ
            RC =2.5
            RC2 = RC * RC
            if (R2) <= (RC2):
                R2I = 1.0/R2
                R6I = R2I * R2I * R2I
                FF = 48.0 * R2I * R6I * (R6I - 0.5)
                FX[i] = FX[i] + FF * RXIJ
                FX[j] = FX[j] - FF * RXIJ
                FY[i] = FY[i] + FF * RYIJ
                FY[j] = FY[j] - FF * RYIJ
                FZ[i] = FZ[i] + FF * RZIJ
                FZ[j] = FZ[j] - FF * RZIJ
                EPOT = EPOT + 4.0 * R6I * (R6I - 1.0)
    return (FX,FY,FZ,EPOT)
FX,FY,FZ,EPOT = forces(RX,RY,RZ)



