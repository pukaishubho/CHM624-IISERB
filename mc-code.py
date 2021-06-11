# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:31:11 2020

@author: ABC
"""
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

no_step =int(input("Number of time steps(iterations) you want = "))
n = 108
temp = 1.0
r_cut = 2.5
dens = 0.6
dr_max = 0.15
r_min = 0.75
box = math.pow((n/dens),(1.0/3))
overlap = False


nc = int(((n)/4)**(1/3))
print(nc)
cell = 1/nc
cell2 = 0.5 * cell

### generating translational vector
r = []
r.append([0,0,0])
r.append([cell2,cell2,0])
r.append([0,cell2,cell2])
r.append([cell2,0,cell2])
### translation of vectors:
at = ['Ar']
r1 = []
for k in range(nc):
	for j in range(nc):
		for i in range (nc):
			for iref in range(4):
				r1.append(r[iref] + cell*np.array([i,j,k]))
R = []

for i in range(108):
    R.append(r1[i] -np.array([round(num)for num in r1[i]]) )
        
R1 = np.array(R)
#print(R1)                
                
                
                
                
                
                

def potential(R,box, r_min, r_cut):
    global overlap
    pot = 0
    sr2_ovr = 1/(r_min*r_min)
    r_cut_box = r_cut/box
    r_cut_box_sq = r_cut_box * r_cut_box
    if ( r_cut_box > 0.5 ):
        sys.exit('r_cut/box too large1')
    box_sq=box * box
    for i in range(n-1):
        for j in range((i+1),n):
            Rij = R[i] - R[j]
            Rij = Rij - np.array([round(num)for num in Rij])
            Rij_sq = sum( Rij**2)
            if (Rij_sq < r_cut_box_sq):
                Rij_sq = Rij_sq * box_sq
                sr2 = 1.0 / Rij_sq
                if (sr2 > sr2_ovr):
                    overlap = True
                    continue
                sr6	= sr2 ** 3
                sr12 = sr6 ** 2
                pair_pot = 4*(sr12 - sr6)
                pot = pot + pair_pot
    return(pot)
#############################################################################    

def potential_1(Ri,i,box, r_min, r_cut):
    global overlap
    overlap = False
    partial_pot = 0
    r_cut_box = r_cut/box
    if ( r_cut_box > 0.5):
        sys.exit('r_cut/box too large2')
    sr2_ovr = 1/(r_min*r_min)
    r_cut_box_sq = r_cut_box * r_cut_box
    box_sq=box * box
    for j in range(0,108):
        if ((i != j)):
            Rij = Ri - R1[j]
            Rij = Rij - np.array([round(num)for num in Rij])
            Rij_sq = sum( Rij**2)
            if (Rij_sq < r_cut_box_sq):
                Rij_sq = Rij_sq * box_sq
                sr2 = 1.0 / Rij_sq
                if (sr2 > sr2_ovr):
                    overlap = True
                    continue
                sr6	= sr2 ** 3
                sr12 = sr6 ** 2
                pot = 4*(sr12 - sr6)
                partial_pot = partial_pot + pot
    return(partial_pot)
'''for i in range(108):
    partial_pot = potential_1(R1[i],i,box, r_min, r_cut,overlap)
    print(partial_pot)'''
#############################################################################

def random_translate_vector (dr_max, old):
    
    zeta = np.random.uniform(0,1,size = 3)
    zeta = 2*zeta - 1
    r_new = old[i] + zeta * dr_max/box
    return(r_new)


################################################################################
def metropolis (delta):
    
    exponent_guard=75.0
    if (delta > exponent_guard ):
    	accept = False
    elif ( delta < 0.0 ):
    	accept = True
    else:
        zeta = np.random.uniform(0,1)
        accept = math.exp(-delta) > zeta
    return(accept)

######main code##############################################################
##2.calculate energy and check for overap
pot =  potential(R1,box, r_min, r_cut)
print(overlap)
if (overlap):
    sys.exit("overlap in initial configaretion")
PE =[pot]
PE_n = []
#print(PE)

ntraial = 0
acpot_sq = 0
acpot = 0
prt_tag = 1
f = open('mc100k.txt','w')
f2 = open("pe.txt",'w')
f3 = open("pen.txt",'w')
f.write('%s %8s %8s\n'%('ntraial','move_ratio','potn'))

for stp in range(no_step):
    
    moves = 0
    for i in range(n):
        partial_pot_old = potential_1 (R1[i],i,box, r_min, r_cut)
        
        
        if overlap:
 #           continue
            sys.exit('overlap')

            
        
        R_new =  random_translate_vector(dr_max,R1)
        
        R_new = R_new- np.array([round(num)for num in R_new])
        
        partial_pot_new = potential_1(R_new,i,box, r_min, r_cut)
#        print(partial_pot_new)
        if(not(overlap)):
            delta =(partial_pot_new-partial_pot_old)/temp
            if metropolis(delta):
                pot =pot + (partial_pot_new-partial_pot_old)
                R1[i] = R_new
                moves = moves + 1
        
        ntraial += 1
        potn =pot/int(n)
        acpot = acpot + potn
        acpot_sq = acpot_sq + potn*potn        
#        print('pot =',pot)
    move_ratio = moves/float(n)
    if(move_ratio > 0.55):
        dr_max = dr_max *1.05
    elif(move_ratio < 0.45):
        dr_max = dr_max*0.95
        
    if((stp%prt_tag)==0):
        PE.append(pot)
        PE_n.append(potn)
        f.write('%s %10.6s %10.6f\n'%(ntraial,move_ratio,potn))
        f.write("\n")
       
        f2.write('%10.6f\n'%pot)
        
        f3.write('%10.6f\n'%potn)
    print('step = ',stp)
    print(potn)
f2.close()
f3.close()

pot_av = acpot/ntraial
acpot_sq = (acpot_sq/ntraial) - pot_av*pot_av
f.write("pot_av = %f\n"%pot_av)
print(pot_av)

if(acpot_sq>0):
    flv = np.sqrt(acpot_sq)
f.write("flv = %f"%flv)
f1 = open("final-position.txt","w")
f1.write("%s %5s %10s %10s\n" %("atom", "X", "Y", "Z"))
at = ['Ar']
R1 = R1 * box
for i in range (108):
    f1.write("%s %10.6f %10.6f %10.6f\n"%((at[0]), R1[i][0], R1[i][1], R1[i][2]))
f.close()
f1.close()
    
                          
###################plot##################################################               
fig = plt.figure()
plt.plot(PE,label ='potential energy' )
plt.xlabel("mc-steps")
plt.ylabel("potential energy")
plt.savefig('PE.png')


fig = plt.figure()
plt.plot(PE_n,label ='potential energy per partical' )
plt.xlabel("mc-steps")
plt.ylabel("PE per partical")
plt.savefig('PE_n.png')              
    
    
    