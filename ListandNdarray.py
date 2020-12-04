data = [0,1,2,3,4,5,6,7,8,9]
result = data * 2
print(result, type(result))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

import numpy as np
x = np.array(data)
print(x, type(x))
