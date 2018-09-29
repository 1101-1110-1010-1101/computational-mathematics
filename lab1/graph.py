import numpy as np
import gnuplotlib as gp

x = np.array(np.arange(-20, 20, step=0.1))
y = (x**3) + (4.81 * x**2) - (17.37 * x) + 5.38
gp.plot(x, y, _with = 'lines')