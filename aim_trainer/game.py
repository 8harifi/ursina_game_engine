from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()


class Floor_Cube(Entity):
	def __init__(self, position):
		super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime,
        )


class Hostile(Button):
	def __init__(self, position):
		super().__init__(
			parent = scene,
			position = position,
			model = 'cube',
			color = color.red)
	def input(self, key):
		if self.hovered:
			if key == 'left mouse down':
				destroy(self)

def add_hostile():
	x = random.randint(1,20)
	z = random.randint(1,20)

	hostile = Hostile(position = (x, 0, z))


invoke(add_hostile, delay = 5)

for z in range(20):
	for x in range(20):
		floor_cube = Floor_Cube(position = (x-10,-20,z-10))




player = FirstPersonController()
app.run()

