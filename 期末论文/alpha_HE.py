import numpy as np  
from math import *
from pylab import *
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
import matplotlib.pyplot as plt  
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
plt.figure(1,figsize=(10,5))

ax1=plt.axes([0.1,0.1,0.35,0.7])
ax2=plt.axes([0.6,0.1,0.35,0.7])
for a in (-3,-1,-0.5,-0.1,0,0.1,0.5,1,3):
    binary = solar(pos_2 = array([-20.,a,0.]),)
    binary.calculate()
    #print binary.x_2,
    #print binary.y_2
    plt.figure(1)  
    plt.sca(ax1) 
    plt.plot(binary.x_2,binary.y_2,'-',label="y="+str(a),)
    plt.title("scattering")
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.legend(loc="best")
    leg = plt.gca().get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize='small')
    plt.plot(binary.x_1,binary.y_1,'.',color='purple')
    plt.sca(ax2) 
    plt.plot(binary.x_2,binary.y_2,'-',label="y="+str(a),)
    plt.title("local amplify scattering")
    plt.xlabel('x/m')
    plt.ylabel('y/m')
    plt.xlim(-5,15)
    plt.ylim(-7,7)
    plt.legend(loc="best")
    leg = plt.gca().get_legend()
    ltext  = leg.get_texts()
    plt.setp(ltext, fontsize='small')
    plt.plot(binary.x_1,binary.y_1,'.',color='purple')
    r1 = 0.0912665
    theta = np.linspace(0,2*np.pi,36)
    x1 = r1*np.cos(theta)+3
    y1 = r1*np.sin(theta)
    plt.plot(x1,y1,'--')
    plt.fill(x1,y1,'y')
plt.plot(binary.x_1,binary.y_1,'.',label="$Cu_{1}$",color='purple') 

show()
