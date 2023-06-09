import numpy as np
from scipy import linalg as la

def index(A, tol=1e-5):
    if not np.isclose(la.det(A),0):
        return 0
    
    n = len(A)
    k=1
    Ak=A.copy()
    
    while k<=n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1
        
    return k

def is_drazin(A, Ad, k):
    X=A@Ad
    Y=Ad@A
    
    if np.allclose(X,Y,rtol=1e-4):
        C=1
    else:
        C=0
    
    AK=np.linalg.matrix_power(A,k)
    AK1=np.linalg.matrix_power(A,k+1)
    N=AK1@Ad
    
    if np.allclose(AK,N,rtol=1e-4):
        C1=1
    else:
        C1=0
        
    Z=(Ad@A)@Ad
    if np.allclose(Ad,Z,rtol=1e-4):
        C2=1
    else:
        C2=0
    
    if (C+C1+C2)==3:
        return True
    else:
        return False
    
def drazin_inverse(A, tol=1e-4):
    n=A.shape[0]
    T,Z=la.schur(A)
    X = lambda x: abs(x) > tol
    T1,Z1,k1 = la.schur(A, sort=X)
    
    X1=Z1[:,:k1]
    
    Y = lambda x: abs(x) <= tol
    T2,Z2,k2 = la.schur(A, sort=Y)
    
    Y1=Z2[:,:k2]
    
    C=np.concatenate((X1,Y1),axis=1)
    I=la.inv(C)
    V=(I@A)@C
    U=np.zeros_like(A,dtype=float)
    
    if k1!=0:
        B=V[:k1,:k2]
    
    BI=la.inv(B)
    U[:k1,:k1]=BI
    Ad=(C@U)@I
    
    return Ad
    