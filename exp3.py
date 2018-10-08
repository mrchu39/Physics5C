import numpy as np
import matplotlib.pyplot as plt
from weighted_least_squares import *

ang = 90-np.array([10, 45, 67, 56])
height = np.array([4.5, 3.5, 2.5, 2.5])
height /= 10

m = get_m(height, ang, False)
b = get_b(height, ang, False)
delta_y = np.array(len(ang)*[get_delta_y(height, ang)])
delta_m = get_delta_m(height, ang, 1/delta_y)
delta_b = get_delta_b(height, ang, 1/delta_y)

plt.errorbar(height, ang, yerr=delta_y, fmt='o')
z = np.polyfit(height, ang, 1)
p = np.poly1d(z)
plt.plot(height,p(height),"r--")
plt.title(r'$\mathrm{Optical \ Axis \ Change \ vs. \ Height \ of \ Fluid}$')
plt.xlabel('Height of Fluid (cm)')
plt.ylabel('Optical Axis Change (degrees)')
plt.show()

print "m =", m, "+-", delta_m
print "b =", b, "+-", delta_b
print "r^2 =", get_r_sq(height,ang,True)
