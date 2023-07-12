# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from machine import Pin, I2C
from micropython_bmi160 import bmi160

i2c = I2C(1, sda=Pin(2), scl=Pin(3))  # Correct I2C pins for RP2040
bmi = bmi160.BMI160(i2c)

bmi.acceleration_output_data_rate = bmi160.BANDWIDTH_25_32

while True:
    for data_rate in bmi160.bandwidth_values:
        print("Current Acceleration Data Rate: ", bmi.acceleration_output_data_rate)
        for _ in range(10):
            accx, accy, accz = bmi.acceleration
            print(f"x:{accx:.2f}m/s2, y:{accy:.2f}m/s2, z{accz:.2f}m/s2")
            time.sleep(0.5)
        bmi.acceleration_output_data_rate = data_rate
