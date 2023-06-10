# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bmi160 import bmi160

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bmi = bmi160.BMI160(i2c)

bmi.gyro_output_data_rate = BMI160.BANDWIDTH_200

while True:
    for data_rate in BMI160.gyro_bandwidth_values:
        print("Current Gyro Data Range: ", bmi.gyro_output_data_rate)
        for _ in range(10):
            gyrox, gyroy, gyroz = bmi.gyro
            print("x:{:.2f}°/s, y:{:.2f}°/s, z{:.2f}°/s".format(gyrox, gyroy, gyroz))
            time.sleep(0.5)
        bmi.gyro_output_data_rate = data_rate
