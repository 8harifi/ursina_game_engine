from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()


window.title = 'aim trainer'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True



score = 0
class Floor_Cube(Button):
	def __init__(self, position):
		super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'white_cube',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
        )


class Hostile(Button):
	def __init__(self, position):
		super().__init__(
			parent = scene,
			position = position,
			model = 'sphere',
			origin_y = .5,
			color = color.red)

	def input(self, key):
		if self.hovered:
			if key == 'left mouse down':
				destroy(self)
				add_hostile()


def add_hostile():
	x1 = random.randint(1,19)
	y1 = random.randint(2,6)
	z1 = random.randint(1,19)

	hostile = Hostile(position = (x1-30, y1-2, z1-10))
	return hostile


for z in range(20):
	for x in range(20):
		floor_cube = Floor_Cube(position = (x-10,0,z-10))



for z in range(8):
	for x in range(8):
		floor_cube = Floor_Cube(position = (x-4,1,z-4))



for z in range(20):
	# floor_cube = Floor_Cube(position = (-10, 1, z-10))
	# floor_cube = Floor_Cube(position = (-10, 2, z-10))
	# floor_cube = Floor_Cube(position = (-10, 3, z-10))
	floor_cube = Floor_Cube(position = (10, 1, z-10))
	floor_cube = Floor_Cube(position = (10, 2, z-10))
	floor_cube = Floor_Cube(position = (10, 3, z-10))



for x in range(20):
	floor_cube = Floor_Cube(position = (x-10, 1, -10))
	floor_cube = Floor_Cube(position = (x-10, 2, -10))
	floor_cube = Floor_Cube(position = (x-10, 3, -10))
	floor_cube = Floor_Cube(position = (x-10, 1, 10))
	floor_cube = Floor_Cube(position = (x-10, 2, 10))
	floor_cube = Floor_Cube(position = (x-10, 3, 10))


def update():
	ammo = 30
	if held_keys['left mouse']:
		ammo -= 1
	text_score = Text(text = f"ammo: {ammo}", ignore=True, parent = camera.ui, origin = (-.5, .5))



hostile = add_hostile()


player = FirstPersonController()
app.run()

