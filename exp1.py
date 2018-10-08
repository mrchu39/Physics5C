import numpy as np
import matplotlib.pyplot as plt
from weighted_least_squares import *

# Given data (using the 0 degree optical axis).
theta = np.array(range(7,102,5))*np.pi/180
delta_theta = np.array(len(theta)*[0.5])
I = np.array([374, 361, 350, 331, 308, 276, 242, 203, 189, 142, 112, 89, 62, 39, 22, 11, 3, 4, 2])
delta_I = np.array(len(I)*[0.5])
x = np.cos(theta)**2
delta_x = np.abs(2*np.cos(theta)*np.sin(theta)*delta_I)

# Unweighted stats.
m_unw = get_m(x,I,False)
delta_m_unw = get_delta_m(x,I,False)
b_unw = get_b(x,I,False)
delta_b_unw = get_delta_b(x,I,False)
delta_I_unw = get_delta_y(x,I)
chi_sq_unw = chi_sq(x,I)

# Weighted stats.
delta_I_w = get_delta_y(x,I,delta_x)
w = 1/delta_I_w
m_w = get_m(x,I,w)
delta_m_w = get_delta_m(x,I,w)
b_w = get_b(x,I,w)
delta_b_w = get_delta_b(x,I,w)
chi_sq_w = chi_sq(x,I,delta_x)

print "UNWEIGHTED LEAST SQUARES REGRESSION"
print "I_0 =", m_unw, "+-", delta_m_unw
print "I_bg =", b_unw, " +-", delta_b_unw
print "delta I =", delta_I_unw
print "chi squared =", chi_sq_unw
print "-------------------------- \n"

print "WEIGHTED LEAST SQUARES REGRESSION"
print "I_0 =", m_w, " +-", delta_m_w
print "I_bg =", b_w, " +-", delta_b_w
print "delta I =", delta_I_w
print "chi squared =", chi_sq_w
print "-------------------------- \n"

plt.figure(1)

# Plot unweighted data points with error bars and its respective regression line.
plt.errorbar(x, I, yerr=delta_I_unw, fmt='o')

z = np.polyfit(x, I, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--")
plt.title(r'$\mathrm{Light \ Intensity \ vs. \ }\mathrm{cos}^2(\theta_{rel}) \ \mathrm{(Unweighted)}$')
plt.xlabel(r'$\mathrm{cos}^2 (\theta_{rel})$')
plt.ylabel('Light Intensity (lux)')

plt.show()

plt.figure(2)

# Plot weighted data points with error bars and its respective regression line.
plt.errorbar(x, I, yerr=delta_I_w, fmt='o')

line = np.array([m_w*x[0],m_w*x[len(x)-1]])
plt.plot(np.array([x[0],x[len(x)-1]]),line,"r--")
plt.title(r'$\mathrm{Light \ Intensity \ vs. \ }\mathrm{cos}^2(\theta_{rel}) \ \mathrm{(Weighted)}$')
plt.xlabel(r'$\mathrm{cos}^2 (\theta_{rel})$')
plt.ylabel('Light Intensity (lux)')

plt.show()

plt.figure(3)

# Both plots.
plt.plot(x, I, 'o')
plt.plot(x,p(x),"r--",label='Unweighted')
plt.plot(np.array([x[0],x[len(x)-1]]),line,"b--",label='Weighted')
plt.title(r'$\mathrm{Light \ Intensity \ vs. \ }\mathrm{cos}^2(\theta_{rel}) \ \mathrm{(Both)}$')
plt.xlabel(r'$\mathrm{cos}^2 (\theta_{rel})$')
plt.ylabel('Light Intensity (lux)')
plt.legend(loc='upper left')

plt.show()
