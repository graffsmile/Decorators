import os
from test_2 import logger



@logger(path='test_3_log.log')
def summ(a,b):
    path = 'test_3_log.log'
    if os.path.exists(path):
        os.remove(path)
    return a * b

res = summ(3, 4)