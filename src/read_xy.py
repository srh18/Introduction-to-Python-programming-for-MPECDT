import numpy as np
import pylab as pl
infile = open('../data/xy.dat','r')
x = []
y = []
for line in infile:
    x_,y_= [float(w) for w in line.split()]
    x.append(x_)
    y.append(y_)
x=np.array(x)
y=np.array(y)

pl.plot(x,y)
pl.show()
