# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 16:30:19 2018

@author: ChiJuWu
"""

import matplotlib.pyplot as plt
import numpy as np
import random 


N = 101
n_range = list(range(1,N))

p = random.randint(1,N)
p_inital=p
print('Initial position = ', p_inital)

t_loop = N*2-3
p_array = np.arange(t_loop)+1
g_array = n_range[0:N] + n_range[::-1] 

for t in range(t_loop):
    if p == 1:
        p = p + 1
        p_array[t] = p
    elif p == N-1:
        p = p - 1
        p_array[t] = p
    else:
        c=random.randint(0,1)
        if c == 1:
            p = p + c
        else:
            p = p-1
        p_array[t] = p    
    
    guess = g_array[t]
    if guess == p:
        print('Correct guess at t = ', t, 'when the princess at ', p)


print('Final position = ', p)

plt.figure(figsize=(15,15))
plt.plot(p_array,'o')
plt.plot(p_array)
plt.plot(g_array)
plt.xlabel('Try')
plt.ylabel('Position')
plt.show()





        
