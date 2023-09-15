from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import numpy as np
n = 0
e = 0
tempNumpyArray=np.load("name.npy")
namelist = tempNumpyArray.tolist()
tempNumpyArray=np.load("data.npy")
datalist = tempNumpyArray.tolist()
tempNumpyArray=np.load("qanak.npy")
qanaklist = tempNumpyArray.tolist()
tempNumpyArray=np.load("allqanak.npy")
allqanaklist = tempNumpyArray.tolist()
tempNumpyArray=np.load("allname.npy")
allnamelist = tempNumpyArray.tolist()
print(namelist)
print(datalist)
print(qanaklist)
print(allnamelist)
print(allqanaklist)
rx = 0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(430, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 220, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 341, 60))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 80, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(410, 150, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 290, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 290, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 360, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(250, 360, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.clicked.connect(self.on)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_5.clicked.connect(self.delate)
        self.pushButton_6.clicked.connect(self.alllist)
        self.pushButton_7.clicked.connect(self.minus)
        self.pushButton_4.hide()
        self.pushButton.hide()  
        self.lineEdit.hide()  
        self.label_2.hide()
        self.label_3.hide()
        self.pushButton_7.hide()

        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        for port in ports:
            portlist.append(port.portName())
        print(portlist)
        self.comboBox.addItems(portlist)
        
 
    def minus(self):
        global rx
        e = datalist.index(rx)
        qanaklist[e] = qanaklist[e]-1
        self.label_3.setText(str(qanaklist[e]))
        allqanaklist[e] = allqanaklist[e]-1
    def alllist(self):
        self.pushButton_7.hide()
        if allnamelist.count(self.lineEdit_3.text()) > 0:
            e = allnamelist.index(self.lineEdit_3.text())
            self.label_2.setText(allnamelist[e])
            self.label_3.setText(str(allqanaklist[e]))
            self.label_2.show()
            self.label_3.show()
            self.label.hide()
        self.lineEdit_3.setText("")
        self.pushButton.hide()
        self.lineEdit.hide()
    def delate(self):
        self.pushButton_7.hide()
        if namelist.count(self.lineEdit_2.text()) > 0:
            e = namelist.index(self.lineEdit_2.text())
            print(e)
            namelist.remove(self.lineEdit_2.text())  
            datalist.pop(e)
            qanaklist.pop(e)
            np.save("name.npy",namelist)     
            np.save("data.npy",datalist)
            np.save("qanak.npy",qanaklist) 
            self.label_2.hide()
            self.label_3.hide()
            self.label.setText("ջնջված է")
        self.lineEdit_2.setText("")
        self.pushButton.hide()
        self.lineEdit.hide()
    def av(self):
        global rx
        global e
        if e == 0:
            qanaklist[datalist.index(rx)]=1
            allqanaklist[datalist.index(rx)] = allqanaklist[datalist.index(rx)]+1
            self.pushButton_4.hide()
            self.label_3.setText(str(qanaklist[datalist.index(rx)]))
            e = 1
    def comm(self):
        global e
        global rx
        global n
        n = 0
        rx = str(self.serial.readLine())
        
        
                
        def data():
            self.pushButton_7.hide()
            if datalist.count(rx) == 0:
                if allnamelist.count(self.lineEdit.text()) != 0:
                    e = allnamelist.index(self.lineEdit.text())
                    allqanaklist.append(allqanaklist[e]+1)
                    allnamelist.pop(e)
                    allqanaklist.pop(e)
                    
                else:
                    
                    allqanaklist.append(1)
                qanaklist.append(0)
                namelist.append(self.lineEdit.text())  
                allnamelist.append(self.lineEdit.text())  
                datalist.append(rx)  
                qanaklist[datalist.index(rx)] = int(qanaklist[datalist.index(rx)])+1
                np.save("name.npy",namelist)     
                np.save("data.npy",datalist)
                np.save("qanak.npy",qanaklist)
                np.save("allname.npy",allnamelist)
                np.save("allqanak.npy",allqanaklist)        
                self.pushButton.hide()
                self.lineEdit.hide()  
                self.label_2.setText(namelist[datalist.index(rx)])
                self.label_3.setText(str(qanaklist[datalist.index(rx)]))
                self.label_2.show()
                self.label_3.show() 
                self.label.setText("գրանցված է")
                self.lineEdit.setText("")
        
            
            
            
        if datalist.count(rx) == 0 and rx != b'\r\n':    
            self.pushButton_7.hide()
            self.pushButton.show()
            self.label.setText("սխալ քարտ")
            self.pushButton.clicked.connect(data)
            self.lineEdit.show()
            self.label_2.hide()
            self.label_3 .hide()
            self.pushButton_4.hide()
        elif datalist.count(rx) != 0 and rx != b'\r\n':
            # lastrx = rx
            self.pushButton.show()  
            self.pushButton_7.show()
            self.label.setText("ճիշտ քարտ")
            self.pushButton.hide()  
            self.lineEdit.hide() 
            self.pushButton_4.hide()
            self.label_2.show()
            self.label_3.show() 
            self.label_2.setText(namelist[datalist.index(rx)])
            if qanaklist[datalist.index(rx)] < 11:
                self.pushButton_4.hide()
                qanaklist[datalist.index(rx)] = int(qanaklist[datalist.index(rx)])+1
                e = allnamelist.index(namelist[datalist.index(rx)])
                allqanaklist[e] = int(allqanaklist[e])+1
            elif qanaklist[datalist.index(rx)] == 11:
                qanaklist[datalist.index(rx)] = int(qanaklist[datalist.index(rx)])+1
                e = allnamelist.index(namelist[datalist.index(rx)])
                allqanaklist[e] = int(allqanaklist[e])+1
                self.pushButton_4.show()
                self.pushButton_4.clicked.connect(self.av)
                
            else:
                self.pushButton_4.hide()
                e = 0
                self.pushButton_4.show()
                self.pushButton_4.clicked.connect(self.av)
                
            self.label_3.setText(str(qanaklist[datalist.index(rx)]))
            print(rx)
            #print(lastrx)
            np.save("qanak.npy",qanaklist)    
            np.save("allqanak.npy",allqanaklist)    
        print(namelist)
        print(datalist)
        print(qanaklist)
        print(allnamelist)
        print(allqanaklist)
        
        
        

    def on(self):
        self.serial.setPortName(self.comboBox.currentText())
        self.serial.open(QIODevice.ReadWrite)
        self.serial.readyRead.connect(self.comm)
    def close(self):
        self.serial = QSerialPort()
        self.serial.setBaudRate(9600)
        portlist = []
        ports = QSerialPortInfo().availablePorts()
        self.comboBox.clear()
        for port in ports:
            portlist.append(port.portName())
        self.comboBox.addItems(portlist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "CONNECT"))
        self.pushButton_2.setText(_translate("MainWindow", "REFRESH"))
        self.label.setText(_translate("MainWindow", "քարտ հայտնաբերվաէծ չէ"))
        self.pushButton.setText(_translate("MainWindow", "գրանցել"))
        self.label_2.setText(_translate("MainWindow", "անուն"))
        self.label_3.setText(_translate("MainWindow", "0"))
        self.pushButton_4.setText(_translate("MainWindow", "ավելացնել"))
        self.pushButton_7.setText(_translate("MainWindow", "պակասեցնել"))
        self.pushButton_5.setText(_translate("MainWindow", "ջնջել"))
        self.pushButton_6.setText(_translate("MainWindow", "փնտրել"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
