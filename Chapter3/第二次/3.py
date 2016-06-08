from pylab import *
import numpy as np   
import math
import sys
reload(sys)
sys.setdefaultencoding('gb18030')


class Harmonic(object):
    def __init__(self,_t, _omega, _theta,omega_D=2.0/3.0,):
        self.t=[_t]
        self.l=9.8
        self.omga_D=2.0/3.0
        self.m=0.5
        self.g=9.8
        self.omega=[_omega]
        self.theta=[a]
        self.end_time=800*math.pi/omega_D
        self.dt=0.04
        self.chosen_omega=[]
        self.chosen_theta=[]
        self.chosen_t=[]
    def calculate(self):
        for i in range(int(self.end_time/self.dt)):
            Omega1=self.omega[i]-(self.g/self.l*math.sin(self.theta[i])+self.m*self.omega[i]-F_D*math.sin(self.omga_D*self.t[i]))*self.dt
            self.omega.append(Omega1)
            theta1=self.theta[i]+self.omega[i+1]*self.dt
            self.t.append(self.t[i]+self.dt)
            while theta1>math.pi:
                theta1=theta1-2*math.pi
            else:
                theta1=theta1
            while theta1<-math.pi:
                theta1=theta1+2*math.pi
            else:
                theta1=theta1
            self.theta.append(theta1)
finnal_F_D=[]
finnal_theta=[]
F_D0=1.40
for a in range(1,1000):
    F_D=F_D0+0.0001*a
    trejectory = Harmonic(_t=0,_omega=0,_theta=0.2)
    trejectory.calculate()
    print trejectory.t[-1], trejectory.theta[-1],F_D
    finnal_F_D.append(F_D)
    finnal_theta.append(trejectory.theta[-1])
scatter(finnal_F_D,finnal_theta, linestyle='-' ,s=1)
title('bifurcation diagram',fontsize=15)
xlabel('F_D')
ylim(0,3.5)
ylabel('theta(rad)')
show()
