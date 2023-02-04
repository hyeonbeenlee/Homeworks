# mykey=(1,2,3,4,5)
# myval=('일','이','삼','사','오')
#
# while True:
#     a=int(input(''))
#     if a in mykey:
#         index=mykey.index(a)
#         print(myval[index])
#     else:
#         print('제대로')

import random
import math
import time
import numpy as np
import matplotlib.pyplot as plt

a=np.random.random(100)
b=np.random.random(100)
c=np.correlate(a,b)

print(c)

