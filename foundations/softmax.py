import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        maxm = np.max(z)
        exps = []
        res =[]
        for i in z:
            exps.append(np.e**(i-maxm))
        for i in exps:
            res.append(i/np.sum(exps))
        
        return np.round(res,4)


        
            
        
