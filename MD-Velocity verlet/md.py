# -*- coding: utf-8 -*-
"""
Created on Fri May  8 23:21:12 2020

@author: ABC
"""
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:42:59 2020

@author: shubhojit
"""

from Force_calculations import *
DELT = float(input("LENGTH OF TIME STEP = "))
no_step = int(input("Number of time steps(iterations) you want = "))
EK =[]
Epot =[]
ETOTAL =[]
V = []
v_ =[]
Rt = [] 
t = []
T = []
pe1 = 0
tem1 = 0
Rt.append([RX,RY,RZ])
f= open("md.txt","a")
for j in range(no_step):
    RX = (RX +  DELT * V2x  + 0.5 * DELT * DELT * FX)% BOXL  ###! Update the positions to t + dt
    RY = (RY +  DELT * V2y  + 0.5 * DELT * DELT * FY)% BOXL
    RZ = (RZ +  DELT * V2z  + 0.5 * DELT * DELT * FZ)% BOXL
    FX1,FY1,FZ1,EPOT=forces(RX,RY,RZ)
    V2x = V2x + (FX + FX1) * 0.5 * DELT
    V2y = V2y + (FY + FY1) * 0.5 * DELT
    V2z = V2z + (FZ + FZ1) * 0.5 * DELT
    Vsq = V2x*V2x + V2y*V2y + V2z*V2z
    vsq = sum(Vsq)
    ek = .5 * vsq
    EK.append(ek)
    Epot.append(EPOT)
    et = ek + (EPOT)
    ETOTAL.append(et)
    tem = vsq/df
    T.append(tem)
    V.append([np.mean(V2x),np.mean(V2y),np.mean(V2z)])
    v_.append([V2x,V2y,V2z])
    Rt.append([RX,RY,RZ])
    FX = FX1
    FY = FY1
    FZ = FZ1
f.write("\n\nFINAL position\n")
f.write("%s %5s %10s %10s\n" %("atom", "X", "Y", "Z"))
for i in range(n_atom):
    f.write("%s %10.6f %10.6f %10.6f\n"%((at[0]), RX[i], RY[i], RZ[i]))
f.write("\n\nENERGY DATA\n")
f.write("%s %5s %10s %10s\n" %("STEP", "Ek", "POT-ENERGY", "E-Total"))
for i in range(no_step):
    f.write("%d %10.6f %10.6f %10.6f\n" %(i, EK[i], Epot[i], ETOTAL[i]))    

'''2)OUTPUT FILE FOR Vcm vs TIME'''

f.write("\n\n")
f.write("%5s %10s %10s\n" %("Vcmx", "Vcmy", "Vcmz"))
for i in range(-100,0,1):
    f.write("%10.6e %10.6e %10.6e\n" %(V[i][0], V[i][1], V[i][2]))
f.write("\n\n")
'''3)AVERAGE VALUE OF POTRNTIAL ENERGY & TEMPERATURE'''
print(T)
m =int(no_step/2)
pe1 = Epot[-m:]
tem1 = T[-m:]
avg_pe =sum(pe1)/m
avg_tem =sum(tem1)/m
f.write("Average Potential Energy = %f" %(avg_pe))
f.write("Average Temperature =%f" %(avg_tem))
f.close()

f= open("vcm.txt","a+")
f.write("%5s %12s %13s\n" %("Vcmx", "Vcmy", "Vcmz"))
for i in range(-100,0,1):
    f.write("%10.6e %10.6e %10.6e\n" %(V[i][0], V[i][1], V[i][2]))
f.write("\n\n")
f.close()


