"""
:testcase_name composite
:source https://github.com/faif/python-patterns/blob/master/patterns/structural/composite.py
:description The composite pattern describes a group of objects that is treated the
same way as a single instance of the same type of object. The intent of
a composite is to "compose" objects into tree structures to represent
part-whole hierarchies. Implementing the composite pattern lets clients
treat individual objects and compositions uniformly.

The example implements a graphic class，which can be either an ellipse
or a composition of several graphics. Every graphic can be printed.
"""


class Graphic:
    def render(self):
        raise NotImplementedError("You should implement this.")


class CompositeGraphic(Graphic):
    def __init__(self):
        self.graphics = []

    def render(self):
        for graphic in self.graphics:
            graphic.render()

    def add(self, graphic):
        self.graphics.append(graphic)

    def remove(self, graphic):
        self.graphics.remove(graphic)


class Ellipse(Graphic):
    def __init__(self, name):
        self.name = name

    def render(self):
        print("Ellipse: {}".format(self.name))


if __name__ == '__main__':
    ellipse1 = Ellipse("1")
    ellipse2 = Ellipse("2")
    ellipse3 = Ellipse("3")
    ellipse4 = Ellipse("4")

    graphic1 = CompositeGraphic()
    graphic2 = CompositeGraphic()

    graphic1.add(ellipse1)
    graphic1.add(ellipse2)
    graphic1.add(ellipse3)
    graphic2.add(ellipse4)

    graphic = CompositeGraphic()

    graphic.add(graphic1)
    graphic.add(graphic2)

    graphic.render()
