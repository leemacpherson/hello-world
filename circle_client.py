from circle import *  # the ' * ' lets you access indentifiers in client program without prefixing with the module name

my_circle = Circle(5)  #we are intantiating the class Circle and passing an argument of '5' as the radius

print ("The radius of the circle is ", my_circle.radius)

print ("The area of the circle is ", format(my_circle.get_area(), ".3f"))

print ("The area formatted as an integer is ", format(int(my_circle.get_area()), "3d"))
