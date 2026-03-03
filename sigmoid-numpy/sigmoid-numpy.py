import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Convert input to a numpy array so it can handle lists and scalars
    x = np.array(x)
    
    # Now -x and 1/x will work correctly on all elements
    return 1 / (1 + np.exp(-x))