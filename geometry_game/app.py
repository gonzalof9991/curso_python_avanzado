from random import randint
import turtle

print("Hola Mundo")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Mis coordenadas son {self.y}"

    def falls_in_rectangle(self, rectangle):
        print(rectangle)
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point2.y < self.y < rectangle.point1.y:
            return True
        else:
            return False

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


# Extendemos la clase Rectangle para no modificar la clase
# Estamos hablando de herencia, Rectangle es padre de GuiRectangle
class GuiRectangle(Rectangle):

    def draw(self, canvas: turtle):
        canvas.penup()
        canvas.goto(self.point1.x, self.point1.y)
        canvas.pendown()
        # forward() -> es un metodo que sirve para avanzar
        canvas.forward(self.point2.x - self.point1.x)
        # left() -> ir a la izquiera
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)


class GuiPoint(Point):
    def draw(self, canvas: turtle, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


"""gui_rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400)))
my_turtle = turtle.Turtle()

gui_rectangle.draw(canvas=my_turtle)"""

"""point1 = Point(6, 7)
point2 = Point(2, 2)
rectanglex = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400)))
flag = point1.falls_in_rectangle(rectanglex)
resp = point1.distance_from_point(point2)
print(flag)
print(resp)"""

"Juego"
rectangle = GuiRectangle(
    Point(randint(0, 400), randint(0, 400)),
    Point(randint(10, 400), randint(10, 400)))

print("Rectangle Coordinates: ", rectangle.point1.x, ",", rectangle.point1.y, "and", rectangle.point2.x, ",",
      rectangle.point2.y)
user_point = GuiPoint(
    float(input("Guess X: ")),
    float(input("Guess Y: "))
)

user_area = float(input("Guess rectangle area: "))

print("Your point was inside rectangle ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)

myturtle = turtle.Turtle()
# Ocupamos la misma instancia de turtle para que ocupe el mismo lienzo y pueda marcar el punto sin perder el rectangulo
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
# Mantener ventana
turtle.done()
