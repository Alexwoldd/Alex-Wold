# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Alexandra Wold>
<MTH 420>
<5/5/23>
"""
import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    A = np.random.normal(size=(n,n))
    A_mean=A.mean(axis=1)
    return A_mean.var

def prob1():
    var_array=np.zeros((1,10))
    for i in range(10):
        var_array=var_of_means(100*(i+1))
    plt.plot(var_array)
    return plt.show()
    


# Problem 2
def prob2():
    a=np.linspace(-2*np.pi,2*np.pi,200)
    plt.plot(a,np.sin(a))
    plt.plot(a,np.cos(a))
    plt.plot(a,np.arctan(a))
    return plt.show()


# Problem 3
def prob3():
    a1=np.linspace(-2,1,45, endpoint=False)
    a2=np.linspace(1,6,75)[1:]
    plt.plot(a1, (1/(a1-1)), 'm--',linewidth=4)
    plt.plot(a2, (1/(a2-1)), 'm--',linewidth=4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    return plt.show


# Problem 4
def prob4():
    x=np.linspace(0,2*np.pi,200)
    plt.subplot(2,2,1)
    plt.plot(x,np.sin(x), 'g-')
    plt.title("a")
    plt.subplot(2,2,2)
    plt.plot(x,np.sin(2*x), 'r--')
    plt.plot("b")
    plt.subplot(2,2,3)
    plt.plot(x,2*np.sin(x), 'b-')
    plt.plot("c")
    plt.subplot(2,2,4)
    plt.plot(x, 2*np.sin(2*x), 'm:')
    plt.title("d")
    
    plt.axis([0,2*np.pi,-2,2])
    plt.suptitle("abcd")
    return plt.show()


# Problem 5
def prob5():



# Problem 6
def prob6():
    a=np.linspace(-2*np.pi,2*np.pi, 200)
    b=a.copy()
    A, B = np.meshgrid(a,b)
    C=(((np.sin(A))*(np.sin(B)))/(A*B))
    plt.subplot(1,2,1)
    plt.pcolormesh(A,B,C, cmap="magma", shading="auto")
    plt.colorbar()
    plt.subplot(1,2,2)
    plt.contour(A,B,C,20, cmap="magma")
    plt.colorbar()
    plt.axis([-2*np.pi,2*np.pi,-2*np.pi,2*np.pi])
    return plt.show()