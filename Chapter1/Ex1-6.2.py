from pylab import *

N= []
t = []
a = 10
b =0.01
dt = 0.01
N.append(100.)
t.append(0)
end_time = 1
for i in range(int(end_time / dt)):
	N_P = N[i] + (a  * N[i]-b* N[i]* N[i])  * dt
	N.append(N_P)
	t.append(dt * (i + 1))
	print t[-1], N[-1]
plot(N, color='blue', linewidth = 2.0)
show()

