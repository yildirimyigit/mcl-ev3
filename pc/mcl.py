'''
    Author: yigit.yildirim@boun.edu.tr
'''

import random
import math

from particle import Particle
from map import Map

class MCL:
    def __init__(self, world_length=2000, num_particles=50):
        self.measurement_sigma = 20
        self.movement_sigma = 20

        self.particles = []
        for _ in range(num_particles):
            self.particles.append(Particle())

        self.pose = Particle()
        self.map = Map()
        self.reset()

    def measurement_model(self, sonar_reading, location):
        expected_sonar_reading = self.map.expected_sonar_reading(location)
        prob = gaussian(sonar_reading, expected_sonar_reading, self.measurement_sigma)
        return prob

    def motion_model(self, movement_distance):
        return random.normalvariate(movement_distance, self.movement_sigma)

    def measurement_update(self):
        pass

    def motion_update(self):
        pass

    def calculatePose(self):
        pass

    def resample(self):
        pass

    '''
        Resets all particles with random locations and same belief
    '''
    def reset(self):
        bel_reset = 1/len(self.particles)  # belief of an individual
        for particle in self.particles:
            particle.location = random.randrange(2000)
            particle.belief = bel_reset

'''
    Value of a variable under gaussian distribution
'''
def gaussian(x, m, s):
    return math.pow(math.e, -(math.pow((x-m), 2) / (2*s*s))) / math.sqrt(2*math.pi*s*s)