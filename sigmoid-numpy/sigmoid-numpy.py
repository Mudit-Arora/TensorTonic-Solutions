import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x, dtype=float) # 1st step - convert into array 
    return 1 / (1 + np.exp(-x)) # 2nd step - create sigmoid function  