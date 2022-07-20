import math
class Figure:
  def Move(self, h, v):
    for i in range(len(self.coordinates['x'])):
      self.coordinates['x'][i]+=h
      self.coordinates['y'][i]+=v
      
  def Rotate(self, degrees):
    #formula uses radian, conversion from degrees to radian required
    radian=degrees*(math.pi/180)
    # center of figures with only 1 coordinate would be the coordinate itself
    center_x=self.coordinates['x'][0]
    center_y=self.coordinates['y'][0]
   # FORMULA for Rotating about the center of figure
    # x?=(x-xc)cos(?)?(y-yc)sin(?)+xc
    # y?=(x-xc)sin(?)+(y-yc)cos(?)+yc
    for i in range(len(self.coordinates['x'])):
      temp = ((self.coordinates['x'][i]-center_x)*math.cos(radian)) - ((self.coordinates['y'][i]-center_y)*math.sin(radian))+center_x
      self.coordinates['y'][i] = ((self.coordinates['x'][i]-center_x)*math.sin(radian)) + ((self.coordinates['y'][i]-center_y)*math.cos(radian))+center_y
      self.coordinates['x'][i]=temp

  def displayCoordinates(self):
    print('(', round(self.coordinates['x'][0], 2), ', ', round(self.coordinates['y'][0], 2), ')')
          
class Point(Figure):
  def __init__(self, x, y):
    self.coordinates={'x':[x], 'y':[y]}

class Line(Figure):
  def __init__(self, x1, y1, x2, y2):
    self.coordinates={'x':[x1,x2], 'y':[y1,y2]}
    
  def Rotate(self, degrees):
    radian=degrees*(math.pi/180)
    #find center of the line
    center_x= (self.coordinates['x'][1]-self.coordinates['x'][0])/2 
    center_y= (self.coordinates['y'][1]-self.coordinates['y'][0])/2
    
    for i in range(len(self.coordinates['x'])):
      temp = ((self.coordinates['x'][i]-center_x)*math.cos(radian)) - ((self.coordinates['y'][i]-center_y)*math.sin(radian))+center_x
      self.coordinates['y'][i] = ((self.coordinates['x'][i]-center_x)*math.sin(radian)) + ((self.coordinates['y'][i]-center_y)*math.cos(radian))+center_y
      self.coordinates['x'][i]=temp
  
  def displayCoordinates(self):
    print('(', round(self.coordinates['x'][0], 2), ', ', round(self.coordinates['y'][0], 2), ')', ', ''(', round(self.coordinates['x'][1], 2), ', ', round(self.coordinates['y'][1], 2), ')')

class Circle(Figure):
  def __init__(self, x, y, r):
    self.coordinates={'x':[x], 'y':[y], 'r':[r]}

class Aggregation(Figure):
  def __init__(self, *args):
    self.shapes=[]
    for i in args:
      self.shapes.append(i)
  #overriding methods move and rotate
  def Move(self, h, v):
    for shape in self.shapes:
      shape.Move(h,v)
      # for i in range(len(shape.coordinates['x'])):
      #   shape.coordinates['x'][i]+=h
      #   shape.coordinates['y'][i]+=v

  def Rotate(self, degrees):
    #formula uses radian, conversion from degrees to radian required
    radian=degrees*(math.pi/180)
    # Find the max and min x,y to calculate the center of the aggregation
    min_x=self.shapes[0].coordinates['x'][0]
    max_x=self.shapes[0].coordinates['x'][0]
    min_y=self.shapes[0].coordinates['y'][0]
    max_y=self.shapes[0].coordinates['y'][0]
    
    for shape in self.shapes:
      for i in range(len(shape.coordinates['x'])):
        if shape.coordinates['x'][i]>max_x:
          max_x=shape.coordinates['x'][i]
        elif shape.coordinates['x'][i]<min_x:
          min_x=shape.coordinates['x'][i]

        if shape.coordinates['y'][i]>max_y:
          max_x=shape.coordinates['y'][i]
        elif shape.coordinates['y'][i]<min_y:
          min_y=shape.coordinates['y'][i]
          
    #finding the center of aggregation       
    center_x= (max_x-min_x)/2 
    center_y= (max_y-min_y)/2

    #for each shape, and for each of its coordinates, calculate the 
    #rotation of the shape around the center of aggregation 
    for shape in self.shapes:
      for i in range(len(shape.coordinates['x'])):
        temp = ((shape.coordinates['x'][i]-center_x)*math.cos(radian)) - ((shape.coordinates['y'][i]-center_y)*math.sin(radian))+center_x
        shape.coordinates['y'][i] = ((shape.coordinates['x'][i]-center_x)*math.sin(radian)) + ((shape.coordinates['y'][i]-center_y)*math.cos(radian))+center_y
        shape.coordinates['x'][i]=temp

  def displayCoordinates(self):
    for shape in self.shapes:
      shape.displayCoordinates()

#NOTE: Angle metrics used is degrees for Rotate function  
print('Point:')
p1 = Point(2,2)
p1.Move(10,20)
p1.displayCoordinates()

print('\nLine:')
l1 = Line(0,0,4,0)
l1.Rotate(90)
l1.displayCoordinates()

print('\nCircle:')
c1 = Circle(2,2,4)
c1.Rotate(90)
c1.displayCoordinates()

print('\nAggregation:')
b=Aggregation(p1, l1, c1, Line(3,3,4,4))
b.Rotate(30)
b.Move(10,20)
b.displayCoordinates()