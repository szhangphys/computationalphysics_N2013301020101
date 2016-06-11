from math import *
import numpy as np
from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
class solar:
    def __init__(self, beta = 3.0, end = 5,  Gms = 4*pi , k=0.5, v_2 = array([0.,-1/3.99,0.]),pos_1 =array([1.,0.,0.]), pos_2 = array([-1.,0.,0.]), v_1 = array([0.,1.,0.]), dt = .0001 ):
        self.m_1 = Gms
        self.m_2 = k*Gms
        self.beta = beta
        self.n = int(end / dt)
        self.dt = dt
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.v_1 = v_1
        self.v_2 = v_2
        self.x_1 = []
        self.y_1 = []
        self.z_1 = []
        self.x_2 = []
        self.y_2 = []
        self.z_2 = []
    def calculate(self):
        for i in range(self.n):
            d = inner(self.pos_1-self.pos_2, self.pos_1 - self.pos_2)
            self.a_1 =  self.m_2 * (self.pos_2 - self.pos_1)/d ** ((self.beta) / 2.)
            self.a_2 = self.m_1 * (self.pos_1 - self.pos_2)/d** ((self.beta) / 2.)
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
 
binary = solar(beta=3.0,k=3.99)
binary.calculate()
plot(binary.x_1,binary.y_1,label="planet $m_{1}$",color='purple')
plot(binary.x_2,binary.y_2,label="planet $m_{2}$",color='red')
title("binary in CM")
xlabel('x/AU')
ylabel('y/AU')
legend(loc="best")
legend(loc = 'best')
show()
