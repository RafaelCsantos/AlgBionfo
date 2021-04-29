import numpy as np
import matplotlib.pyplot as plt

#criando vetor:
v=np.arange(-2*np.pi,2*np.pi,2*np.pi/30)

#plotando a função seno

sen=np.sin(v)
plt.plot(v,sen,color='r')
plt.xlim(-2*np.pi,2*np.pi)
plt.title("função seno (x)")
plt.show()

#plotando a função cosseno
cos=np.cos(v)
plt.fill_between(v,cos)
plt.xlim(-2*np.pi,2*np.pi)
plt.title("função cos(x)")
plt.show()

#plotando a função tangente:
tg=np.tan(v)
plt.scatter(v,tg)
plt.title("função tg(x)")
plt.xlabel("valor de x")
plt.ylabel("valor de tg(x)")
plt.ylim(-40,40)
plt.show()