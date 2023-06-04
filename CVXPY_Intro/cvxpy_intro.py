# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Alexandra Wold>
<MTH 420>
<6/3/23>
"""
import cvxpy as cp
import numpy as np

def prob1():
    x = cp.Variable(3, nonneg = True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c.T @ x)
    A = np.array([1, 2, 0])
    B = np.array([0, 1, -4])
    C = np.array([2, 10, 3])
    P = np.eye(3)
    constraints = [A@x<=3, B@x<=1, C@x>=12, P@x>=0]
    problem = cp.Problem(objective, constraints)
    minv=(problem.solve())
    print(problem.solve())
    print(x.value)
    return [x.value, minv]

   
   


# Problem 2
def l1Min(A, b):
    dx=np.shape(A)[1]
    A=A.astype('float64')
    x=cp.Variable(dx, nonneg=True)
    c=np.ones(dx)
    objective=cp.Minimize(c.T@x)
    constraints = []
    P=np.eye(dx)
    for i in range(0, np.shape(A)[0]):
        constraints.append(A[i, :]@x==b[i])
    constraints.append(P@x>=0)
    problem = cp.Problem(objective, constraints)
    minv=(problem.solve())
    print(problem.solve())
    print(x.value)
    return [x.value, minv]
    


# Problem 3
def prob3():
    pianos=13
    x = cp.Variable(6, nonneg = True)
    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(c.T @ x)
    P=np.eye(6)
    A=np.array([[1,1,1,1,1,1], [1,0,1,0,1,0], [0,1,0,1,0,1], [1,1,0,0,0,0], [0,0,1,1,0,0], [0,0,0,0,1,1]])
    constraints=[A[0, :]@x==13, A[1, :]@x==5, A[2, :]@x==8, A[3,:]@x==7, A[4,:]@x==2, A[5,:]@x==4, P@x>=0]
    
    problem=cp.Problem(objective, constraints)
    mv=prob.solve()
    return [x.value, mv]


# Problem 4
def prob4():
    A=np.array([[3,1,0.5],[1,1,1],[0.5,1,3]])
    B=np.array([3,0,1])
    x=cp.Variable(3)
    problem=cp.Problem(cp.Minimize(0.5*cp.quad_form(x, A)+B.T@x))
    solution=prob.solve()
    return [x.value, solution]


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")