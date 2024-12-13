# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 00:37:24 2024

@author: Admin
"""

import numpy as np
from random import shuffle
import networkx as nx

t=[[4,6],[4,7],[4,8],[6,8],[6,9],[4,12],[4,13],[4,14]]
shuffle(t)
T=[np.array(el) for el in t]

x=[el[0] for el in T]
y=[el[1] for el in T]

xmat = np.expand_dims(np.array(x),1)-np.expand_dims(np.array(x),0)
ymat = np.expand_dims(np.array(y),1)-np.expand_dims(np.array(y),0)
conmat = np.abs(xmat)+np.abs(ymat)
conmat[conmat!=1] = 0

G = nx.from_numpy_array(conmat)
nx.draw(G, with_labels=True)
print(len(list(nx.connected_components(G))))