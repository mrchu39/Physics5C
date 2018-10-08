import numpy as np
import matplotlib.pyplot as plt

"""
Takes x and y, both numpy arrays, and w, which is either a bool or a numpy array.
If w false, it returns an unweighted slope. If w is an array, it uses the weights
in the array to return a weighted slope.
"""
def get_m(x,y,w):
	if type(w) == bool and w == False:
		return (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
	elif type(w) == np.ndarray:
		return (sum(w)*sum(x*y*w) - sum(w*x)*sum(w*y))/(sum(w)*sum(w*x**2)-sum(w*x)**2)
	else:
		raise ValueError('Weight parameter is invalid.')

"""
Takes x and y, both numpy arrays, and w, which is either a bool or a numpy array.
If w false, it returns an unweighted intercept. If w is an array, it uses the weights
in the array to return a weighted intercept.
"""
def get_b(x,y,w):
	if type(w) == bool and w == False:
		return np.mean(y) - get_m(x,y,False)*np.mean(x)
	elif type(w) == np.ndarray:
		return (sum(w*x**2)*sum(w*y) - sum(w*x)*sum(w*x*y))/(sum(w)*sum(w*x**2)-sum(w*x)**2)
	else:
		raise ValueError('Weight parameter is invalid.')

"""
Takes x and y, both numpy arrays, and optional parameter delta_x. If delta_x is empty,
an unweighted delta_y is calculated and a constant error value is returned. If delta_x
is not constant, then a weighted delta_y is calculated and an array of values is returned.
"""
def get_delta_y(x,y,delta_x=[]):
	m, b = get_m(x,y,False), get_b(x,y,False)
	tot = 0
	delta_y = np.array([])
	if len(delta_x) != 0:
		for i in range(len(x)):
			tot += (y[i]-(m*x[i]+b))**2
		return np.sqrt(1./(len(x)-2)*tot)
	else:
		for i in range(len(x)):
			delta_y = np.append(delta_y, np.sqrt((y[i]-(m*x[i]+b))**2 + (m*delta_x[i])**2))
		return delta_y

"""
Takes x and y, both numpy arrays, and w, which is either a bool or a numpy array.
If w false, it returns unweighted slope error. If w is an array, it uses the weights
in the array to return weighted slope error.
"""
def get_delta_m(x,y,w):
	if type(w) == bool and w == False:
		return get_delta_y(x,y)/np.sqrt(len(x)*(np.mean(x**2)-np.mean(x)**2))
	elif type(w) == np.ndarray:
		return np.sqrt((sum(w))/(sum(w)*sum(w*x**2)-sum(w*x)**2))
	else:
		raise ValueError('Weight parameter is invalid.')

"""
Takes x and y, both numpy arrays, and w, which is either a bool or a numpy array.
If w false, it returns unweighted intercept error. If w is an array, it uses the weights
in the array to return weighted intercept error.
"""
def get_delta_b(x,y,w):
	if type(w) == bool and w == False:
		return np.sqrt(np.mean(x**2))*get_delta_m(x,y,False)
	elif type(w) == np.ndarray:
		return np.sqrt((sum(w*x**2))/(sum(w)*sum(w*x**2)-sum(w*x)**2))
	else:
		raise ValueError('Weight parameter is invalid.')

"""
Calculates the r-squared value. Takes x and y arrays, as well as bool value adj. If adj
is false, it returns an unadjusted r^2 value. If adj is true, it returns an adjusted one.
"""
def get_r_sq(x,y,adj):
	r = (np.mean(x*y)-np.mean(x)*np.mean(y))/np.sqrt((np.mean(x**2)-np.mean(x)**2)*(np.mean(y**2)-np.mean(y)**2))
	if adj==False:
		return r**2
	else:
		return r**2**2-(1-r**2)/len(x)

"""
Calculates the chi-square value. Takes arrays x and y, and optional parameter delta_x. Returns
reduced chi-square value.
"""
def chi_sq(x,y,delta_x=[]):
	if len(delta_x) == 0:
		y_err = get_delta_y(x,y)
		y_err = np.array(len(y)*[y_err])
		m = get_m(x,y,False)
		b = get_b(x,y,False)
	else:
		y_err = get_delta_y(x,y,delta_x)
		w = 1/y_err**2
		m = get_m(x,y,w)
		b = get_b(x,y,w)
	return sum(((y-(m*x+b))/y_err)**2)/(len(y)-2)
