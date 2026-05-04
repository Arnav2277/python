import math
import random
import turtle

# ── Shape Classes ──────────────────────────────────────────────────────────────

class Shape:
    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    def describe(self):
        print(f"  {self.__class__.__name__}")
        print(f"    Area      : {self.area():.2f}")
        print(f"    Perimeter : {self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def fun_fact(self):
        return "A circle has infinite lines of symmetry!"

    def draw(self, t, x, y, color):
        t.penup()
        t.goto(x, y - self.radius)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def fun_fact(self):
        if self.is_square():
            return "This rectangle is actually a square — a very special rectangle!"
        return f"Aspect ratio is {self.width / self.height:.2f}:1"

    def draw(self, t, x, y, color):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(color)
        t.begin_fill()
        for _ in range(2):
            t.forward(self.width)
            t.left(90)
            t.forward(self.height)
            t.left(90)
        t.end_fill()


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("These sides don't form a valid triangle!")
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def kind(self):
        sides = sorted([self.a, self.b, self.c])
        if sides[0] == sides[2]:
            return "Equilateral"
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            return "Isosceles"
        else:
            return "Scalene"

    def fun_fact(self):
        return f"I'm a {self.kind()} triangle!"

    def draw(self, t, x, y, color):
        height = (math.sqrt(3) / 2) * self.a
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.goto(x + self.a, y)
        t.goto(x + self.a / 2, y + height)
        t.goto(x, y)
        t.end_fill()


class RegularPolygon(Shape):
    def __init__(self, sides, side_length):
        if sides < 3:
            raise ValueError("A polygon needs at least 3 sides!")
        self.sides = sides
        self.side_length = side_length

    def area(self):
        return (self.sides * self.side_length ** 2) / (4 * math.tan(math.pi / self.sides))

    def perimeter(self):
        return self.sides * self.side_length

    def interior_angle(self):
        return (self.sides - 2) * 180 / self.sides

    def fun_fact(self):
        return f"Each interior angle is {self.interior_angle():.1f}°"

    def draw(self, t, x, y, color):
        t.penup()
        t.goto(x, y)
        t.setheading(0)
        t.pendown()
        t.color(color)
        t.begin_fill()
        for _ in range(self.sides):
            t.forward(self.side_length)
            t.left(360 / self.sides)
        t.end_fill()


# ── Spiral Art ─────────────────────────────────────────────────────────────────

def draw_spiral(t, colors):
    print("\n✦ Drawing a rainbow spiral...")
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.width(2)
    size = 5
    for i in range(100):
        t.color(colors[i % len(colors)])
        t.forward(size)
        t.left(59)
        size += 3


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    COLORS = ["tomato", "gold", "mediumseagreen", "dodgerblue",
              "orchid", "coral", "turquoise", "hotpink"]

    shapes = [
        Circle(50),
        Rectangle(80, 120),
        Rectangle(70, 70),
        Triangle(60, 60, 60),
        Triangle(50, 80, 90),
        RegularPolygon(6, 50),
        RegularPolygon(8, 40),
    ]

    print("=" * 50)
    print("        FUN WITH SHAPES — Python Edition")
    print("=" * 50)

    for shape in shapes:
        shape.describe()
        if hasattr(shape, "fun_fact"):
            print(f"    Fun fact  : {shape.fun_fact()}")
        print()

    biggest = max(shapes, key=lambda s: s.area())
    print(f"Biggest shape by area: {biggest.__class__.__name__} "
          f"with area {biggest.area():.2f}")
    print("=" * 50)

    screen = turtle.Screen()
    screen.title("Fun with Shapes!")
    screen.bgcolor("#1a1a2e")
    screen.setup(width=900, height=650)

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    positions = [
        (-380, 150), (-230, 150), (-50, 150),
        (130, 150),  (310, 150),
        (-300, -50), (-100, -50), (100, -50), (300, -50),
    ]

    drawable = [s for s in shapes if hasattr(s, "draw")]
    for i, shape in enumerate(drawable):
        x, y = positions[i % len(positions)]
        shape.draw(t, x, y, COLORS[i % len(COLORS)])

    t.width(1)
    draw_spiral(t, COLORS)

    t.penup()
    t.goto(0, -280)
    t.color("white")
    t.write("Fun with Shapes — click to close", align="center",
            font=("Arial", 14, "bold"))

    print("\nTurtle window open — click it to close.")
    screen.exitonclick()


if __name__ == "__main__":
    main()