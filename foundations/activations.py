import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        sig = 1 / (1+np.e**(-z))
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        return np.round(sig,5)

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        return np.maximum(0,z)
        a = []
        
        for i in range(len(z)):
            a.append(max(0.0,float(z[i])))

        
        return a
