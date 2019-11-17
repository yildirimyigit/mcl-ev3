#!/usr/bin/env python3

'''
    Author: yigit.yildirim@boun.edu.tr
'''

from ev3dev2.button import Button
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sound import Sound
from time import sleep


class WhereAmI:
    def __init__(self):
        self.us = UltrasonicSensor()
    def run(self):
        print('RUNNING...')


if __name__ == "__main__":
    wai = WhereAmI()
    wai.run()
