'''
    Author: yigit.yildirim@boun.edu.tr
'''

import sys
import time

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

from mcl import MCL


class WhereAmIPC(QWidget):
    def __init__(self):
        super().__init__()
        self.mcl = MCL()
        self.initUI()

        # gui-related variables
        self.gui_zoom = 4
        self.belief_magnification = 200
        self.start_y = 400

    def initUI(self):
        self.setGeometry(100, 100, 900, 500)
        self.setWindowTitle('Localization Monitor for CmpE 434')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_map(qp)
        self.draw_particles(qp)
        self.draw_pose(qp)
        qp.end()

    def run(self, movement_distance, sonar_reading):
        self.mcl.motion_update(movement_distance)
        self.mcl.measurement_update(sonar_reading)
        self.mcl.calculatePose()
        self.update()
        QtGui.QGuiApplication.processEvents()

    def draw_map(self, qp):
        qp.setPen(Qt.blue)
        for i in range(self.mcl.map.length):
            x = i
            y = self.mcl.map.expected_sonar_reading(i) + 80
            for j in range(self.gui_zoom):
               qp.drawPoint(x*self.gui_zoom+j, y)

    def draw_particles(self, qp):
        qp.setPen(Qt.red)
        for i in range(len(self.mcl.particles)):
            x = self.mcl.particles[i].location * self.gui_zoom
            height = self.mcl.particles[i].belief * self.belief_magnification

            qp.drawLine(x, self.start_y-height, x, self.start_y)
            

    def draw_pose(self, qp):
        qp.setPen(Qt.black)
        x = self.mcl.pose.location * self.gui_zoom
        height = self.mcl.pose.belief * self.belief_magnification
        qp.drawLine(x, self.start_y-height, x, self.start_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wai_pc = WhereAmIPC()
    distance = 20
    while wai_pc.isEnabled():
        distance += 1
        sonar = wai_pc.mcl.map.expected_sonar_reading(distance)
        wai_pc.run(1, sonar)
        time.sleep(0.5)
    sys.exit(app.exec_())
