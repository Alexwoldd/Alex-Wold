# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Alexandra Wold>
<MTH 420>
<5/12/23>
"""

# (Optional) Import functions from your QR Decomposition lab.
# import sys
# sys.path.insert(1, "../QR_Decomposition")
# from qr_decomposition import qr_gram_schmidt, qr_householder, hessenberg

import numpy as np
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    q,r=np.linalg.qr(A, mode="reduced")
    qb=(q.T).dot(b)
    c=np.linalg.solve(r, qb)
    return c

# Problem 2
def line_fit():
    house=np.load("housing.npy")
    
    A=np.column_stack((house[:,0], np.ones(house[:,0].size)))
    b=house[:,1]
    x=least_squares(A,b)
    
    plt.plot(house[:,0], b, 'o')
    plt.plot(house[:,0], x[0]*house[:,0]+x[1], 'g-') 
    return 
    


# Problem 3
def polynomial_fit():
    house=np.load("housing.npy")
    
    A=np.vander(house[:,0], 3)
    b=house[:,1]
    x=least_squares(A,b)
    
    A2=np.vander(house[:,0], 4)
    x2=least_squares(A2,b)
    f2=np.zeros_like(house[:,0])
    for i in range(4):
        f2=f2+x2[i]*house[:,0]**(3-i)
    plt.subplot(411)
    plt.plot(house[:,0], f2, 'g-')
    plt.plot(house[:,0], b, 'o')
    
    A3=np.vander(house[:,0], 7)
    x3=least_squares(A3,b)
    f3=np.zeros_like(house[:,0])
    for i in range(7):
        f3=f3+x3[i]*house[:,0]**(6-i)
    plt.subplot(412)
    plt.plot(house[:,0], f3, 'g-')
    plt.plot(house[:,0], b, 'o')
    
    
    
    A4=np.vander(house[:,0], 10)
    x4=least_squares(A4,b)
    f4=np.zeros_like(house[:,0])
    for i in range(10):
        f4=f4+x4[i]*house[:,0]**(9-i)
    plt.subplot(413)
    plt.plot(house[:,0], f4, 'g-')
    plt.plot(house[:,0], b, 'o')
    
    A5=np.vander(house[:,0], 13)
    x5=least_squares(A5,b)
    f5=np.zeros_like(house[:,0])
    for i in range(13):
        f5=f5+x5[i]*house[:,0]**(12-i)
    plt.subplot(414)
    plt.plot(house[:,0], f5, 'g-')
    plt.plot(house[:,0], b, 'o')
    
    

    return 
    


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
