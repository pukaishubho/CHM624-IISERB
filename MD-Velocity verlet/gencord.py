import numpy as np

#### declearing variables
#total no of atoms in unit cell = 4*nc**3
#length of each unit cell =cell
#nc = int(input("Enter no of unit cell:"))
n_atom = 108

nc = int(((n_atom)/4)**(1/3))
print(nc)
cell = 1/nc
cell2 = 0.5 * cell
BOXL =(n_atom)**(1/3)
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
r2=[]
R = np.zeros([108,3])




for i in range(len(r1)):
    r2.append(r1[i]*BOXL)
print(r2)    
rX = []
rY = []
rZ = []
for i in range (n_atom):
    rX.append(r2[i][0])
    rY.append(r2[i][1])
    rZ.append(r2[i][2])
    
RX = np.array(rX)
RY = np.array(rY)
RZ = np.array(rZ)   
		
