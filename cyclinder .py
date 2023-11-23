# Define cyclinder class to find it's surface area and volumne

class Cylinder():
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.surface_area = None
        self.volume = None
    

test = Cylinder(100, 1)
print('Height:', str(test.height))
print('Radius:', str(test.radius))

print('Surface Area:', test.surface_area)