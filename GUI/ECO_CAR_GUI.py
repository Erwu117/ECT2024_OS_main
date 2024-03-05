#Imports for GUI
import tkinter as tk
import math
import tkintermapview
import time
import board

#Imports for BME280
import smbus2
import bme280

#Imports for MPU6050
import smbus

#Import for DHT11
import adafruit_dht


app = tk.Tk()
app.title("CAR GUI")
app.geometry("800x480")
app.configure(bg='white')
screen_width = 800
screen_height = 480

# Global variables
current_color = 'black'
yellow_filled = False
accel = 0
speed = 0
speed2 = 0
speaker_filled = False
warning_filled = False
is_glowing = False
glow_after_id = None
is_glowing2 = False
glow_after_id2 = None
temperature_celsius = 0

# Initialize the bus for BME280s
bus = smbus2.SMBus(1)  # Use the appropriate bus number
address = 0x76  # BME280 default address
calibration_params = bme280.load_calibration_params(bus, address)
bme_device = bme280.sample(bus, address, calibration_params)


# Initialize MPU6050
mpu6050_bus = smbus.SMBus(1)  # If it's the same physical bus as BME280, consider using just one bus variable
Device_Address = 0x68  # MPU6050 device address
# MPU6050 Registers
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
ACCEL_CONFIG = 0x1C
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47


# Initialize DHT11
dht_device = adafruit_dht.DHT11(board.D4)


def Degree_functionchange():
    global temperature_celsius  # Assuming you have a mechanism to update this variable periodically
    
    label5.config(text=str(temperature_celsius))
    # Adjust label position based on temperature length
    if len(str(temperature_celsius)) == 2:
        label5.place(relx=0.45, rely=0.87)
    elif len(str(temperature_celsius)) > 2:  
        label5.place(relx=0.43, rely=0.87)  
    else:
        label5.place(relx=0.47, rely=0.87)

def update_temperature():
    try:
        global temperature_celsius
        temperature_celsius = dht_device.temperature
        Degree_functionchange()
        app.after(1000, update_temperature)
    except Exception as e:
        print('Sensor read failed:', e)

def update_humidity():
    try:
        global humidity
        humidity = dht_device.humidity
        app.after(1000, update_humidity)
    except Exception as e:
        print('Sensor read failed:', e)

def update_pressure():
    try:
        global pressure
        pressure = bme_device.pressure
        app.after(1000, update_pressure)
    except Exception as e:
        print('Sensor read failed:', e) 

def update_speed(event=None): #In Progress
    global speed

    # magnitude = math.sqrt(sum(a**2 for a in speed))

    # speed = magnitude

    speed_str = "{:.2f}".format(speed)
    if speed < 160:
        speedometer.itemconfigure(label, text=str(speed_str))

    if len(str(speed_str)) == 2:
        speedometer.coords(label, 125, 105)
    elif len(str(speed_str)) > 2:  
        speedometer.coords(label, 124, 105)
    else:
        speedometer.coords(label, 127, 105,)
    
    angle = math.radians(135 + (speed / max_speed) * 360)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    speedometer.coords(speed_indicator, center_x, center_y, x, y)

def MPU_Init():
    # Wake-up the MPU6050
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 0)
    
    # Write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
    
    # Write to power management register to wake up the MPU6050
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    # Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)
    
    # Write to Gyro configuration register to set full-scale range
    # Example: ±250 degrees/second (0x00)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 0x00)
    
    # Write to Accel configuration register to set full-scale range
    # Example: ±2g (0x00)
    bus.write_byte_data(Device_Address, ACCEL_CONFIG, 0x00)
    
    # Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	high = bus.read_byte_data(Device_Address, addr)
	low = bus.read_byte_data(Device_Address, addr+1)
	value = ((high << 8) | low)
	if(value > 32768):
			value -= 65536
	return value

def read_accel(): # MPU6050
    global accel, Ax, Ay, Az

    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)

    Ax = (acc_x/16384.0) * 9.80665
    Ay = (acc_y/16384.0) * 9.80665
    Az = (acc_z/16384.0) * 9.80665
    
    #accel = math.sqrt(Ax**2 + Ay**2 + Az**2)

    #formatted_accel = "{:.2f}".format(accel)
    formatted_Ax = "{:.2f}".format(Ax)
    formatted_Ay = "{:.2f}".format(Ay)
    formatted_Az = "{:.2f}".format(Az)

    #accelerometerlabel.config(text=f"Acceleration: {formatted_accel} m/s²")
    Axlabel.config(text=f"{formatted_Ax} m/s²")
    Aylabel.config(text=f"{formatted_Ay} m/s²")
    Azlabel.config(text=f"{formatted_Az} m/s²")
    app.after(1000, read_accel)



