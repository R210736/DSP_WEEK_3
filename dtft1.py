import numpy as np
import matplotlib.pyplot as plt
def dtft(x):
	n=len(x)
	w=np.linspace(-np.pi,np.pi,n) #frequency vector to create n evenly spaced  points b/w -pi to pi
	X=np.zeros(n) #initialize dtft array X
	for k in range(n):
		X[k]=np.sum(x*np.exp(-1j*k*w))
	return X,w
x=np.array([1,2,3,4,5])
X,w=dtft(x)
plt.subplot(121)
plt.plot(w,np.abs(X))
plt.xlabel("Frequency")
plt.ylabel('magnitude')
plt.title('magnitude spectrum')

plt.subplot(122)
plt.plot(w,np.angle(X))
plt.xlabel("Frequency")
plt.ylabel('phase')
plt.title('phase spectrum')
plt.show()
