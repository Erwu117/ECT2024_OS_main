#Data value displays are in retranslateUi() under "#Label Values" comment.

#Imports for GUI
from PyQt5 import QtCore, QtGui, QtWidgets
import os

#Imports for Folium Map
import folium
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

#Main Window

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

#Map Box
        
        # Create a Folium map centered at the specified coordinates
        self.m = folium.Map(location=[-8.899038249049422, 116.30608808971405], tiles="https://tile.jawg.io/jawg-matrix/{z}/{x}/{y}{r}.png?access-token=nm4WzOTm7wM4qUMqnODWo0aqcjbjCQqyskBxGFl0hU3YKZ7fRnUpwfpFo6XgK419", attr="Jawg_Matrix", zoom_start=15)

        # Convert the Folium map to an HTML string
        self.m.save('map.html')
        with open('map.html', 'r') as f:
            html = f.read()

        # Create a QWebEngineView widget and set the HTML string as its content
        self.webview = QWebEngineView()
        self.webview.setHtml(html)

        # Set the size of the QWebEngineView widget
        self.webview.setGeometry(QtCore.QRect(0, 0, 350, 350))

        self.MapBox = QtWidgets.QFrame(self.centralwidget)
        self.MapBox.setGeometry(QtCore.QRect(225, 20, 350, 350))
        self.MapBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.MapBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MapBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MapBox.setContentsMargins(0, 0, 0, 0)
        self.MapBox.setObjectName("MapBox")

        # Set the QWebEngineView widget as the central widget of the QFrame
        self.MapBox.setLayout(QVBoxLayout(self.MapBox))
        self.MapBox.layout().addWidget(self.webview)

