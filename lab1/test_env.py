import sys
import numpy as np
import matplotlib.pyplot as plt

def get_keys():
    keys = {}
    for a in sys.argv:
        temp = a.split('=', maxsplit=1)
        if (len(temp) > 1):
            keys[temp[0]] = temp[1]

    if (keys.get('--file') is not None):
        file = open(keys['--file'], 'r')
        for line in file:
            line = line.rstrip()
            temp = line.split('=', maxsplit=1)
            keys[temp[0]] = temp[1]
    return keys

def build_plot():
    x = np.array(np.arange(-20, 20, step=0.1))
    y = (x**3) + (4.81 * x**2) - (17.37 * x) + 5.38
    plt.plot(x, y)
    plt.savefig('foo.png')