from pylab import *
import numpy as np   
import math
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

class lorenz(object):
	def __init__(self,_x,_y,_z,sigma=10.0,r=140,b=2.0,):
		self.x=[_x]
		self.y=[_y]
		self.z=[_z]
		self.t=[0.]
		self.dt=0.0001
		self.b=b
		self.r=r
		self.sigma=sigma
	def calculate(self):
		while self.t[-1]<50 :
			x_=self.sigma*(self.y[-1]-self.x[-1])
			y_=(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
			z_=(self.x[-1]*self.y[-1]-self.b*self.z[-1])
			self.t.append(self.t[-1]+self.dt)
			self.x.append(self.x[-1]+x_*self.dt)
			self.y.append(self.y[-1]+y_*self.dt)
			self.z.append(self.z[-1]+z_*self.dt)
Phase = lorenz(1,0,0)
Phase.calculate()
print Phase.x[-1],Phase.z[-1]
plot(Phase.t,Phase.z,'-',linewidth=1,)
xlabel('time')
ylabel('z')

title('Lorenz model z versus time')
show()