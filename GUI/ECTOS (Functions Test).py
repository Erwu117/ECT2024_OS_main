#Imports for GUI
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import math
import time
import board

#Imports for BME280
import smbus2
import bme280

#Imports for MPU6050
import smbus

#Import for DHT11
import adafruit_dht
from time import sleep
DHT_PIN = board.D4
dht_device = adafruit_dht.DHT11(board.D4)

# Initialize the bus for BME280s
bus = smbus2.SMBus(1)  # Use the appropriate bus number
address = 0x76  # BME280 default address
calibration_params = bme280.load_calibration_params(bus, address)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.centralwidget.setObjectName("centralwidget")

        #Acceleration
        self.accel = QtWidgets.QLabel(self.centralwidget)
        self.accel.setGeometry(QtCore.QRect(120, 330, 49, 16))
        self.accel.setObjectName("accel")

        #Temparature
        self.temp = QtWidgets.QLabel(self.centralwidget)
        self.temp.setGeometry(QtCore.QRect(620, 320, 49, 16))
        self.temp.setObjectName("temp")

        #X-coordinates
        self.xcord = QtWidgets.QLabel(self.centralwidget)
        self.xcord.setGeometry(QtCore.QRect(310, 410, 49, 16))
        self.xcord.setObjectName("xcord")

        #Y-coordinates
        self.ycord = QtWidgets.QLabel(self.centralwidget)
        self.ycord.setGeometry(QtCore.QRect(380, 410, 49, 16))
        self.ycord.setObjectName("ycord")

        #Z-coordinates
        self.zcord = QtWidgets.QLabel(self.centralwidget)
        self.zcord.setGeometry(QtCore.QRect(450, 410, 49, 16))
        self.zcord.setObjectName("zcord")

        #Humidity
        self.humidity = QtWidgets.QLabel(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(380, 290, 49, 16))
        self.humidity.setObjectName("humidity")

        #Pressure
        self.pressure = QtWidgets.QLabel(self.centralwidget)
        self.pressure.setGeometry(QtCore.QRect(390, 350, 49, 16))
        self.pressure.setObjectName("pressure")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

def read_dht11():
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity
            if temperature_c is not None and humidity is not None:
                return temperature_c, humidity
        except Exception as e:
            print('Sensor read failed:', str(e))
            time.sleep(2)
    return None, None

def update_temperature_and_humidity(self):
        try:
            temperature, humidity = read_dht11()

            if temperature is not None and humidity is not None:
                self.temp.setText(f"{temperature}°C")
                self.humidity.setText(f"{humidity}%")
            else:
                print("Failed to read from DHT11 sensor after multiple attempts.")

            QTimer.singleShot(3000, self.update_temperature_and_humidity)
        except Exception as e:
            print('Sensor read failed:', str(e))

def update_pressure(self):
    try:
        bme_device = BME280(bus, address)
        pressure = int(bme_device.get_pressure())
        self.pressure.setText(str(pressure))

        QTimer.singleShot(1000, self.update_pressure)
    except Exception as e:
        print('Sensor read failed:', str(e))

def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.accel.setText(_translate("MainWindow", "TextLabel"))
    self.temp.setText(_translate("MainWindow", "TextLabel"))
    self.xcord.setText(_translate("MainWindow", "TextLabel"))
    self.ycord.setText(_translate("MainWindow", "TextLabel"))
    self.zcord.setText(_translate("MainWindow", "TextLabel"))
    self.humidity.setText(_translate("MainWindow", "TextLabel"))
    self.pressure.setText(_translate("MainWindow", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    update_temperature_and_humidity()

    update_pressure()

    app.mainloop()
    sys.exit(app.exec_())