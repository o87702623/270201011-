class Cylinder:
  def __init__(self, radius, height):
    self.set_radius(radius)
    self.set_height(height)
  
  def get_radius(self):
    return self.radius

  def set_radius(self,radius):
    if radius > 0:
      self.radius = radius
  
  def get_height(self):
    return self.height
  
  def set_height(self, height):
    if height > 0:
      self.height = height
  
  def base_area(self):
    return 3.14 * (self.radius ** 2)
  
  def surface_area(self):
    return 2 * (3.14 * self.radius) * self.height
  
  def area(self):
    return 2 * self.base_area() + self.surface_area()
  
  def vol(self):
    return self.base_area() * self.height
  
c = Cylinder(3, 5)
print("area = ", c.area())
print("volume = ", c.vol())