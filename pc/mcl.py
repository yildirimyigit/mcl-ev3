'''
    Author: yigit.yildirim@boun.edu.tr
'''

import random
import math

from particle import Particle
from map import Map

class MCL:
    def __init__(self, num_particles=100):
        self.measurement_sigma = 1
        self.movement_sigma = 1
        self.delta = 2  # distortion coeff
        self.num_particles = num_particles

        self.particles = []
        for _ in range(num_particles):
            self.particles.append(Particle())

        self.pose = Particle()
        self.map = Map()
        self.reset()

    def measurement_model(self, current_sonar_reading, location):
        expected_sonar_reading = self.map.expected_sonar_reading(location)
        prob = gaussian(current_sonar_reading, expected_sonar_reading, self.measurement_sigma)
        return prob

    def motion_model(self, movement_distance):
        return random.normalvariate(movement_distance, self.movement_sigma)

    def measurement_update(self, current_sonar_reading):
        for particle in self.particles:
            particle.belief = self.measurement_model(current_sonar_reading, particle.location)
        self.resample()

    def motion_update(self, movement_distance):
        for particle in self.particles:
            particle.location += int(self.motion_model(movement_distance))
            if particle.location > self.map.length:
                particle.location = self.map.length
            # elif particle.location < 0:
            #     particle.location = 0

    '''
        Calculate and return the average location and belief as the position estimation
    '''
    def calculatePose(self):
        location = 0
        belief = 0
        for particle in self.particles:
            location += particle.location * particle.belief
            belief += particle.belief
        self.pose.location = int(location / self.num_particles)
        self.pose.belief = belief / self.num_particles

    def resample(self):
        resampled = []
        sum_belief = 0
        for particle in self.particles:
            sum_belief += particle.belief

        avg_belief = sum_belief/self.num_particles
        for particle in self.particles:
            if particle.belief > avg_belief:    # if it deserves, generate a clone with random distortion
                temp = particle
                temp.location += int(self.delta * random.random())    # distortion
                if temp.location > self.map.length:
                    temp.location = self.map.length
                resampled.append(temp)

        for i in range(self.num_particles):
            if i < len(resampled):  # copy the resampled ones
                self.particles[i] = resampled[i]
            else:   # fill the list with random particles
                temp = Particle()
                self.particles[i] = self.reset_individual(temp)

    '''
        Reset all particles with random locations and same belief
    '''
    def reset(self):
        for particle in self.particles:
            particle = self.reset_individual(particle)

    def reset_individual(self, particle):
        particle.location = random.randrange(self.map.length)
        particle.belief = 1/self.num_particles
        return particle


'''
    Value of a variable under gaussian distribution
'''
def gaussian(x, m, s):
    return math.pow(math.e, -(math.pow((x-m), 2) / (2*s*s))) / math.sqrt(2*math.pi*s*s)