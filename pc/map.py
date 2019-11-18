'''
    Author: yigit.yildirim@boun.edu.tr
'''

'''
    Class that describes the environment.
    It basically keeps the information about (location-sonar reading) pairs. 
'''
class Map:
    def __init__(self):
        self.near = 200
        self.moderate = 400
        self.far = 600
        self.length = 2000

    '''
        The map can be depicted as follows:

         ||       (Finish: 2000)
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
        if 0 <= location < 300:
            return self.near
        elif 300 <= location < 1000:
            return self.far
        elif 1000 <= location < 1400:
            return self.moderate
        elif 1400 <= location < 1700:
            return self.far
        else:
            return self.moderate
