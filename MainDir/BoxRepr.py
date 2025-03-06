from manim import *
import json

class SolutionSample(ThreeDScene):

    def setFill(self, objects):
        for item in objects:
            random = random_bright_color()
            item.set_fill(random, opacity=5)
            item.set_stroke(BLACK, width=4)

    def createMobject(self, items):
        mobjects = []
        for item in items:
            dimensions, target = item
            x, y, z = dimensions
            t_x, t_y, t_z = target
            mobject = Prism(dimensions=(float(x), float(y), float(z))).move_to((float(t_x), float(t_y), float(t_z)))
            mobjects.append(mobject)

        return mobjects

    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=150 * DEGREES)

        Box = Prism(dimensions=(14, 3, 3)).move_to((0, 0, 0))
        Box.set_fill(opacity=0)
        Box.set_stroke(BLUE, width=1)

        objects = self.createMobject(items)

        self.setFill(objects)
        self.play(
            Create(Box, run_time=5),
            Succession(
                Wait(2),
                *[Add(item, run_time=1) for item in objects],
                rate_func=smooth,
            )
        )
        Wait(2)


def getItems():
    objects = []
    with open("Data/BoxTestData.json", "r") as file:
        data = json.load(file)
        for item in data:
            dimensions = item["dimensions"]
            target = item["target"]
            dimensions = tuple(dimensions.split(","))
            target = tuple(target.split(","))
            objects.append((dimensions, target))
        return  objects

items = getItems()
SolutionSample().render()

