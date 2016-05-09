import numpy as np   
import math
import matplotlib.pyplot as plt

class BASEBALL(object):
    def __init__(self, _vx0, _vy0, _vz0, _dt= 0.1, _omgx=0,_omgy=0,_omgz=0):
        self.vx, self.vy, self.vz= _vx0, _vy0, _vz0     
        self.v = math.sqrt(_vx0**2+ _vy0**2+ _vz0**2)
        self.B2= 0.0039+ 0.0058/(1.+math.exp((self.v-35)/5))
        self.S0= 4.1E-4
        self.g= 9.8
        self.dt= _dt 
        self.x, self.y, self.z= [0], [1.8], [0]
        self.omgx, self.omgy, self.omgz= _omgx, _omgy, _omgz 
    def calculate(self):
        while True: 
            self.x.append(self.vx*self.dt+self.x[-1])   
            self.y.append(self.vy*self.dt+self.y[-1])
            self.z.append(self.vz*self.dt+self.z[-1])   
            self.vx, self.vy, self.vz = \
                (-self.B2*self.v*self.vx+ self.S0*self.vy*self.omgz)*self.dt+ self.vx, \
                (-self.g- self.B2*self.v*self.vy+ self.S0*self.vz*self.omgx)*self.dt+ self.vy,\
                (self.S0*self.vx*self.omgy)*self.dt+ self.vz                         # change the velocity
            self.v= math.sqrt(self.vx**2+self.vy**2+self.vz**2)
            self.B2= 0.0039+ 0.0058/(1.+math.exp((self.v-35)/5))
            if self.y[-1]< 0: 
                break



for q in (-2000,-1000,-200,209, 2000,20000):
    trejectory_with = BASEBALL(50, 50, 0 ,_omgx=0,_omgy=0,_omgz=q )

    trejectory_with.calculate()
    print trejectory_with.x,'\n\n\n',  trejectory_with.y, '\n\n\n', trejectory_with.z
    plt.plot(trejectory_with.x, trejectory_with.y,label = "$\omega _z$ = "+str(q)+'rad\s')
    plt.legend(loc="upper right")
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
plt.show()