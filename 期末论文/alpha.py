from math import *
import numpy as np
from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
class solar:
    def __init__(self,  l=4.0558/10**26,end = 10, pos_1 =array([0.,3.,0.]),pos_2=array([0.,-100.,0.]) ,  dt = 0.001 ):
        self.m_2 = 4*1.673/10**27
        self.l=l
        self.n = int(end / dt)
        self.dt = dt
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.v_1 = array([0.,0.,0.])
        self.v_2 = array([0.,100.,0.])
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



for a in (-3,-1,-0.5,-0.1,0,0.1,0.5,1,3):
    binary = solar(pos_2 = array([a,-20.,0.]),)
    binary.calculate()
    #print binary.x_2,
    #print binary.y_2
    plot(binary.x_2,binary.y_2,'-',label="x="+str(a),)
plot(binary.x_1,binary.y_1,'.',label="planet $m_{1}$",color='purple')


title("scattering")
xlabel('x/m')
ylabel('y/m')
#ylim(-10,10)
xlim(-7,7)
legend(loc="best")
legend(loc = 'best')
show()
