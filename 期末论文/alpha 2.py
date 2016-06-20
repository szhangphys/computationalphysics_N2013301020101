import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d 
from math import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
class solar:
    def __init__(self,  l=4.0558/10**26,end = 10,  Gms = 1 ,pos_1 =array([3.,0.,0.]),pos_2=array([-100.,-0.,0.]) ,  dt = 0.001 ):
        self.m_2 = 4*1.673/10**27
        self.l=l
        self.n = int(end / dt)
        self.dt = dt
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.v_1 = array([0.,0.,0.])
        self.v_2 = array([10.,0.,0.])
        self.x_1 = []
        self.y_1 = []
        self.z_1 = []
        self.x_2 = []
        self.y_2 = []
        self.z_2 = []
        self.d=[]
    def calculate(self):
        for i in range(self.n):
            d = inner(self.pos_1-self.pos_2, self.pos_1 - self.pos_2)
            self.d.append(d)
            self.a_1 =  0
            self.a_2 = (self.l/self.m_2)*(self.pos_2 - self.pos_1)/(d** (3 / 2.))
            self.v_1 +=self.a_1 * self.dt
            self.v_2 +=self.a_2 * self.dt
            self.pos_1 +=self.v_1 * self.dt
            self.pos_2 +=self.v_2 * self.dt
            self.x_1.append(self.pos_1[0])
            self.y_1.append(self.pos_1[1])
            self.z_1.append(self.pos_1[2])
            self.x_2.append(self.pos_2[0])
            self.y_2.append(self.pos_2[1])
            self.z_2.append(self.pos_2[2])  
        print min(self.y_2),min(self.d)

ax=plt.subplot(111,projection='3d')

for a in (-3,-1,-0.5,-0.1,0,0.1,0.5,1,3):
    binary = solar(pos_2 = array([-20.,a,0.4*a]),)
    binary.calculate()
    print a, len(binary.x_2), binary.x_2[6000:6010]
    #print binary.y_2
    ax.plot(binary.x_2,binary.y_2,binary.z_2) #,rstride=2,cstride=1,cmap=plt.cm.coolwarm,alpha=1)
    ax.plot(binary.x_1,binary.y_1,binary.z_1,'.',color = 'red')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_zlim(-2,2)
    ax.set_xlim(-10,10)
    ax.set_ylim(-10,10)

title('scattering')
plt.show()    

