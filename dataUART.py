from machine import Pin, SoftI2C, Timer, SoftSPI, UART#匯入Pin及I2C模組
from imu import MPU6050#匯入 MPU6050 模組
from utime import sleep #匯入時間模組(暫停)
import os
i2c1=SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)#建立SoftI2C類別物件(MPU6050)
imu = MPU6050(i2c1) #inerti al moti on sensor 47 /# (MPU6050)
uart = UART(1,baudrate=115200, tx=17, rx=16) #以UART傳輸至python介面
#drive_path = '/sd'

number = 2
data_number = 0 
def get_data(self):
    global number, data_number
    acc=imu.accel.xyz#獲取三軸加速度值
    gyro = imu.gyro.xyz#獲取三軸角速度
    # write_label = f'acX{number}\tacY{0}\tacZ{0}\tgvroX{0}\tgvroY{0}\tgvorZ{0}\t{ID}\n'
    # 將六軸資料寫入txt檔
    if (number != 150):
        write_str_acc  = str(acc[0] )[0:4] + "\t" + str(acc[1] )[0:4] + "\t"
        write_str_gvro = str(gyro[0])[0:4] + "\t" + str(gyro[1])[0:4] + "\t" + str(gyro[2])[0:4]+"\t"
        number += 2
    elif (number == 150):
        write_str_acc  = str(acc[0] )[0:4] + "\t" + str(acc[1] )[0:4] + "\n"
        write_str_gvro = str(gyro[0])[0:4] + "\t" + str(gyro[1])[0:4] + "\t" + str(gyro[2])[0:4]+"\n"
        number  = 2
        data_number += 1
    
    uart.write(write_str_acc)
    

tim1=Timer(1)
tim1.init(period = 50, mode = Timer.PERIODIC, callback = get_data) #設定成週期性觸發，每50ms觸發一次

while True:
    sleep(1)
    
