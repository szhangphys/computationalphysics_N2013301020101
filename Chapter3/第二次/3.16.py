from pylab import *
import numpy as np   
import math
import sys
reload(sys)
sys.setdefaultencoding('gb18030')



class Harmonic(object):
    def __init__(self,_t, _omega, _theta, g=0,l=1,m=1,F_D=0,omga_D=0,_dt=0.1):
        self.t=[_t]
        self.l=1
        self.F_D=0
        self.omga_D=0
        self.m=1
        self.g=0
        self.omega=[_omega]
        self.theta=[a]
        self.end_time=10
        self.dt=0.1
    def calculate(self):
        for i in range(int(self.end_time/self.dt)):
        	self.omega.append(self.omega[i]-(self.g/self.l*math.sin(self.theta[i])-self.m*self.omega[i]+self.F_D*math.sin(self.omga_D*self.t[i]))*self.dt)
            theta1=self.theta[i]+self.omega[i+1] *self.dt
        	self.t.append(self.dt*(i+1))
            while theta1>math.pi:
                theta1=theta12*math.pi
            while theta1<-math.pi:
                theta1=theta1+2*math.pi
            self.theta.append(theta1)



for a in (0.1,):
    trejectory = Harmonic(0,0,_theta=a)
    trejectory.calculate()
    print trejectory.t[-1], trejectory.theta[-1]
    plot(trejectory.t,trejectory.theta, linestyle='-',label ="$\\theta_0$=" +str(a))
xlabel('time(s)')
ylabel('$\\theta$(rad)')
title('$\\theta-t$')
legend(loc="upper right")
show()
class Harmonic(object):
    def __init__(self,_t, _omega, _theta, g=0,l=1,m=1,F_D=0,omga_D=0,_dt=0.1):
        self.t=[_t]
        self.l=1
        self.F_D=0
        self.omga_D=0
        self.m=1
        self.g=0
        self.omega=[_omega]
        self.theta=[a]
        self.end_time=10
        self.dt=0.1
    def calculate(self):
        for i in range(int(self.end_time/self.dt)):
            self.omega.append(self.omega[i])
            theta1=self.theta[i]+self.omega[i+1] *self.dt
            self.t.append(self.dt*(i+1))
            while theta1>3:
                theta1=theta12*math.pi
            while theta1<-3:
                theta1=theta1+2*math.pi
            self.theta.append(theta1)



for a in (0.1,):
    trejectory = Harmonic(0,0,_theta=a)
    trejectory.calculate()
    print trejectory.t[-1], trejectory.theta[-1]
    plot(trejectory.t,trejectory.theta, linestyle='-',label ="$\\theta_0$=" +str(a))
xlabel('time(s)')
ylabel('$\\theta$(rad)')
title('$\\theta-t$')
legend(loc="upper right")
show()
F_D=1.35
for a in (0.1,):
    trejectory = Harmonic(0,0,_theta=a)
    trejectory.calculate()
    print trejectory.t[-1], trejectory.theta[-1]
    plot(trejectory.t,trejectory.theta, linestyle='-',label ="$\\theta_0$=" +str(a))
    show()



'''
finnal_theta=[]
finnal_F_D=[]
F_=[]
F_D0=1.2

for a in range(0,100):
    F_D=F_D0+a*0.001
    trejectory = Harmonic(_t=0, _omega=0, _theta=0.2)
    trejectory.calculate()
    F_.append(F_D)

    print trejectory.t[-1], trejectory.theta[-1]
    finnal_theta.append(trejectory.theta[-1])
    finnal_F_D.append(F_[-1])
    print finnal_F_D,finnal_theta

scatter(finnal_F_D,finnal_theta,)
xlabel('F_D')
ylabel('$\\theta$(rad)')
title('$\\theta-t$')
legend(loc="upper right")
show()