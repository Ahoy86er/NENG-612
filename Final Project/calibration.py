import numpy as np
import matplotlib.pyplot as plt
#from scipy.optimize import curve_fit
from numpy import log as ln
from numpy import exp as e

x = np.array([59.5409, 121.7, 244.7, 302.85, 344.38, 356.01, 661.657, 778.9, 964.06, 1085.837, 1112.08, 1173.23, 1332.49, 1408.01])
y = np.array([1.13E-02, 1.05E-02, 7.31E-03, 5.97E-03, 5.44E-03, 5.27E-03, 3.22E-03, 2.75E-04, 2.34E-03, 2.52E-03, 2.07E-03, 2.03E-03, 2.02E-03, 1.79E-03])

#plt.plot(x, y, 'ro', label="original data")

def fit_func(x, a, b):
    return e(b*(ln(x/a)))

z = np.polyfit(x, y, 3)
f = np.poly1d(z)

x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'ko', label='Experimental Data')
plt.plot(x_new, y_new, label='Fitted Caibration Equation')
plt.legend(loc='upper right')
plt.xlabel('Energy [keV]')
plt.ylabel('Efficiency')
plt.title('Efficiency Calibration')
plt.show()