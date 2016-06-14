from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
reload(sys)
sys.setdefaultencoding('gb18030')
N=60
accuracy=1e-5
class Fields:
    def __init__(self):
        self.v=[]
        self.pre_v=[]
        for i in range(N):
            self.v.append([])
            self.pre_v.append([])


        for i in range(N):
            for j in range(N):
                self.v[i].append(random.uniform(-1,1))
                self.pre_v[i].append(0)
    def update(self):
        for i in range(N):
            self.v[i][0]=0
            self.v[i][N-1]=0
        for j in range(N):
            self.v[0][j]=0
            self.v[N-1][j]=0
        for i in range(N/4,3*N/4):
            self.v[i][N/4]=1
            self.v[i][3*N/4]=-1
        self.dv=0.
        for i in range(N):
            for j in range(N):
                self.pre_v[i][j]=self.v[i][j]
        for i in range(1,N-1):
            for j in range(1,N-1):
                if ((j==N/4 and (i in range(N/4,3*N/4))) or (j==3*N/4 and (i in range(N/4,3*N/4)))):
                    pass
                else:
                    self.v[i][j]=(self.pre_v[i+1][j]+self.pre_v[i-1][j]+self.pre_v[i][j+1]+self.pre_v[i][j-1])/4.

                self.dv+=abs(self.pre_v[i][j]-self.v[i][j])
        print self.dv
    def Ele_field(self,x1,x2,y1,y2):       # calculate the Electirc field  
        self.dx=abs(x1-x2)/float(self.n-1)
        self.Ex=[]
        self.Ey=[]
        for j in range(self.n):
            self.Ex.append([0.0]*self.n)
            self.Ey.append([0.0]*self.n)
        for j in range(1,self.n-1,1):
            for i in range(1,self.n-1,1):
                self.Ex[j][i]=-(self.V[j][i+1]-self.V[j][i-1])/(2*self.dx)
                self.Ey[j][i]=-(self.V[j-1][i]-self.V[j+1][i])/(2*self.dx)
    def plot_2(self,ax1,ax2,x1,x2,y1,y2):     # give 2d plot of potential and electric field
        self.x=linspace(x1,x2,self.n)
        self.y=linspace(y2,y1,self.n)
        self.x,self.y=meshgrid(self.x,self.y)
        
        cs=ax1.contour(self.x,self.y,self.V)
        plt.clabel(cs, inline=1, fontsize=10)
        ax1.set_title('Equipotential lines',fontsize=18)
        ax1.set_xlabel('x (m)',fontsize=14)
        ax1.set_ylabel('y (m)',fontsize=14)
        
        for j in range(1,self.n-1,1):
            for i in range(1,self.n-1,1):
                ax2.arrow(self.x[j][i],self.y[j][i],self.Ex[j][i]/40,self.Ey[j][i]/40,fc='k', ec='k')             
        ax2.set_xlim(-1.,1.)
        ax2.set_ylim(-1.,1.)
        ax2.set_title('Electric field',fontsize=18)
        ax2.set_xlabel('x (m)',fontsize=14)
        ax2.set_ylabel('y (m)',fontsize=14)

    def fire(self):
        self.dv=1
        while (self.dv>=accuracy):
            self.update()
        return self.v
finnal=Fields()
distribution=finnal.fire()

fig = plt.figure()
ax = fig.gca(projection='3d')
x=range(N)
y=range(N)
x, y = np.meshgrid(x, y)
surf = ax.plot_surface(x, y, distribution, rstride=1, cstride=1, cmap=cm.jet,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
plt.xlabel("X")
plt.ylabel("Y")
plt.title('Electric Field')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()