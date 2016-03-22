from pylab import *

N= []
t = []
a = 10
dt = 1
N.append(100.)
t.append(0)
end_time = 100
for i in range(int(end_time / dt)):
	N_P = N[i] + a  * N[i]  * dt
	N.append(N_P)
	t.append(dt * (i + 1))
	print t[-1], N[-1]
plot(N, color='purple', linewidth = 1.0,linestyle='-')
show()

