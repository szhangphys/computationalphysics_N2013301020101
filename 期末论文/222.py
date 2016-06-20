import numpy as np  
from math import *
from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
import matplotlib.pyplot as plt  



class solar:
    def __init__(self,  l=4.0558/10**26,end = 20, pos_1 =array([0.,3.,0.]),pos_4 =array([0.6,5.,0.]),pos_5 =array([0.4,5.,0.]),pos_3 =array([+1,3.,0.]),pos_2=array([0.,-100.,0.]) ,  dt = 0.0001 ):
        self.m_2 = 4*1.673/10**27
        self.l=l
        self.n = int(end / dt)
        self.dt = dt
        self.pos_1 = pos_1
        self.pos_2 = pos_2
        self.pos_3 = pos_3
        self.pos_4 = pos_4
        self.pos_5 = pos_5
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
        self.x_4 = []
        self.y_4 = []
        self.z_4 = []
        self.x_5 = []
        self.y_5 = []
        self.z_5 = []
        self.d=[]
    def calculate(self):
        for i in range(self.n):
            d1 = inner(self.pos_1-self.pos_2, self.pos_1 - self.pos_2)
            d2 = inner(self.pos_3-self.pos_2, self.pos_3 - self.pos_2)
            d3 = inner(self.pos_4-self.pos_2, self.pos_4 - self.pos_2)
            d4 = inner(self.pos_5-self.pos_2, self.pos_5 - self.pos_2)
            self.d.append(d1)
            self.a_1 =  0
            self.a_2 = (self.l/self.m_2)*(self.pos_2 - self.pos_1)/(d1** (3 / 2.))
            self.a_3 = (self.l/self.m_2)*(self.pos_2 - self.pos_3)/(d2** (3 / 2.))
            self.a_4 = (self.l/self.m_2)*(self.pos_2 - self.pos_4)/(d3** (3 / 2.))
            self.a_5 = (self.l/self.m_2)*(self.pos_2 - self.pos_5)/(d4** (3 / 2.))
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
            self.x_4.append(self.pos_4[0])
            self.y_4.append(self.pos_4[1])
            self.z_4.append(self.pos_4[2])
            self.x_5.append(self.pos_5[0])
            self.y_5.append(self.pos_5[1])
            self.z_5.append(self.pos_5[2])
        print min(self.y_2),min(self.d)

plt.figure(1)
ax1=plt.subplot(211)
ax2=plt.subplot(212)
for a in (0.5,0.6):
    binary = solar(pos_2 = array([a,-20.,0.]),)
    binary.calculate()
    #print binary.x_2,
    #print binary.y_2
    plt.figure(1)  
    plt.sca(ax1) 
    plt.plot(binary.x_1,binary.y_1,'.',label="$Cu_{1}$",color='purple')
    plt.plot(binary.x_3,binary.y_3,'.',label="$Cu_{2}$",color='black')
    plt.plot(binary.x_4,binary.y_4,'.',label="$Cu_{3}$",color='yellow')
    plt.plot(binary.x_5,binary.y_5,'.',label="$Cu_{4}$",color='green')
    plt.plot(binary.x_2,binary.y_2,'-',label="x="+str(a),)

    plt.sca(ax2)
    plt.plot(binary.x_1,binary.y_1,'.',label="$Cu_{1}$",color='purple')
    plt.plot(binary.x_3,binary.y_3,'.',label="$Cu_{2}$",color='black')
    plt.plot(binary.x_4,binary.y_4,'.',label="$Cu_{3}$",color='yellow')
    plt.plot(binary.x_5,binary.y_5,'.',label="$Cu_{4}$",color='green')   
    plt.plot(binary.x_2,binary.y_2,'-',label="x="+str(a),)




show()


fig=plt.figure(figsize=(10,5)) 
ax1=plt.axes([0.1,0.1,0.35,0.7])
ax2=plt.axes([0.6,0.1,0.35,0.7])
ax1.set_xlim(-5,15)
ax1.set_ylim(-7,7)
ax2.set_xlim(-5,15)
ax2.set_ylim(-7,7)
ax1.set_xlabel('x/m')
ax1.set_ylabel('y/m')
ax2.set_xlabel('x/m')
ax2.set_ylabel('y/m')
ax1.set_title("$\\alpha scattering$",fontsize=18)
ax2.set_title('$\\alpha scattering$',fontsize=18)
ax1.plt.legend(loc="best")
ax1.leg = plt.gca().get_legend()
ax1.ltext  = leg.get_texts()
ax1.plt.setp(ltext, fontsize='small')
ax2.plt.legend(loc="best")
ax2.leg = plt.gca().get_legend()
ax2.ltext  = leg.get_texts()
ax2.plt.setp(ltext, fontsize='small')