class circle:
 def __init__(self,ra):
  self.radius = ra

 def areaofcircle(self):
  return self.radius**2*3.14159265359

newcircle = circle(7)
print("Radius of circle:",newcircle.radius)
print("Area of circle:",newcircle.areaofcircle())    