from math import *
import numpy as np
import matplotlib.pyplot as plt

class FourierSeries():
    def __init__(self, safe_dict, time_interval, limit_n=50):
        self.limit_n = limit_n
        self.an_cos = list
        self.bn_sin = list
        self.time_interval = np.arange(time_interval[0], time_interval[1], 0.05)
        data = np.zeros((2, self.time_interval.shape[0]))
        data[1,:] = self.time_interval
        self.data = data
        self.safe_dict = safe_dict
        
    def function_evaluate(self, an, bn, n): 
        self.safe_dict['n'] = n
        y1 = eval(an, {"__builtins__":None}, self.safe_dict)
        y2 = eval(bn, {"__builtins__":None}, self.safe_dict)
        return y1, y2
      
    def get_input(self):
        self.period = float(input("Enter the period: "))
        a0 = float(input("Enter the a0 (in terms of n):"))
        an = input("Enter the an (in terms of n):")
        bn = input("Enter the bn (in terms of n):")
        return a0, an, bn
    
    def evaluate_for_one(self, an, bn, n, t):
        an, bn = self.function_evaluate(an, bn, n)
        first = an * np.array(list(map(lambda x: cos(n * (2*pi/self.period) * x), t)))  
        second = bn * np.array(list(map(lambda x: sin(n * (2*pi/self.period) * x), t)))
        return first + second
    
    def find(self):
        a0, an, bn = self.get_input()
        for n in range(1,self.limit_n+1):
            self.data[0] = self.data[0] + self.evaluate_for_one(an, bn, n, self.time_interval)
        self.data[0,:] = self.data[0,:] + float(a0)
        return self.data
    
    def plot_data(self):
        plt.plot(self.data[1,:], self.data[0,:])
    
# list of safe methods 
safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 
             'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 
             'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 
             'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 
             'tan', 'tanh'] 
  
# creating a dictionary of safe methods 
#safe_dict = dict([(k, locals()[str(k)]) for k in safe_list]) 
safe_dict = dict()
for k in safe_list:
    safe_dict[k] = locals()[k]
    
myseries = FourierSeries(safe_dict,  [-10,10], 100)
data = myseries.find()
myseries.plot_data()
