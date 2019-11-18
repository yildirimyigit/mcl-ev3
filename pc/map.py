'''
    Author: yigit.yildirim@boun.edu.tr
'''

'''
    Class that describes the environment.
    It basically keeps the information about (location-sonar reading) pairs. 
'''
class Map:
    def __init__(self):
        self.near = 20
        self.moderate = 40
        self.far = 60
        self.length = 200

    '''
        The map can be depicted as follows:

         ||       (Finish: 200)
MODERATE ||    
         ||
    ||
FAR ||
    ||
         ||
MODERATE ||
         ||
    ||
FAR ||
    ||
             ||
NEAR         ||
             ||  R (Start: 0)
    '''
    def expected_sonar_reading(self, location):
        if 0 <= location < 30:
            return self.near
        elif 30 <= location < 100:
            return self.far
        elif 100 <= location < 140:
            return self.moderate
        elif 140 <= location < 170:
            return self.far
        else:
            return self.moderate
