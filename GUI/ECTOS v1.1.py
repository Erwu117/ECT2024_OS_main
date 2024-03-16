from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.LOGO = QtWidgets.QLabel(self.centralwidget)
        self.LOGO.setGeometry(QtCore.QRect(225, 375, 80, 80))
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap("EcoCar-Logo.png"))
        self.LOGO.setScaledContents(True)
        self.LOGO.setObjectName("LOGO")
        self.Background = QtWidgets.QLabel(self.centralwidget)
        self.Background.setGeometry(QtCore.QRect(-10, -10, 831, 491))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap("MainBg.png"))
        self.Background.setScaledContents(True)
        self.Background.setObjectName("Background")
        self.TimeBox = QtWidgets.QLineEdit(self.centralwidget)
        self.TimeBox.setGeometry(QtCore.QRect(20, 20, 200, 75))
        self.TimeBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"")
        self.TimeBox.setPlaceholderText("")
        self.TimeBox.setObjectName("TimeBox")
        self.SpeedBox = QtWidgets.QLineEdit(self.centralwidget)
        self.SpeedBox.setGeometry(QtCore.QRect(20, 100, 200, 200))
        self.SpeedBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.SpeedBox.setObjectName("SpeedBox")
        self.AccelCoords = QtWidgets.QLineEdit(self.centralwidget)
        self.AccelCoords.setGeometry(QtCore.QRect(20, 305, 200, 155))
        self.AccelCoords.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.AccelCoords.setObjectName("AccelCoords")
        self.MapBox = QtWidgets.QLineEdit(self.centralwidget)
        self.MapBox.setGeometry(QtCore.QRect(225, 20, 350, 350))
        self.MapBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.MapBox.setObjectName("MapBox")
        self.TempBox = QtWidgets.QLineEdit(self.centralwidget)
        self.TempBox.setGeometry(QtCore.QRect(580, 20, 200, 75))
        self.TempBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.TempBox.setObjectName("TempBox")
        self.BatteryBox = QtWidgets.QLineEdit(self.centralwidget)
        self.BatteryBox.setGeometry(QtCore.QRect(580, 100, 200, 200))
        self.BatteryBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.BatteryBox.setObjectName("BatteryBox")
        self.HumidityBox = QtWidgets.QLineEdit(self.centralwidget)
        self.HumidityBox.setGeometry(QtCore.QRect(580, 305, 200, 75))
        self.HumidityBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.HumidityBox.setObjectName("HumidityBox")
        self.PressureBox = QtWidgets.QLineEdit(self.centralwidget)
        self.PressureBox.setGeometry(QtCore.QRect(580, 385, 200, 75))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.PressureBox.setFont(font)
        self.PressureBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.PressureBox.setObjectName("PressureBox")
        self.AuxiliaryBox = QtWidgets.QLineEdit(self.centralwidget)
        self.AuxiliaryBox.setGeometry(QtCore.QRect(310, 375, 180, 85))
        self.AuxiliaryBox.setStyleSheet("QLineEdit {\n"
"    background-color: transparent; /* Make the background transparent */\n"
"    border: 2px solid #b4ffc1; /* Set the border thickness and color */\n"
"    border-radius: 10px; /* Set the border radius to make rounded edges */\n"
"    padding: 5px;\n"
"}")
        self.AuxiliaryBox.setObjectName("AuxiliaryBox")
        self.Shell_Logo = QtWidgets.QLabel(self.centralwidget)
        self.Shell_Logo.setGeometry(QtCore.QRect(495, 375, 80, 80))
        self.Shell_Logo.setText("")
        self.Shell_Logo.setTextFormat(QtCore.Qt.AutoText)
        self.Shell_Logo.setPixmap(QtGui.QPixmap("Shell-Logo.png"))
        self.Shell_Logo.setScaledContents(True)
        self.Shell_Logo.setObjectName("Shell_Logo")
        self.TimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TimeLabel.setGeometry(QtCore.QRect(20, 20, 200, 30))
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
        self.SpeedLabel = QtWidgets.QLabel(self.centralwidget)
        self.SpeedLabel.setGeometry(QtCore.QRect(20, 100, 200, 30))
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
        self.BatteryLabel = QtWidgets.QLabel(self.centralwidget)
        self.BatteryLabel.setGeometry(QtCore.QRect(580, 100, 200, 30))
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
        self.TempLabel = QtWidgets.QLabel(self.centralwidget)
        self.TempLabel.setGeometry(QtCore.QRect(580, 20, 200, 30))
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
        self.HumidityLabel = QtWidgets.QLabel(self.centralwidget)
        self.HumidityLabel.setGeometry(QtCore.QRect(580, 305, 200, 30))
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
        self.CoordinatesLabel = QtWidgets.QLabel(self.centralwidget)
        self.CoordinatesLabel.setGeometry(QtCore.QRect(20, 305, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        font.setBold(False)
        self.CoordinatesLabel.setFont(font)
        self.CoordinatesLabel.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.CoordinatesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CoordinatesLabel.setObjectName("CoordinatesLabel")
        self.PressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.PressureLabel.setGeometry(QtCore.QRect(580, 385, 200, 30))
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
        self.Time = QtWidgets.QLabel(self.centralwidget)
        self.Time.setGeometry(QtCore.QRect(20, 50, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Time.setFont(font)
        self.Time.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Time.setAlignment(QtCore.Qt.AlignCenter)
        self.Time.setObjectName("Time")
        self.Temp = QtWidgets.QLabel(self.centralwidget)
        self.Temp.setGeometry(QtCore.QRect(580, 50, 200, 30))
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
        self.Humidity = QtWidgets.QLabel(self.centralwidget)
        self.Humidity.setGeometry(QtCore.QRect(580, 335, 200, 30))
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
        self.Pressure = QtWidgets.QLabel(self.centralwidget)
        self.Pressure.setGeometry(QtCore.QRect(580, 415, 200, 30))
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
        self.READY = QtWidgets.QLabel(self.centralwidget)
        self.READY.setGeometry(QtCore.QRect(320, 420, 75, 30))
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
        self.GearP = QtWidgets.QLabel(self.centralwidget)
        self.GearP.setGeometry(QtCore.QRect(395, 420, 30, 30))
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
        self.GearR = QtWidgets.QLabel(self.centralwidget)
        self.GearR.setGeometry(QtCore.QRect(415, 420, 30, 30))
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
        self.GearN = QtWidgets.QLabel(self.centralwidget)
        self.GearN.setGeometry(QtCore.QRect(435, 420, 30, 30))
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
        self.GearD = QtWidgets.QLabel(self.centralwidget)
        self.GearD.setGeometry(QtCore.QRect(455, 420, 30, 30))
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
        self.Warning = QtWidgets.QLabel(self.centralwidget)
        self.Warning.setGeometry(QtCore.QRect(385, 390, 30, 25))
        self.Warning.setText("")
        self.Warning.setTextFormat(QtCore.Qt.AutoText)
        self.Warning.setPixmap(QtGui.QPixmap("Warning-OFF.png"))
        self.Warning.setScaledContents(True)
        self.Warning.setObjectName("Warning")
        self.Charging = QtWidgets.QLabel(self.centralwidget)
        self.Charging.setGeometry(QtCore.QRect(415, 390, 30, 25))
        self.Charging.setText("")
        self.Charging.setTextFormat(QtCore.Qt.AutoText)
        self.Charging.setPixmap(QtGui.QPixmap("Charging-OFF.png"))
        self.Charging.setScaledContents(True)
        self.Charging.setObjectName("Charging")
        self.Lights = QtWidgets.QLabel(self.centralwidget)
        self.Lights.setGeometry(QtCore.QRect(355, 390, 30, 25))
        self.Lights.setText("")
        self.Lights.setTextFormat(QtCore.Qt.AutoText)
        self.Lights.setPixmap(QtGui.QPixmap("Lights-OFF.png"))
        self.Lights.setScaledContents(True)
        self.Lights.setObjectName("Lights")
        self.LeftSignal = QtWidgets.QLabel(self.centralwidget)
        self.LeftSignal.setGeometry(QtCore.QRect(325, 390, 30, 25))
        self.LeftSignal.setText("")
        self.LeftSignal.setTextFormat(QtCore.Qt.AutoText)
        self.LeftSignal.setPixmap(QtGui.QPixmap("LeftSignal-OFF.png"))
        self.LeftSignal.setScaledContents(True)
        self.LeftSignal.setObjectName("LeftSignal")
        self.RightSignal = QtWidgets.QLabel(self.centralwidget)
        self.RightSignal.setGeometry(QtCore.QRect(445, 390, 30, 25))
        self.RightSignal.setText("")
        self.RightSignal.setTextFormat(QtCore.Qt.AutoText)
        self.RightSignal.setPixmap(QtGui.QPixmap("RightSignal-OFF.png"))
        self.RightSignal.setScaledContents(True)
        self.RightSignal.setObjectName("RightSignal")
        self.CoordinatesX = QtWidgets.QLabel(self.centralwidget)
        self.CoordinatesX.setGeometry(QtCore.QRect(30, 340, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.CoordinatesX.setFont(font)
        self.CoordinatesX.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.CoordinatesX.setObjectName("CoordinatesX")
        self.CoordinatesY = QtWidgets.QLabel(self.centralwidget)
        self.CoordinatesY.setGeometry(QtCore.QRect(30, 375, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.CoordinatesY.setFont(font)
        self.CoordinatesY.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.CoordinatesY.setObjectName("CoordinatesY")
        self.Humidity_4 = QtWidgets.QLabel(self.centralwidget)
        self.Humidity_4.setGeometry(QtCore.QRect(30, 410, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Humidity_4.setFont(font)
        self.Humidity_4.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Humidity_4.setObjectName("Humidity_4")
        self.Speed = QtWidgets.QLabel(self.centralwidget)
        self.Speed.setGeometry(QtCore.QRect(20, 140, 200, 100))
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
        self.SpeedUnit = QtWidgets.QLabel(self.centralwidget)
        self.SpeedUnit.setGeometry(QtCore.QRect(20, 250, 200, 30))
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
        self.Time_4 = QtWidgets.QLabel(self.centralwidget)
        self.Time_4.setGeometry(QtCore.QRect(580, 250, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        self.Time_4.setFont(font)
        self.Time_4.setStyleSheet("QLabel {\n"
"    color: #b4ffc1; /* Set the color of the QLabel text */\n"
"}")
        self.Time_4.setAlignment(QtCore.Qt.AlignCenter)
        self.Time_4.setObjectName("Time_4")
        self.Battery = QtWidgets.QLabel(self.centralwidget)
        self.Battery.setGeometry(QtCore.QRect(580, 140, 200, 100))
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
        self.Background.raise_()
        self.LOGO.raise_()
        self.TimeBox.raise_()
        self.SpeedBox.raise_()
        self.AccelCoords.raise_()
        self.MapBox.raise_()
        self.TempBox.raise_()
        self.BatteryBox.raise_()
        self.HumidityBox.raise_()
        self.PressureBox.raise_()
        self.AuxiliaryBox.raise_()
        self.Shell_Logo.raise_()
        self.TimeLabel.raise_()
        self.SpeedLabel.raise_()
        self.BatteryLabel.raise_()
        self.TempLabel.raise_()
        self.HumidityLabel.raise_()
        self.CoordinatesLabel.raise_()
        self.PressureLabel.raise_()
        self.Time.raise_()
        self.Temp.raise_()
        self.Humidity.raise_()
        self.Pressure.raise_()
        self.READY.raise_()
        self.GearP.raise_()
        self.GearR.raise_()
        self.GearN.raise_()
        self.GearD.raise_()
        self.Warning.raise_()
        self.Charging.raise_()
        self.Lights.raise_()
        self.LeftSignal.raise_()
        self.RightSignal.raise_()
        self.CoordinatesX.raise_()
        self.CoordinatesY.raise_()
        self.Humidity_4.raise_()
        self.Speed.raise_()
        self.SpeedUnit.raise_()
        self.Time_4.raise_()
        self.Battery.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TimeLabel.setText(_translate("MainWindow", "Time"))
        self.SpeedLabel.setText(_translate("MainWindow", "Speed"))
        self.BatteryLabel.setText(_translate("MainWindow", "Battery"))
        self.TempLabel.setText(_translate("MainWindow", "Temp"))
        self.HumidityLabel.setText(_translate("MainWindow", "Humidity"))
        self.CoordinatesLabel.setText(_translate("MainWindow", "Coordinates"))
        self.PressureLabel.setText(_translate("MainWindow", "Pressure"))
        self.Time.setText(_translate("MainWindow", "12:00:00 AM"))
        self.Temp.setText(_translate("MainWindow", "75°C"))
        self.Humidity.setText(_translate("MainWindow", "50%"))
        self.Pressure.setText(_translate("MainWindow", "300hPa"))
        self.READY.setText(_translate("MainWindow", "READY"))
        self.GearP.setText(_translate("MainWindow", "P"))
        self.GearR.setText(_translate("MainWindow", "R"))
        self.GearN.setText(_translate("MainWindow", "N"))
        self.GearD.setText(_translate("MainWindow", "D"))
        self.CoordinatesX.setText(_translate("MainWindow", "X: 123"))
        self.CoordinatesY.setText(_translate("MainWindow", "Y: 234"))
        self.Humidity_4.setText(_translate("MainWindow", "Z: 345"))
        self.Speed.setText(_translate("MainWindow", "100"))
        self.SpeedUnit.setText(_translate("MainWindow", "km/h"))
        self.Time_4.setText(_translate("MainWindow", "%"))
        self.Battery.setText(_translate("MainWindow", "100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())