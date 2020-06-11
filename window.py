from PyQt5 import QtCore, QtGui, QtWidgets
from mplwidget import MplWidget

class Window(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.button_plot = QtWidgets.QPushButton(self.centralwidget)
        self.button_plot.setGeometry(QtCore.QRect(220, 720, 100, 30))
        self.button_plot.setObjectName("button_plot")
        
        self.button_exit = QtWidgets.QPushButton(self.centralwidget)
        self.button_exit.setGeometry(QtCore.QRect(340, 720, 100, 30))
        self.button_exit.setObjectName("button_exit")
        
        self.MplWidget = MplWidget(self.centralwidget)
        self.MplWidget.setGeometry(QtCore.QRect(40, 30, 560, 220))
        self.MplWidget.setObjectName("MplWidget")
        
        self.MplWidget2 = MplWidget(self.centralwidget)
        self.MplWidget2.setGeometry(QtCore.QRect(40, 250, 270, 220))
        self.MplWidget2.setObjectName("MplWidget2")
        
        self.MplWidget3 = MplWidget(self.centralwidget)
        self.MplWidget3.setGeometry(QtCore.QRect(330, 250, 270, 220))
        self.MplWidget3.setObjectName("MplWidget3")
        
        self.label_an = QtWidgets.QLabel(self.centralwidget)
        self.label_an.setGeometry(QtCore.QRect(125, 480, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_an.setFont(font)
        self.label_an.setObjectName("label_an")
        
        self.label_bn = QtWidgets.QLabel(self.centralwidget)
        self.label_bn.setGeometry(QtCore.QRect(485, 480, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_bn.setFont(font)
        self.label_bn.setObjectName("label_bn")
        
        self.text_an = QtWidgets.QTextEdit(self.centralwidget)
        self.text_an.setGeometry(QtCore.QRect(40, 520, 200, 165))
        self.text_an.setObjectName("text_an")
        
        self.text_bn = QtWidgets.QTextEdit(self.centralwidget)
        self.text_bn.setGeometry(QtCore.QRect(400, 520, 200, 165))
        self.text_bn.setObjectName("text_bn")
        
        self.label_a0 = QtWidgets.QLabel(self.centralwidget)
        self.label_a0.setGeometry(QtCore.QRect(250, 485, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_a0.setFont(font)
        self.label_a0.setObjectName("label_a0") 
        
        self.label_mod = QtWidgets.QLabel(self.centralwidget)
        self.label_mod.setGeometry(QtCore.QRect(250, 520, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mod.setFont(font)
        self.label_mod.setObjectName("label_mod")
        
        self.label_xstart = QtWidgets.QLabel(self.centralwidget)
        self.label_xstart.setGeometry(QtCore.QRect(250, 555, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_xstart.setFont(font)
        self.label_xstart.setObjectName("label_xstart")
        
        self.label_xend = QtWidgets.QLabel(self.centralwidget)
        self.label_xend.setGeometry(QtCore.QRect(250, 590, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_xend.setFont(font)
        self.label_xend.setObjectName("label_xend")
        
        self.label_period = QtWidgets.QLabel(self.centralwidget)
        self.label_period.setGeometry(QtCore.QRect(250, 625, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_period.setFont(font)
        self.label_period.setObjectName("label_period")
        
        self.label_n = QtWidgets.QLabel(self.centralwidget)
        self.label_n.setGeometry(QtCore.QRect(250, 660, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_n.setFont(font)
        self.label_n.setObjectName("label_n")
        
        self.edit_a0 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_a0.setGeometry(QtCore.QRect(320, 485, 70, 25))
        self.edit_a0.setObjectName("edit_a0")
        
        self.edit_mod = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_mod.setGeometry(QtCore.QRect(320, 520, 70, 25))
        self.edit_mod.setObjectName("edit_mod")
        
        self.edit_xend = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_xend.setGeometry(QtCore.QRect(320, 590, 70, 25))
        self.edit_xend.setObjectName("edit_xend")
        
        self.edit_xstart = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_xstart.setGeometry(QtCore.QRect(320, 555, 70, 25))
        self.edit_xstart.setObjectName("edit_xstart")
        
        self.edit_n = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_n.setGeometry(QtCore.QRect(320, 660, 70, 25))
        self.edit_n.setObjectName("edit_n")
        
        self.edit_period = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_period.setGeometry(QtCore.QRect(320, 625, 70, 25))
        self.edit_period.setObjectName("edit_period")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.setFixedSize(self.size())
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_plot.setText(_translate("MainWindow", "Plot"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.label_a0.setText(_translate("MainWindow", "a0"))
        self.label_an.setText(_translate("MainWindow", "an"))
        self.label_bn.setText(_translate("MainWindow", "bn"))
        self.label_mod.setText(_translate("MainWindow", "mod"))
        self.label_xstart.setText(_translate("MainWindow", "x start"))
        self.label_xend.setText(_translate("MainWindow", "x end"))
        self.label_period.setText(_translate("MainWindow", "period"))
        self.label_n.setText(_translate("MainWindow", "n"))
        
    def close_win(self):
        QtCore.QCoreApplication.instance().quit()

