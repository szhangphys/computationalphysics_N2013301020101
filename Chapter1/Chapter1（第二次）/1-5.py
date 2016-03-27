from pylab import *

NA= []
NB= []
t = []
tau = 1
dt = 0.1
NA.append(100.)
NB.append(0.)
t.append(0)
end_time = 4
for i in range(int(end_time / dt)):
	N_A = NA[i] +(NB[i]/tau - NA[i]/tau) * dt
	N_B = NB[i] +(NA[i]/tau - NB[i]/tau) * dt
	NA.append(N_A)
	NB.append(N_B)
	t.append(dt * (i + 1))
	print t[-1], NA[-1],NB[-1]
plot(t,NB, color='purple', linewidth = 1.0,linestyle='--',label='NB')
plot(t,NA, color='purple', linewidth = 1.0,linestyle='-',label='NA')
xlabel('t/s')
ylabel('N')
legend(loc='upper right')
show()
