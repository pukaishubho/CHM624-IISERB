# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:47:23 2020

@author: Shubhojit
"""
import numpy as np
from gencord import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
temp = float(input("required temperature in reduce unit ="))
###temp =1
vx = np.random.uniform(-.5,.5,size = n_atom )
vy = np.random.uniform(-.5,.5,size = n_atom )
vz = np.random.uniform(-.5,.5,size = n_atom )
print(vx)
###conservation of linear momentum
Vcx =np.mean(vx) 
Vcy =np.mean(vy)
Vcz =np.mean(vz)
#print(Vcx,Vcy,Vcz)
V1x = np.zeros(len(vx))
V1y = np.zeros(len(vy))
V1z = np.zeros(len(vz))
v2 = []
V1x = vx - Vcx
V1y = vy - Vcy
V1z = vz - Vcz
v2 = V1x*V1x+V1y*V1y+V1z*V1z

x = sum(V1x)
y = sum(V1y)
z = sum(V1z)
V2 = sum(v2)
#print("total velocity along x,y,z direction = ", x,y,z)
#print("V**2 = ",V2)




##############calculation of initial temp before scaling
df = ((3*n_atom)-3)
T_red = V2/df
#print(T_red)
##############Scale the velocity:
fs = np.sqrt((temp*df)/V2)
V2x =np.zeros(len(V1x))
V2y =np.zeros(len(V1y))
V2z =np.zeros(len(V1z))
V2x = V1x * fs
V2y = V1y * fs
V2z = V1z * fs
V_sq = V2x*V2x+V2y*V2y+V2z*V2z
av_v_sq = sum(V_sq)
kin = 0.5*av_v_sq


