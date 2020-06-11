from math import *
import numpy as np
import window
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class FourierSeries(window.Window, QtWidgets.QMainWindow):
    def __init__(self, safe_dict):
        super(FourierSeries, self).__init__()
        self.setupUi(self)
        self.safe_dict = safe_dict
        self.button_plot.clicked.connect(self.update_graph)
        self.show()
        self.button_exit.clicked.connect(self.close_win)
            
    def function_evaluate(self, an, bn, n): 
        self.safe_dict['n'] = n
        y1 = eval(an, {"__builtins__":None}, self.safe_dict)
        y2 = eval(bn, {"__builtins__":None}, self.safe_dict)
        return y1, y2
      
    def get_input(self):
        self.limit_n = int(self.edit_n.text())
        self.time_interval = np.arange(float(self.edit_xstart.text()), float(self.edit_xend.text()), 0.01)
        data = np.zeros((2, self.time_interval.shape[0]))
        data[1,:] = self.time_interval
        self.data = data   
        self.an_expression = self.text_an.toPlainText().splitlines()
        self.bn_expression = self.text_bn.toPlainText().splitlines()
        self.a0 = float(self.edit_a0.text())
        self.mod_num = int(self.edit_mod.text())
        self.period = float(self.edit_period.text())
        self.magnitude = np.zeros((2, self.limit_n))
        self.magnitude[1,:] = np.arange(1, self.limit_n+1, 1)
        self.theta = np.zeros((2, self.limit_n))
        self.theta[1,:] = np.arange(1, self.limit_n+1, 1)
    
    def evaluate_for_one(self, an, bn, n, t):
        an, bn = self.function_evaluate(an, bn, n)
        first = an * np.array(list(map(lambda x: cos(n * (2*pi/self.period) * x), t)))  
        second = bn * np.array(list(map(lambda x: sin(n * (2*pi/self.period) * x), t)))
        
        self.magnitude[0,n-1] = sqrt(an**2 + bn**2)
        self.theta[0,n-1] = np.arctan2(-1*bn, an) * 180/pi
        
        return first + second

    def find_value(self):
        self.data[0,:] = self.data[0,:] + self.a0 
        for n in range (1, self.limit_n + 1):
            element = n % self.mod_num
            value = self.evaluate_for_one(self.an_expression[element], self.bn_expression[element], n, self.time_interval)
            self.data[0] = self.data[0] + value
        return self.data

    def update_graph(self):
        self.get_input()
        self.data = self.find_value()
        self.plot_graph(self.data, "Fourier Series Visualization", self.MplWidget)
        self.plot_stem(self.magnitude, "Magnitude", self.MplWidget2)
        self.plot_stem(self.theta,  "Phase", self.MplWidget3)
        
    def plot_graph(self, data, name, MplWidget):
        MplWidget.canvas.axes.clear()
        MplWidget.canvas.axes.plot(data[1,:], data[0,:])
        MplWidget.canvas.axes.set_title(name)
        MplWidget.canvas.draw()      
        
    def plot_stem(self, data, name, MplWidget):
        MplWidget.canvas.axes.clear()
        MplWidget.canvas.axes.stem(data[1,:], data[0,:], use_line_collection=True)
        MplWidget.canvas.axes.set_title(name)
        MplWidget.canvas.draw()      
        
safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 
             'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 
             'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10', 
             'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 
             'tan', 'tanh'] 
      
safe_dict = dict()
for k in safe_list:
    safe_dict[k] = locals()[k]
    
app = QtWidgets.QApplication(sys.argv)   
myseries = FourierSeries(safe_dict)
app.exec_()