#Time Box

        self.TimeBox = QtWidgets.QFrame(self.centralwidget)
        self.TimeBox.setGeometry(QtCore.QRect(20, 20, 200, 75))
        self.TimeBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.TimeBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TimeBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TimeBox.setObjectName("TimeBox")

        #Time Label

        self.Time = QtWidgets.QLabel(self.TimeBox)
        self.Time.setGeometry(QtCore.QRect(0, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Time.setFont(font)
        self.Time.setStyleSheet(".QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Time.setObjectName("Time")


        self.TimeLabel = QtWidgets.QLabel(self.TimeBox)
        self.TimeLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.TimeLabel.setFont(font)
        self.TimeLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.TimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeLabel.setObjectName("TimeLabel")

#Temp Box

        self.TempBox = QtWidgets.QFrame(self.centralwidget)
        self.TempBox.setGeometry(QtCore.QRect(580, 20, 200, 75))
        self.TempBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.TempBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TempBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TempBox.setObjectName("TempBox")

        #Temp Label

        self.Temp = QtWidgets.QLabel(self.TempBox)
        self.Temp.setEnabled(True)
        self.Temp.setGeometry(QtCore.QRect(0, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Temp.setFont(font)
        self.Temp.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Temp.setAlignment(QtCore.Qt.AlignCenter)
        self.Temp.setObjectName("Temp")


        self.TempLabel = QtWidgets.QLabel(self.TempBox)
        self.TempLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.TempLabel.setFont(font)
        self.TempLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.TempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TempLabel.setObjectName("TempLabel")

#Humidity Box

        self.HumidityBox = QtWidgets.QFrame(self.centralwidget)
        self.HumidityBox.setGeometry(QtCore.QRect(580, 305, 200, 75))
        self.HumidityBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.HumidityBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.HumidityBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.HumidityBox.setObjectName("HumidityBox")
        
        #Humidity Label

        self.Humidity = QtWidgets.QLabel(self.HumidityBox)
        self.Humidity.setGeometry(QtCore.QRect(0, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Humidity.setFont(font)
        self.Humidity.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.Humidity.setObjectName("Humidity")


        self.HumidityLabel = QtWidgets.QLabel(self.HumidityBox)
        self.HumidityLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.HumidityLabel.setFont(font)
        self.HumidityLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.HumidityLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.HumidityLabel.setObjectName("HumidityLabel")

#Pressure Box

        self.PressureBox = QtWidgets.QFrame(self.centralwidget)
        self.PressureBox.setGeometry(QtCore.QRect(580, 385, 200, 75))
        self.PressureBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.PressureBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PressureBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PressureBox.setObjectName("PressureBox")
        
        #Pressure Label

        self.Pressure = QtWidgets.QLabel(self.PressureBox)
        self.Pressure.setGeometry(QtCore.QRect(0, 30, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Pressure.setFont(font)
        self.Pressure.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Pressure.setAlignment(QtCore.Qt.AlignCenter)
        self.Pressure.setObjectName("Pressure")


        self.PressureLabel = QtWidgets.QLabel(self.PressureBox)
        self.PressureLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.PressureLabel.setFont(font)
        self.PressureLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.PressureLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PressureLabel.setObjectName("PressureLabel")

# Acceleration Box

        self.AccelerationBox = QtWidgets.QFrame(self.centralwidget)
        self.AccelerationBox.setGeometry(QtCore.QRect(20, 305, 200, 155))
        self.AccelerationBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.AccelerationBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AccelerationBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AccelerationBox.setObjectName("AccelerationBox")
        self.AccelerationLabel = QtWidgets.QLabel(self.AccelerationBox)
        self.AccelerationLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.AccelerationLabel.setFont(font)
        self.AccelerationLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.AccelerationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AccelerationLabel.setObjectName("AccelerationLabel")
        
        #X-Acceleration Label

        self.AccelerationX = QtWidgets.QLabel(self.AccelerationBox)
        self.AccelerationX.setGeometry(QtCore.QRect(10, 35, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.AccelerationX.setFont(font)
        self.AccelerationX.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.AccelerationX.setObjectName("AccelerationX")

        #Y-Acceleration Label

        self.AccelerationY = QtWidgets.QLabel(self.AccelerationBox)
        self.AccelerationY.setGeometry(QtCore.QRect(10, 70, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.AccelerationY.setFont(font)
        self.AccelerationY.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.AccelerationY.setObjectName("AccelerationY")
        
        #Z-Acceleration Label

        self.AccelerationZ = QtWidgets.QLabel(self.AccelerationBox)
        self.AccelerationZ.setGeometry(QtCore.QRect(10, 105, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.AccelerationZ.setFont(font)
        self.AccelerationZ.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.AccelerationZ.setObjectName("AccelerationZ")

#Speed Box

        self.SpeedBox = QtWidgets.QFrame(self.centralwidget)
        self.SpeedBox.setGeometry(QtCore.QRect(20, 100, 200, 200))
        self.SpeedBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.SpeedBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SpeedBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SpeedBox.setObjectName("SpeedBox")
        self.SpeedLabel = QtWidgets.QLabel(self.SpeedBox)
        self.SpeedLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.SpeedLabel.setFont(font)
        self.SpeedLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.SpeedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeedLabel.setObjectName("SpeedLabel")
        self.SpeedUnit = QtWidgets.QLabel(self.SpeedBox)
        self.SpeedUnit.setGeometry(QtCore.QRect(0, 140, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.SpeedUnit.setFont(font)
        self.SpeedUnit.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.SpeedUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeedUnit.setObjectName("SpeedUnit")

        #Speed Label

        self.Speed = QtWidgets.QLabel(self.SpeedBox)
        self.Speed.setGeometry(QtCore.QRect(0, 40, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(48)
        font.setBold(True)
        self.Speed.setFont(font)
        self.Speed.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Speed.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed.setObjectName("Speed")

#Battery Box

        self.BatteryBox = QtWidgets.QFrame(self.centralwidget)
        self.BatteryBox.setGeometry(QtCore.QRect(580, 100, 200, 200))
        self.BatteryBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.BatteryBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BatteryBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BatteryBox.setObjectName("BatteryBox")

        #Battery Label

        self.Battery = QtWidgets.QLabel(self.BatteryBox)
        self.Battery.setGeometry(QtCore.QRect(0, 40, 200, 100))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(48)
        font.setBold(True)
        self.Battery.setFont(font)
        self.Battery.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Battery.setAlignment(QtCore.Qt.AlignCenter)
        self.Battery.setObjectName("Battery")


        self.BatteryLabel = QtWidgets.QLabel(self.BatteryBox)
        self.BatteryLabel.setGeometry(QtCore.QRect(0, 0, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.BatteryLabel.setFont(font)
        self.BatteryLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.BatteryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BatteryLabel.setObjectName("BatteryLabel")
        self.BatteryUnit = QtWidgets.QLabel(self.BatteryBox)
        self.BatteryUnit.setGeometry(QtCore.QRect(0, 140, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.BatteryUnit.setFont(font)
        self.BatteryUnit.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.BatteryUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.BatteryUnit.setObjectName("BatteryUnit")

#Auxiliary Box

        self.AuxiliaryBox = QtWidgets.QFrame(self.centralwidget)
        self.AuxiliaryBox.setGeometry(QtCore.QRect(310, 375, 180, 85))
        self.AuxiliaryBox.setStyleSheet(".QFrame {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.AuxiliaryBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AuxiliaryBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AuxiliaryBox.setObjectName("AuxiliaryBox")
        
        #Warning Indicator

        self.AuxiliaryWarning = QtWidgets.QLabel(self.AuxiliaryBox)
        self.AuxiliaryWarning.setGeometry(QtCore.QRect(75, 15, 30, 25))
        self.AuxiliaryWarning.setText("")
        self.AuxiliaryWarning.setTextFormat(QtCore.Qt.AutoText)
        #Display Of Warning Indicator
        auxiliaryWarningSymbol = os.path.join(os.path.dirname(__file__), "IMG/Warning_OFF.png")
        self.AuxiliaryWarning.setPixmap(QtGui.QPixmap(auxiliaryWarningSymbol))
        self.AuxiliaryWarning.setScaledContents(True)
        self.AuxiliaryWarning.setObjectName("AuxiliaryWarning")
        
        #Charging Indicator

        self.AuxiliaryCharging = QtWidgets.QLabel(self.AuxiliaryBox)
        self.AuxiliaryCharging.setGeometry(QtCore.QRect(108, 15, 30, 25))
        self.AuxiliaryCharging.setText("")
        self.AuxiliaryCharging.setTextFormat(QtCore.Qt.AutoText)
        #Display Of Charging Indicator
        auxiliaryChargingSymbol = os.path.join(os.path.dirname(__file__), "IMG/Charging_OFF.png")
        self.AuxiliaryCharging.setPixmap(QtGui.QPixmap(auxiliaryChargingSymbol))
        self.AuxiliaryCharging.setScaledContents(True)
        self.AuxiliaryCharging.setObjectName("AuxiliaryCharging")
        
        #Drive Gear Indicator

        self.GearD = QtWidgets.QLabel(self.AuxiliaryBox)
        self.GearD.setGeometry(QtCore.QRect(145, 45, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        self.GearD.setFont(font)
        self.GearD.setStyleSheet("QLabel {\n"
"    color: #2E7042; /* Set the color of the QLabel text */\n"
"}")
        self.GearD.setAlignment(QtCore.Qt.AlignCenter)
        self.GearD.setObjectName("GearD")
        
        #Ready Indicator

        self.READY = QtWidgets.QLabel(self.AuxiliaryBox)
        self.READY.setGeometry(QtCore.QRect(10, 45, 75, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        self.READY.setFont(font)
        self.READY.setStyleSheet("QLabel {\n"
"    color: #2E7042; /* Set the color of the QLabel text */\n"
"}")
        self.READY.setAlignment(QtCore.Qt.AlignCenter)
        self.READY.setObjectName("READY")
        
        #Park Gear Indicator

        self.GearP = QtWidgets.QLabel(self.AuxiliaryBox)
        self.GearP.setGeometry(QtCore.QRect(85, 45, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        self.GearP.setFont(font)
        self.GearP.setStyleSheet("QLabel {\n"
"    color: #2E7042; /* Set the color of the QLabel text */\n"
"}")
        self.GearP.setAlignment(QtCore.Qt.AlignCenter)
        self.GearP.setObjectName("GearP")
        
        #Neutral Gear Indicator

        self.GearN = QtWidgets.QLabel(self.AuxiliaryBox)
        self.GearN.setGeometry(QtCore.QRect(125, 45, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        self.GearN.setFont(font)
        self.GearN.setStyleSheet("QLabel {\n"
"    color: #2E7042; /* Set the color of the QLabel text */\n"
"}")
        self.GearN.setAlignment(QtCore.Qt.AlignCenter)
        self.GearN.setObjectName("GearN")
        
        #Reverse Gear Indicator

        self.GearR = QtWidgets.QLabel(self.AuxiliaryBox)
        self.GearR.setGeometry(QtCore.QRect(105, 45, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(True)
        self.GearR.setFont(font)
        self.GearR.setStyleSheet("QLabel {\n"
"    color: #2E7042; /* Set the color of the QLabel text */\n"
"}")
        self.GearR.setAlignment(QtCore.Qt.AlignCenter)
        self.GearR.setObjectName("GearR")
        
        #Right Signal Indicator

        self.AuxiliarySignalRight = QtWidgets.QLabel(self.AuxiliaryBox)
        self.AuxiliarySignalRight.setGeometry(QtCore.QRect(140, 15, 30, 25))
        self.AuxiliarySignalRight.setText("")
        self.AuxiliarySignalRight.setTextFormat(QtCore.Qt.AutoText)
        #Display Of Right Signal Indicator
        auxiliaryRightSignal = os.path.join(os.path.dirname(__file__), "IMG/RightSignal_OFF.png")
        self.AuxiliarySignalRight.setPixmap(QtGui.QPixmap(auxiliaryRightSignal))
        self.AuxiliarySignalRight.setScaledContents(True)
        self.AuxiliarySignalRight.setObjectName("AuxiliarySignalRight")
        
        #Left Signal Indicator

        self.AuxiliarySignalLeft = QtWidgets.QLabel(self.AuxiliaryBox)
        self.AuxiliarySignalLeft.setGeometry(QtCore.QRect(10, 15, 30, 25))
        self.AuxiliarySignalLeft.setText("")
        self.AuxiliarySignalLeft.setTextFormat(QtCore.Qt.AutoText)
        #Display Of Left Signal Indicator
        auxiliaryLeftSignal = os.path.join(os.path.dirname(__file__), "IMG/LeftSignal_OFF.png")
        self.AuxiliarySignalLeft.setPixmap(QtGui.QPixmap(auxiliaryLeftSignal))
        self.AuxiliarySignalLeft.setScaledContents(True)
        self.AuxiliarySignalLeft.setObjectName("AuxiliarySignalLeft")
        
        #Lights Indicator

        self.AuxiliaryLights = QtWidgets.QLabel(self.AuxiliaryBox)
        self.AuxiliaryLights.setGeometry(QtCore.QRect(42, 15, 30, 25))
        self.AuxiliaryLights.setText("")
        self.AuxiliaryLights.setTextFormat(QtCore.Qt.AutoText)
        #Display Of Lights Indicator
        auxiliaryLightsSymbol = os.path.join(os.path.dirname(__file__), "IMG/Lights_OFF.png")
        self.AuxiliaryLights.setPixmap(QtGui.QPixmap(auxiliaryLightsSymbol))
        self.AuxiliaryLights.setScaledContents(True)
        self.AuxiliaryLights.setObjectName("AuxiliaryLights")

#Background and Logos

        self.Background = QtWidgets.QFrame(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.Background.setStyleSheet("")
        self.Background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Background.setObjectName("Background")
        self.BackgroundImage = QtWidgets.QLabel(self.Background)
        self.BackgroundImage.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.BackgroundImage.setText("")
        main_bg = os.path.join(os.path.dirname(__file__), "IMG/MainBg.png")
        self.BackgroundImage.setPixmap(QtGui.QPixmap(main_bg))
        self.BackgroundImage.setScaledContents(True)
        self.BackgroundImage.setObjectName("BackgroundImage")
        self.Shell_Logo = QtWidgets.QLabel(self.Background)
        self.Shell_Logo.setGeometry(QtCore.QRect(495, 375, 80, 80))
        self.Shell_Logo.setText("")
        self.Shell_Logo.setTextFormat(QtCore.Qt.AutoText)
        shell_logo = os.path.join(os.path.dirname(__file__), "IMG/Shell_Logo.png")
        self.Shell_Logo.setPixmap(QtGui.QPixmap(shell_logo))
        self.Shell_Logo.setScaledContents(True)
        self.Shell_Logo.setObjectName("Shell_Logo")
        self.ECT_logo = QtWidgets.QLabel(self.Background)
        self.ECT_logo.setGeometry(QtCore.QRect(225, 375, 80, 80))
        self.ECT_logo.setText("")
        ect_logo = os.path.join(os.path.dirname(__file__), "IMG/ECT_Logo.png")
        self.ECT_logo.setPixmap(QtGui.QPixmap(ect_logo))
        self.ECT_logo.setScaledContents(True)
        self.ECT_logo.setObjectName("ECT_logo")

#Raise

        self.Background.raise_()
        self.MapBox.raise_()
        self.TimeBox.raise_()
        self.TempBox.raise_()
        self.HumidityBox.raise_()
        self.PressureBox.raise_()
        self.AccelerationBox.raise_()
        self.SpeedBox.raise_()
        self.BatteryBox.raise_()
        self.AuxiliaryBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#Label Values

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Time.setText(_translate("MainWindow", "12:00:00 AM"))
        self.TimeLabel.setText(_translate("MainWindow", "Time"))
        self.Temp.setText(_translate("MainWindow", "75°C"))
        self.TempLabel.setText(_translate("MainWindow", "Temp"))
        self.Humidity.setText(_translate("MainWindow", "50%"))
        self.HumidityLabel.setText(_translate("MainWindow", "Humidity"))
        self.Pressure.setText(_translate("MainWindow", "300hPa"))
        self.PressureLabel.setText(_translate("MainWindow", "Pressure"))
        self.AccelerationLabel.setText(_translate("MainWindow", "Acceleration"))
        self.AccelerationX.setText(_translate("MainWindow", "X: 123"))
        self.AccelerationY.setText(_translate("MainWindow", "Y: 234"))
        self.AccelerationZ.setText(_translate("MainWindow", "Z: 345"))
        self.SpeedLabel.setText(_translate("MainWindow", "Speed"))
        self.SpeedUnit.setText(_translate("MainWindow", "km/h"))
        self.Speed.setText(_translate("MainWindow", "100"))
        self.Battery.setText(_translate("MainWindow", "100"))
        self.BatteryLabel.setText(_translate("MainWindow", "Battery"))
        self.BatteryUnit.setText(_translate("MainWindow", "%"))
        self.GearD.setText(_translate("MainWindow", "D"))
        self.READY.setText(_translate("MainWindow", "READY"))
        self.GearP.setText(_translate("MainWindow", "P"))
        self.GearN.setText(_translate("MainWindow", "N"))
        self.GearR.setText(_translate("MainWindow", "R"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())