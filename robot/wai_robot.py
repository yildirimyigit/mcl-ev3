#!/usr/bin/env python3

'''
    Author: yigit.yildirim@boun.edu.tr
'''

from ev3dev2.button import Button
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import MoveDifferential, OUTPUT_B, OUTPUT_C, SpeedRPM
from ev3dev2.wheel import EV3EducationSetTire
from ev3dev2.sound import Sound
from ev3dev.ev3 import *
from time import sleep

import socket
import bluetooth


class WhereAmI:
    def __init__(self):
        self.host_bt_mac = "AC:FD:CE:82:1E:CC"
        self.port = 1
        self.backlog = 1
        self.size = 1024
        self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        self.s.bind((self.host_bt_mac, self.port))
        self.s.listen(self.backlog)

        self.us = UltrasonicSensor()
    def run(self):
        try:
            client, address = s.accept()
            while 1:
                data = client.recv(size)
                if data:
                    print(data)
                    client.send(data)
        except:	
            print("Closing socket")	
            client.close()
            s.close()


if __name__ == "__main__":
    wai = WhereAmI()
    wai.run()
