'''
    Author: yigit.yildirim@boun.edu.tr
'''

from mcl import MCL

class WhereAmIPC:
    def __init__(self):
        self.mcl = MCL()

    def run(self, movement_distance, sonar_reading):
        self.mcl.motion_update(movement_distance)
        self.mcl.measurement_update(sonar_reading)
        self.mcl.calculatePose()


if __name__ == "__main__":
    wai_pc = WhereAmIPC()
    while True:
        distance = 0
        sonar = 0
        wai_pc.run(distance, sonar)
