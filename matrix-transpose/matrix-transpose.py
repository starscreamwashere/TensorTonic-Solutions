import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Convert input to a numpy array so we can use .shape and easy indexing
    A = np.array(A)
    
    # 1. Get the number of rows (n) and columns (m)
    n, m = A.shape
    
    # 2. Create a new empty array with swapped dimensions (m, n)
    # The requirement asks for a new NumPy array
    A_T = np.zeros((m, n))
    
    # 3. Fill the new array using manual indexing
    for i in range(n):
        for j in range(m):
            # Map element at (i, j) to (j, i)
            A_T[j, i] = A[i, j]
            
    return A_T