def update_batt(event=None):
    global speed2
    if speed2 <100:
        speed2 += 1 
        label3.config(text=str(speed2))

    if len(str(speed2)) == 2:
        label3.place(relx=0.771, rely=0.65) 
    elif len(str(speed2)) > 2:  
        label3.place(relx=0.751, rely=0.65)  
    else:
        label3.place(relx=0.79, rely=0.65) 

def lower_batt(event=None):
    global speed2
    if speed2 > 0:
        speed2 -= 1  
        label3.config(text=str(speed2))

    if len(str(speed2)) == 2:
        label3.place(relx=0.771, rely=0.65) 
    elif len(str(speed2)) > 2:  
        label3.place(relx=0.751, rely=0.65) 
    else:
        label3.place(relx=0.79, rely=0.65) 

def left_lane(event=None):
    global is_glowing
    is_glowing = not is_glowing  # Toggle glowing state
    if is_glowing:
        glow()
    else:
        canvas.itemconfigure(object_id, fill='black')  # Reset object color
        # Cancel scheduled glow
        if glow_after_id:
            canvas.after_cancel(glow_after_id)

def glow():
    canvas.itemconfigure(object_id, fill='#FDDA0D')  # Set object color to yellow (glowing)
    global glow_after_id
    glow_after_id = canvas.after(1000, dim)  # Schedule dimming after 1 second

def dim():
    canvas.itemconfigure(object_id, fill='black')  # Reset object color
    global glow_after_id
    glow_after_id = canvas.after(1000, glow)  # Schedule glowing after 1 second

def right_lane(event=None):
    global is_glowing2  # Change the variable name to differentiate between canvas objects
    is_glowing2 = not is_glowing2  # Toggle glowing state for canvas2
    if is_glowing2:
        glow2()
    else:
        canvas2.itemconfigure(object_id2, fill='black')  # Reset object color for canvas2
        # Cancel scheduled glow
        if glow_after_id2:
            canvas2.after_cancel(glow_after_id2)

def glow2():
    canvas2.itemconfigure(object_id2, fill='#FDDA0D')  # Set object color to yellow (glowing) for canvas2
    global glow_after_id2
    glow_after_id2 = canvas2.after(1000, dim2)  # Schedule dimming after 1 second for canvas2

def dim2():
    canvas2.itemconfigure(object_id2, fill='black')  # Reset object color for canvas2
    global glow_after_id2
    glow_after_id2 = canvas2.after(1000, glow2)  
def update_label():
    current_time = time.strftime("%I:%M %p")    # Get current time
    timelabel.config(text=current_time)  # Update label text with current time
    timelabel.after(1000, update_label) 



def ready_green(event=None):
    global current_color
    # Toggle between black and green
    current_color = '#7CFC00' if current_color == 'black' else 'black'
    ReadyLabel.config(fg=current_color) 


def reset_labels():
    labelP.config(fg='Grey')
    labelR.config(fg='Grey')
    labelN.config(fg='Grey')
    labelD.config(fg='Grey')

def P_function(event):
    reset_labels()
    labelP.config(fg='#A32C3A')

def R_function(event):
    reset_labels()
    labelR.config(fg='Orange')

def N_function(event):
    reset_labels()
    labelN.config(fg='Black')

def D_function(event):
    reset_labels()
    labelD.config(fg='Dark Green')
def light_function(event=None):
    global yellow_filled
    if yellow_filled:
        canvas3.itemconfig(line1, fill='black')
        canvas3.itemconfig(line2, fill='black')
        canvas3.itemconfig(line3, fill='black')
    else:
        canvas3.itemconfig(line1, fill='#FDDA0D')
        canvas3.itemconfig(line2, fill='#FDDA0D')
        canvas3.itemconfig(line3, fill='#FDDA0D')
    yellow_filled = not yellow_filled
