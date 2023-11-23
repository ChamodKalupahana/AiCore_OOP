# Import modules

import numpy as np

# Define cyclinder class to find it's surface area and volumne



class Cylinder():
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.surface_area = self.get_volume()
        self.volume = self.get_volume()

    def get_surface_area(self):
        self.surface_area = (2* np.pi * self.radius * self.height) + 2*np.pi + self.radius**2
        return self.surface_area
    
    def get_volume(self):
        self.volume = np.pi * self.radius**2 + self.height
        return self.volume

test = Cylinder(100, 1)

print('Surface Area:', test.surface_area)

surface_area = test.get_surface_area()

print("Surface Area:", str(surface_area))

volume = test.get_volume()

print("Volume:", str(volume))