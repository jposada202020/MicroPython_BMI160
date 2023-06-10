# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bmi160 import bmi160

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bmi = bmi160.BMI160(i2c)

bmi.acceleration_output_data_rate = BMI160.BANDWIDTH_25_32

while True:
    for data_rate in BMI160.bandwidth_values:
        print("Current Acceleration Data Rate: ", bmi.acceleration_output_data_rate)
        for _ in range(10):
            accx, accy, accz = bmi.acceleration
            print("x:{:.2f}m/s2, y:{:.2f}m/s2, z{:.2f}m/s2".format(accx, accy, accz))
            time.sleep(0.5)
        bmi.acceleration_output_data_rate = data_rate
