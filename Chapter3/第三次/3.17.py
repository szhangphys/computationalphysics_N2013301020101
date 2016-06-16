from pylab import *
import numpy as np   
import math
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

class lorenz(object):
	def __init__(self,_x,_y,_z,sigma=10.0,r=25,b=8.0/3.0,):
		self.x=[_x]
		self.y=[_y]
		self.z=[_z]
		self.newx=[_x]
		self.newy=[_y]
		self.newz=[_z]
		self.t=[0.]
		self.dt=0.0001
		self.b=b
		self.r=r
		self.sigma=sigma
	def calculate(self):
		while self.t[-1]<500 :
			x_=self.sigma*(self.y[-1]-self.x[-1])
			y_=(-self.x[-1]*self.z[-1]+self.r*self.x[-1]-self.y[-1])
			z_=(self.x[-1]*self.y[-1]-self.b*self.z[-1])
			self.t.append(self.t[-1]+self.dt)
			self.x.append(self.x[-1]+x_*self.dt)
			self.y.append(self.y[-1]+y_*self.dt)
			self.z.append(self.z[-1]+z_*self.dt)
			if (self.t[-1]<30):
			     if(abs(self.y[-1]+y_*self.dt)<0.5):
			     	self.newx.append(self.x[-1]+x_*self.dt)
			     	self.newz.append(self.z[-1]+z_*self.dt)
			     else:
				 	pass
			else:
				pass
Phase = lorenz(1,0,0)
Phase.calculate()
print Phase.newx[-1],Phase.newz[-1]
plot(Phase.newx,Phase.newz,',',linewidth=2,)
xlabel('x')
ylabel('z')

title('Phase space plot:z versus x')
show()

