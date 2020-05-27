# -*- coding: utf-8 -*-
"""
Created on Wed May 13 16:48:11 2020

@author: ABC
"""


# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:49:38 2020

@author: ABC
"""
from md import *

##################PLOTS########################### 
'''fig1 =plt.figure()
plt1= fig1.add_subplot(221,projection='3d')
plt2= fig1.add_subplot(222)
plt3= fig1.add_subplot(223)
plt4= fig1.add_subplot(224)

plt1.set_title("INITIAL VS FINAL POSITION")
for i in range(n_atom):
    plt1.scatter(RX, RY, RZ, color ='red')
    plt1.scatter(Rt[0][0],Rt[0][1],Rt[0][2],color ='black')
    plt1.legend(["final","initial"])
plt2.hist(V2x, bins=50,)
plt2.hist(v_[0][0], bins=50)
plt2.legend(["final","initial"])
plt2.set_title("Final vs initial velocity(Vx) from normal distribution")
plt3.hist(V2y, bins=50)
plt3.hist(v_[0][1],bins=50)
plt3.legend(["final","initial"])
plt3.set_title("Final vs initial velocity(Vy) from normal distribution")
plt4.hist(V2z, bins=50)
plt4.hist(v_[0][2], bins=50)
plt4.legend(["final","initial"])
plt4.set_title("Final vs initial velocity(Vz) from normal distribution")
plt.savefig("position_velocity.png",dpi = 300)
################PLOT OF ENERGY################
fig2 =plt.figure()
plt5= fig2.add_subplot(221)
plt6= fig2.add_subplot(222)
plt7= fig2.add_subplot(223)
plt8= fig2.add_subplot(224)

plt5.plot(ETOTAL ,label ="ET")
plt5.plot(Epot ,label = "EP")
plt5.plot(EK ,label = "EK")
plt5.set_title("PLOT OF  ENERGY VS TIME")

plt5.legend()
plt6.plot(ETOTAL ,label ="ET")
plt6.legend()
plt6.set_title("PLOT OF  TOTAL-ENERGY VS TIME")

plt7.plot(Epot ,label = "EP")
plt7.legend()
plt7.set_title("PLOT OF  POTENTIAL-ENERGY VS TIME")

plt8.plot(EK ,label = "EK")
plt8.legend()
plt8.set_title("PLOT OF KINATIC-ENERGY VS TIME")

plt.savefig("eneergy-plot_for_whole_trajectory.png",dpi=300)

########ANSWER OF QUESTIONS########
###1)[a]plot for first 500 steps###
fig3 = plt.figure()
plt9= fig3.add_subplot(221)
plt10= fig3.add_subplot(222)
plt11= fig3.add_subplot(223)
plt12= fig3.add_subplot(224)
plt.xlabel("TIME")
plt.ylabel("ENERGY")

plt9.plot(ETOTAL[500:] ,label ="ET")
plt9.plot(Epot[500:] ,label = "EP")
plt9.plot(EK[500:] ,label = "EK")
plt9.set_title("PLOT OF  ENERGY VS TIME")
    
plt9.legend()
plt10.plot(ETOTAL[500:] ,label ="ET")
plt10.legend()
plt10.set_title("PLOT OF  TOTAL-ENERGY VS TIME")
    
plt11.plot(Epot[500:] ,label = "EP")
plt11.legend()
plt11.set_title("PLOT OF  POTENTIAL-ENERGY VS TIME")
    
plt12.plot(EK[500:] ,label = "EK")
plt12.legend()
plt12.set_title("PLOT OF  KINATIC-ENERGY VS TIME")
    

plt.savefig("energy-for_first-500_steps.png",dpi =300)

#1)[a]plot for last 500 steps###
fig4 = plt.figure()
plt13 = fig4.add_subplot(221)
plt14= fig4.add_subplot(222)
plt15= fig4.add_subplot(223)
plt16= fig4.add_subplot(224)
plt.xlabel("TIME")
plt.ylabel("KINATIC-ENERGY")


plt13.plot(ETOTAL[-500:] ,label ="ET")
plt13.plot(Epot[-500:] ,label = "EP")
plt13.plot(EK[-500:] ,label = "EK")
plt13.set_title("PLOT OF  ENERGY VS TIME")
plt13.legend()
plt14.plot(ETOTAL[-500:] ,label ="ET")
plt14.legend()
plt14.set_title("PLOT OF  TOTAL-ENERGY VS TIME")
    
plt15.plot(Epot[-500:] ,label = "EP")
plt15.legend()
plt15.set_title("PLOT OF  POTENTIAL-ENERGY VS TIME")
    
plt16.plot(EK[-500:] ,label = "EK")
plt16.legend()
plt16.set_title("PLOT OF  KINATIC-ENERGY VS TIME")
   
plt.savefig("energy-for_last-500_steps.png",dpi =300)

2)OUTPUT FILE FOR Vcm vs TIME
for k in np.arange(0,(DELT*no_step),DELT):
    t.append(k)
fig5 = plt.figure()
plt17= fig5.add_subplot(221)
plt18= fig5.add_subplot(222)
plt19= fig5.add_subplot(223)
plt20= fig5.add_subplot(224)
plt.xlabel("Vcm")
plt.ylabel("time")
for i in range(-100,0,1):

    plt17.plot(V[i][0])
    plt17.plot(V[i][1])
    plt17.plot(V[i][2])
    plt17.set_title("Vcm vs.Time")
    
    plt17.legend(["VcmX","VcmY","VcmZ"])
    plt18.plot(V[i][0])
    plt18.set_title("VcmX vs.Time")
    
    plt19.plot(V[i][1])
    plt19.set_title("VcmY vs.Time")
   
    plt20.plot(V[i][2])
    plt20.set_title("VcmZ vs.Time")
    
plt.savefig("Vcm-time.png",dpi = 300)
'''
fig1 =plt.figure()
plt1= fig1.add_subplot(111,projection='3d')
##################PLOTS POSITION vs VELOCITY#######
plt1.set_title("INITIAL VS FINAL POSITION")
for i in range(n_atom):
    plt1.scatter(RX, RY, RZ, color ='red')
    plt1.scatter(Rt[0][0],Rt[0][1],Rt[0][2],color ='black')
    plt1.legend(["final","initial"])
plt.savefig("position.png",dpi =300)
fig = plt.figure()
plt.hist(V2x, bins=50,)
plt.hist(v_[0][0], bins=50)
plt.legend(["final","initial"])
plt.title("Final vs initial velocity(Vx) from normal distribution")
plt.savefig("Vx.png",dpi =300)
fig = plt.figure()
plt.hist(V2y, bins=50)
plt.hist(v_[0][1],bins=50)
plt.legend(["final","initial"])
plt.title("Final vs initial velocity(Vy) from normal distribution")
fig = plt.figure()
plt.savefig("Vy.png",dpi =300)
plt.hist(V2z, bins=50)
plt.hist(v_[0][2], bins=50)
plt.legend(["final","initial"])
plt.title("Final vs initial velocity(Vz) from normal distribution")
plt.savefig("VZ.png",dpi = 300)
################PLOT OF ENERGY################
fig = plt.figure()

plt.plot(ETOTAL ,label ="ET")
plt.plot(Epot ,label = "EP")
plt.plot(EK ,label = "EK")
plt.title("PLOT OF  ENERGY VS TIME")
plt.xlabel("TIME")
plt.ylabel("ENERGY")
plt.legend()
plt.savefig("energy.png",dpi =300)
fig = plt.figure()
plt.plot(ETOTAL ,label ="ET")
plt.legend()
plt.title("PLOT OF  TOTAL-ENERGY VS TIME")
plt.xlabel("TIME")
plt.ylabel("TOTAL-ENERGY")
plt.savefig("et.png",dpi =300)
fig =plt.figure()
plt.plot(Epot ,label = "EP")
plt.legend()
plt.title("PLOT OF  POTENTIAL-ENERGY VS TIME")
plt.xlabel("TIME")
plt.ylabel("POTENTIAL-ENERGY")
plt.savefig("ep.png",dpi =300)
fig = plt.figure()
plt.plot(EK ,label = "EK")
plt.legend()
plt.title("PLOT OF KINATIC-ENERGY VS TIME")
plt.xlabel("TIME")
plt.ylabel("KINATIC-ENERGY")
plt.savefig("ek.png",dpi=300)

########ANSWER OF QUESTIONS########
'''1)[a]plot for first 500 steps###'''
fig = plt.figure()
plt.plot(ETOTAL[:500] ,label ="ET")
plt.plot(Epot[:500] ,label = "EP")
plt.plot(EK[:500] ,label = "EK")
plt.title("PLOT OF  ENERGY VS TIME\n   first 500 steps")
plt.xlabel("TIME")
plt.ylabel("ENERGY")
plt.legend()
plt.savefig("energyf500.png",dpi =300)
fig = plt.figure()
plt.plot(ETOTAL[:500] ,label ="ET")
plt.legend()
plt.title("PLOT OF  TOTAL-ENERGY VS TIME\n  first 500 step")
plt.xlabel("TIME")
plt.ylabel("TOT-ENERGY")
plt.savefig("etf500.png",dpi =300)
fig = plt.figure()
plt.plot(Epot[:500] ,label = "EP")
plt.legend()
plt.title("PLOT OF  POTENTIAL-ENERGY VS TIME\n   first 500 step")
plt.xlabel("TIME")
plt.ylabel("POT-ENERGY")
plt.savefig("f500ep.png",dpi =300)
fig = plt.figure()
plt.plot(EK[:500] ,label = "EK")
plt.legend()
plt.title("PLOT OF  KINATIC-ENERGY VS TIME\n    first 500 step")
plt.xlabel("TIME")
plt.ylabel("KINATIC-ENERGY")
plt.savefig("f55ek.png",dpi =300)

'''1)[b]plot for last 500 steps###'''
fig = plt.figure()
plt.plot(ETOTAL[-500:] ,label ="ET")
plt.plot(Epot[-500:] ,label = "EP")
plt.plot(EK[-500:] ,label = "EK")
plt.title("PLOT OF  ENERGY VS TIME\n   last 500 steps")
plt.xlabel("TIME")
plt.ylabel("ENERGY")
plt.legend()    
plt.savefig("el500.png",dpi =300)




fig = plt.figure()
plt.plot(ETOTAL[-500:] ,label ="ET")
plt.legend()
plt.title("PLOT OF  TOTAL-ENERGY VS TIME\n  last 500 step")
plt.xlabel("TIME")
plt.ylabel("TOT-ENERGY")
plt.savefig("etl500.png",dpi =300)
fig = plt.figure()
plt.plot(Epot[-500:] ,label = "EP")
plt.legend()
plt.title("PLOT OF  POTENTIAL-ENERGY VS TIME\n   last 500 step")
plt.xlabel("TIME")
plt.ylabel("POT-ENERGY")
plt.savefig("l500ep.png",dpi =300)
fig = plt.figure()
plt.plot(EK[-500:] ,label = "EK")
plt.legend()
plt.title("PLOT OF  KINATIC-ENERGY VS TIME\n    last 500 step")
plt.xlabel("TIME")
plt.ylabel("KINATIC-ENERGY")
plt.savefig("l500ek.png",dpi =300)
'''2)OUTPUT FILE FOR Vcm vs TIME'''
fig = plt.figure()
for i in range(-101):
    plt.plot(V[i][0])
    plt.plot(V[i][1])
    plt.plot(V[i][2])
    plt.title("Vcm vs.Time")
    plt.legend(["VcmX","VcmY","VcmZ"])
    plt.xlim(10e-18)
plt.savefig("Vcm.jpg",dpi =300)
fig = plt.figure()
for i in range(-101):
    plt.plot(V[i][0])
    plt.title("VcmX vs.Time")
    plt.xlabel("VcmX")
    plt.ylabel("time")
    plt.xlim(10e-18)
plt.savefig("Vcmx.png",dpi =300)
fig = plt.figure()
for i in range(-100):
    plt.plot(V[i][1])
    plt.title("VcmY vs.Time")
    plt.xlabel("VcmY")
    plt.ylabel("time")
    plt.xlim(10e-18)
plt.savefig("Vcmy.png",dpi =300)
fig = plt.figure()
for i in range(-101):
    plt.plot(V[i][2])
    plt.title("VcmZ vs.Time")
    plt.xlabel("VcmZ")
    plt.ylabel("time")
    plt.xlim(10e-18)
plt.savefig("Vcmz.png",dpi = 300)
    