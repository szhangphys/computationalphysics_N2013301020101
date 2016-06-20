import numpy as np   
import math
import matplotlib.pyplot as plt
'''
class BASEBALL(object):
    def __init__(self, _vx0=1, _vy0=0, _vz0=0, _dt= 0.1, ):
        self.vx, self.vy, self.vz= _vx0, _vy0, _vz0     
        self.v = math.sqrt(_vx0**2+ _vy0**2+ _vz0**2)
        self.B2= 0.0039+ 0.0058/(1.+math.exp((self.v-35)/5))
        self.S0= 4.1E-4
        self.g= 9.8
        self.x0=1
        self.y0=0
        self.z0=0
        self.dt= _dt 
        self.x, self.y, self.z= [a], [0], [0]
        self.d=math.sqrt(self.x[0]**2+ self.y[0]**2+ self.z[0]**2)

    def calculate(self):
        while True: 
            self.x.append(self.vx*self.dt+self.x[-1])   
            self.y.append(self.vy*self.dt+self.y[-1])
            self.z.append(self.vz*self.dt+self.z[-1])  
            self.d=math.sqrt(self.x[-1]**2+ self.y[-1]**2+ self.z[-1]**2) 
            self.vx, self.vy, self.vz = \
                (-1 * (self.x[-1] - self.x0)/self.d** 3)*self.dt+ self.vx, \
                (-1 * (self.y[-1] - self.y0)/self.d** 3)*self.dt+ self.vy,\
                (-1 * (self.z[-1] - self.z0)/self.d** 3)*self.dt+ self.vz                         # change the velocity
            self.v= math.sqrt(self.vx**2+self.vy**2+self.vz**2)
            if self.y[-1]< 0: 
                break



for a in (0.0,0.1):
    trejectory_with = BASEBALL(50, 50, 0 ,)

    trejectory_with.calculate()
    print trejectory_with.x,'\n\n\n',  trejectory_with.y, '\n\n\n', trejectory_with.z
    plt.plot(trejectory_with.x, trejectory_with.y,label = "$\omega _z$ = "+str(q)+'rad\s')
    plt.legend(loc="upper right")
    plt.xlabel('x(m)')
    plt.ylabel('y(m)')
plt.show()
'''
x=[1,2,3]
print max(x)
'''
'''
from math import *
import numpy as np
from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
class solar:
    def __init__(self,  l=4.0558/10**26,end = 10, ,pos_1 =array([0.,3.,0.]),pos_3 =array([0.,3.+10**-10,0.]),pos_2=array([0.,-100.,0.]) ,  dt = 0.0001 ):
        self.m_2 = 4*1.673/10**27
        self.l=l
        self.n = int(end / dt)
        self.dt = dt
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.pos_3 = pos_3
        self.v_1 = array([0.,0.,0.])
        self.v_2 = array([0.,10.,0.])
        self.x_1 = []
        self.y_1 = []
        self.z_1 = []
        self.x_2 = []
        self.y_2 = []
        self.z_2 = []
        self.x_3 = []
        self.y_3 = []
        self.z_3 = []
        self.d=[]
    def calculate(self):
        for i in range(self.n):
            d1 = inner(self.pos_1-self.pos_2, self.pos_1 - self.pos_2)
            d2 = inner(self.pos_3-self.pos_2, self.pos_1 - self.pos_2)
            self.d.append(d)
            self.a_1 =  0
            self.a_2 = (self.l/self.m_2)*(self.pos_2 - self.pos_1)/(d1** (3 / 2.))
            self.a_3 = (self.l/self.m_2)*(self.pos_2 - self.pos_3)/(d2** (3 / 2.))
            self.v_1 +=self.a_1 * self.dt
            self.v_2 +=(self.a_2+self.a_3) * self.dt
            self.pos_1 +=self.v_1 * self.dt
            self.pos_2 +=self.v_2 * self.dt
            self.x_1.append(self.pos_1[0])
            self.y_1.append(self.pos_1[1])
            self.z_1.append(self.pos_1[2])
            self.x_2.append(self.pos_2[0])
            self.y_2.append(self.pos_2[1])
            self.z_2.append(self.pos_2[2])  
            self.x_3.append(self.pos_3[0])
            self.y_3.append(self.pos_3[1])
            self.z_3.append(self.pos_3[2])
        print min(self.y_2),min(self.d)


for a in (-1,0,1):
    binary = solar(pos_2 = array([a,-20.,0.]),)
    binary.calculate()
    #print binary.x_2,
    #print binary.y_2
    plot(binary.x_2,binary.y_2,'-',label="x="+str(a),)
plot(binary.x_1,binary.y_1,'.',label="planet $m_{1}$",color='purple')
plot(binary.x_3,binary.y_3,'.',label="planet $m_{1}$",color='purple')
title("scattering")
xlabel('x/m')
ylabel('y/m')
#ylim(-10,10)
xlim(-7,7)
legend(loc="best")
legend(loc = 'best')
show()
