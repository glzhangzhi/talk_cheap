import os
import pickle
import numpy as np
import copy

S = np.array([[-0.39,1.49,4.21], [-4.61,3.28,1.46], [1.03,-2.37,-2.27]])
y = np.array([[1],[2],[3]])

num_train = S.shape[0]
Sy = S[np.arange(num_train), np.reshape(y-1, (num_train))]
L = np.log(np.sum(np.exp(S), axis=1)) - Sy
print(L)
c = np.max(S, axis=1)
# print(c)
eSj_c = np.sum(np.exp(S-c), axis=1)
# print(eSj_c)
t = np.exp(S-c)
# print(t)
dL = np.matmul(t / eSj_c, S)
# print(dL)
dL[np.arange(num_train), np.reshape(y-1, (num_train))] -= S[np.arange(num_train), np.reshape(y-1, (num_train))]
print(dL)