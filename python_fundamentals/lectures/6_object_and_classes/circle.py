class Circle:
    diameter = 10
    angle = 5
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = self.diameter / 2

    def calculate_circumference(self):
        return 2 * self.radius * self.__pi

    def calculate_area(self):
        return self.__pi * self.radius**2

    def calculate_area_of_sector(self, angle):
        return (angle/360) * self.__pi * self.radius**2
