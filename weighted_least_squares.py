import numpy as np
import matplotlib.pyplot as plt


def get_m(x,y,w):
	if type(w) == bool and w == False:
		return (np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
	elif type(w) == np.ndarray:
		return (sum(w)*sum(x*y*w) - sum(w*x)*sum(w*y))/(sum(w)*sum(w*x**2)-sum(w*x)**2)
	else:
		raise ValueError('Weight parameter is invalid.')

def get_b(x,y,w):
	if type(w) == bool and w == False:
		return np.mean(y) - get_m(x,y,False)*np.mean(x)
	elif type(w) == np.ndarray:
		return (sum(w*x**2)*sum(w*y) - sum(w*x)*sum(w*x*y))/(sum(w)*sum(w*x**2)-sum(w*x)**2)
	else:
		raise ValueError('Weight parameter is invalid.')

def get_delta_y(x,y,w,delta_x=[]):
	m, b = get_m(x,y,False), get_b(x,y,False)
	tot = 0
	delta_y = np.array([])
	if w == False:
		for i in range(len(x)):
			tot += (y[i]-(m*x[i]+b))**2
		return np.sqrt(1./(len(x)-2)*tot)
	else:
		for i in range(len(x)):
			delta_y = np.append(delta_y, np.sqrt((y[i]-(m*x[i]+b))**2 + (m*delta_x[i])**2))
		return delta_y

def get_delta_m(x,y,w):
	if type(w) == bool and w == False:
		return get_delta_y(x,y,False)/np.sqrt(len(x)*(np.mean(x**2)-np.mean(x)**2))
	elif type(w) == np.ndarray:
		return np.sqrt((sum(w))/(sum(w)*sum(w*x**2)-sum(w*x)**2))
	else:
		raise ValueError('Weight parameter is invalid.')

def get_delta_b(x,y,w):
	if type(w) == bool and w == False:
		return np.sqrt(np.mean(x**2))*get_delta_m(x,y,False)
	elif type(w) == np.ndarray:
		return np.sqrt((sum(w*x**2))/(sum(w)*sum(w*x**2)-sum(w*x)**2))
	else:
		raise ValueError('Weight parameter is invalid.')

def get_r_sq(x,y,adj):
	r = (np.mean(x*y)-np.mean(x)*np.mean(y))/np.sqrt((np.mean(x**2)-np.mean(x)**2)*(np.mean(y**2)-np.mean(y)**2))
	if adj==False:
		return r**2
	else:
		return r**2**2-(1-r**2)/len(x)


def chi_sq(x,y,w,delta_x=[]):
	if type(w) == bool and w == False:
		y_err = get_delta_y(x,y,False)
		y_err = np.array(len(y)*[y_err])
		m = get_m(x,y,w)
		b = get_b(x,y,w)
	elif type(w) == bool and w == True:
		y_err = get_delta_y(x,y,w,delta_x)
		w = 1/y_err**2
		m = get_m(x,y,w)
		b = get_b(x,y,w)
	return sum(((y-(m*x+b))/y_err)**2)/(len(y)-2)