def speaker_function(event=None):
    global speaker_filled
    if speaker_filled:
        canvas4.itemconfig(speaker1, outline='black')
        canvas4.itemconfig(speaker2, fill='black')
        canvas4.itemconfig(speaker3, fill='black')
        canvas4.itemconfig(speaker4, fill='black')
        canvas4.itemconfig(speaker5, fill='black')
        canvas4.itemconfig(speaker6, fill='black')
    else:
        canvas4.itemconfig(speaker1, outline='#FDDA0D')
        canvas4.itemconfig(speaker2, fill='#FDDA0D')
        canvas4.itemconfig(speaker3, fill='#FDDA0D')
        canvas4.itemconfig(speaker4, fill='#FDDA0D')
        canvas4.itemconfig(speaker5, fill='#FDDA0D')
        canvas4.itemconfig(speaker6, fill='#FDDA0D')
    speaker_filled = not speaker_filled
def warning_function(event=None):
    global warning_filled
    if warning_filled:
        canvas5.itemconfig(warning1, fill='white')
    else:
        canvas5.itemconfig(warning1, fill='#FDDA0D')
    warning_filled = not warning_filled



max_speed = 200     
current_color = 'black' 
yellow_filled = False
speed = 0
speed2 = 0
speaker_filled = False
warning_filled = False
degree = 0

map_widget= tkintermapview.TkinterMapView(app,width=800, height=240, corner_radius=0)
map_widget.pack()

map_widget.set_position(-8.8952780, 116.3058330)
map_widget.set_zoom(100)


speedometer = tk.Canvas(app, width=400, height=300,bg='white', highlightthickness=0)
speedometer.place(relx=0.03, rely=0.5)
rspeedometer = tk.Canvas(app, width=400, height=400,bg='white', highlightthickness=0)
rspeedometer.place(relx=0.65, rely=0.5)
rspeedometer2 = tk.Canvas(app, width=145, height=240,bg='white', highlightthickness=0)
rspeedometer2.place(relx=0.724, rely=0.776)
rfixspeed = tk.Canvas(app, width=150, height=80,bg='white', highlightthickness=0)
rfixspeed.place(relx=0.72, rely=0.95)




canvas = tk.Canvas(app, width=20, height=20, bg='white', highlightthickness=0)
canvas.place(relx=0.39,rely=0.66)
canvas2 = tk.Canvas(app, width=20, height=20, bg='white', highlightthickness=0)
canvas2.place(relx=0.59,rely=0.66)
canvas3 = tk.Canvas(app, width=20, height=20, bg='white', highlightthickness=0)
canvas3.place(relx=0.53,rely=0.66)
canvas4 = tk.Canvas(app, width=20, height=20, bg='white', highlightthickness=0)
canvas4.place(relx=0.43,rely=0.66)
canvas5 = tk.Canvas(app, width=20, height=20, bg='white', highlightthickness=0)
canvas5.place(relx=0.485,rely=0.66)






# Draw an object (circle in this example)
object_id = canvas.create_polygon(10, 3, 10, 16, 0, 10, fill='black') 
object_id2 = canvas2.create_polygon(0, 3, 10, 10, 0, 16, fill='black')
line1= canvas3.create_line(10, 10, 18, 10, fill='black', width=4)
line2= canvas3.create_line(15, 1, 11, 11, fill='black', width=4)
line3= canvas3.create_line(20, 9, 13, 18, fill='black', width=4)
speaker1=canvas4.create_arc(2, 2, 18, 18, start=-90, extent=180, style=tk.ARC, outline='black', fill='black', width=4)
speaker2=canvas4.create_line(12, 2, 12, 18, fill='black', width=6)
speaker3=canvas4.create_line(14, 3, 14, 16, fill='black', width=6)
speaker4=canvas4.create_line(1, 2, 7, 7, fill='black', width=2)
speaker5=canvas4.create_line(1, 10, 7, 9, fill='black', width=2)
speaker6=canvas4.create_line(1, 18, 7, 12, fill='black', width=2)
warning1=canvas5.create_polygon(2, 18, 18, 18, 10, 2, fill='white', outline='black')
canvas5.create_text(10, 12, text='!', fill='black')
is_glowing = False
glow_after_id = None
is_glowing2 = False
glow_after_id2 = None



custom_font= ("Montserrat", 40,)
custom_font2= ("Montserrat", 13, "bold")
custom_font3= ("Montserrat", 12, "bold")
custom_font4= ("Montserrat", 8, "bold")

