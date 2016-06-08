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

F_D=1.2
for a in(0.2,):
    trejectory = Harmonic(_t=0,_omega=0,_theta=a)
    trejectory.calculate()
    print trejectory.theta[0],trejectory.omega[0]
    plot(trejectory.theta,trejectory.omega, ',' )
    xlabel('$\\theta$(rad)')
    ylabel('$\\omega$(rad/s)')
    title('$\\omega$ versus $\\theta$   $F_D$=1.2')
    show()