speedometer.create_oval(15, 5, 235, 235,  outline="black", width=3)
speedometer.create_oval(25, 10, 225, 225,  outline="black", width=3)

num_intervals = 10
line_length = 30

interval_angle = 360 / num_intervals

radius = (200) / 2
center_x = (250) / 2
center_y = (235) / 2

for i in range(num_intervals + 1):
    angle = math.radians(135 + i * interval_angle)
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    x_end = center_x + (radius - line_length) * math.cos(angle)
    y_end = center_y + (radius - line_length) * math.sin(angle)
    speedometer.create_line(x, y, x_end, y_end, fill='black', width=2)

# Draw the speed indicator

rspeedometer.create_arc(15, 10, 245, 245, start=-45, extent=270, outline="black", width=3)
rspeedometer.create_arc(25, 15, 235, 235, start=-45, extent=270, outline="black", width=3)



rspeedometer2.create_arc(-10, 65, 150, 150, start=-45, extent=270, outline="black", width=3)
rspeedometer2.create_arc(0, 70, 140, 155, start=-45, extent=270, outline="black", width=3)

label = speedometer.create_text(127, 105, text="0", fill='black', font=custom_font)
label2 = speedometer.create_text(126, 150, text="km/hr", fill='black', font=custom_font2)

speed_indicator = speedometer.create_line(center_x, center_y, center_x, center_y, fill='red', width=1.5)
speed_indicatordot = speedometer.create_oval(125,118, 125, 118, fill='red', width = 3)

label3 = tk.Label(app, text="0", bg = 'white',font=custom_font)
label4 = tk.Label(app, text=" % ", bg = 'white',font=custom_font3)
label3.place(relx= 0.79, rely=0.65)
label4.place(relx= 0.79, rely=0.78)

label5 = tk.Label(app, text="0", bg = 'white',font=custom_font3)
label5.place(relx= 0.47, rely=0.86)
label6 = tk.Label(app, text="°C", bg = 'white',font=custom_font2)
label6.place(relx= 0.495, rely=0.875)

accelerometerlabel = tk.Label(app, text="0", bg = 'white',font=custom_font2)
accelerometerlabel.place(relx= 0.43, rely=0.93)
Axlabel = tk.Label(app, text="0", bg = 'white',font=custom_font4)
Axlabel.place(relx= 0.44, rely=0.93)
Aylabel = tk.Label(app, text="0", bg = 'white',font=custom_font4)
Aylabel.place(relx= 0.51, rely=0.93)
Azlabel = tk.Label(app, text="0", bg = 'white',font=custom_font4)
Azlabel.place(relx= 0.37, rely=0.93)



labelP = tk.Label(app, text="P", bg = 'white',fg= 'grey',font=custom_font2)
labelR= tk.Label(app, text="R", bg = 'white',fg= 'grey',font=custom_font2)
labelN = tk.Label(app, text="N", bg = 'white',fg= 'grey',font=custom_font2)
labelD= tk.Label(app, text="D", bg = 'white', fg= 'grey', font=custom_font2)
labelP.place(relx= 0.445, rely=0.8)
labelR.place(relx= 0.475, rely=0.8)
labelN.place(relx= 0.505, rely=0.8)
labelD.place(relx= 0.535, rely=0.8)

timelabel = tk.Label(app, bg= 'white', font=custom_font2 )
timelabel.place(relx=0.456, rely=0.582)

ReadyLabel = tk.Label(app, text="READY", bg = 'white',font=custom_font2)
ReadyLabel.place(relx= 0.463, rely=0.73)



app.bind('<KeyPress-4>', update_batt)
app.bind('<KeyPress-5>', lower_batt)
app.bind('<KeyPress-Left>', left_lane)
app.bind('<KeyPress-Right>', right_lane)
app.bind('<KeyPress-1>', ready_green)
app.bind('<KeyPress-0>', P_function)
app.bind('<KeyPress-9>', R_function)
app.bind('<KeyPress-8>', N_function)
app.bind('<KeyPress-7>', D_function)
app.bind('<KeyPress-Up>', light_function)
app.bind('<KeyPress-Down>', speaker_function)
app.bind('<KeyPress-6>', warning_function)


Degree_functionchange()
app.focus_set()

update_speed()
update_temperature()
update_label()

#MPU6050
MPU_Init()
read_accel()

app.mainloop()