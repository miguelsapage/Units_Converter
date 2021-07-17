from graphics import *
from button import Button

class Mass:
	def __init__(self):
		self.win = GraphWin("Massa", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Massa").draw(self.win)

		self.value = Entry(Point(250, 110), 10).draw(self.win)

		result_bracket = Rectangle(Point(200, 180), Point(300, 200))
		result_bracket.setFill("white")
		result_bracket.draw(self.win)

		Image(Point(250, 150), "img/down_arrow.png").draw(self.win)

		self.convert_button = Button(self.win, Point(250, 260), 75, 22, "Converter")
		self.convert_button.activate()
		self.clean_button = Button(self.win, Point(250, 285), 75, 22, "Limpar")
		self.clean_button.activate()

		self.from_kg_button = Button(self.win, Point(125, 80), 40, 22, "kg")
		self.from_lb_button = Button(self.win, Point(125, 120), 40, 22, "lb")
		self.from_slug_button = Button(self.win, Point(125, 160), 40, 22, "slug")
		self.from_oz_button = Button(self.win, Point(125, 200), 40, 22, "oz")
		self.from_c_button = Button(self.win, Point(125, 240), 40, 22, "c")
		self.from_st_button = Button(self.win, Point(125, 280), 40, 22, "st")

		self.to_kg_button = Button(self.win, Point(375, 80), 40, 22, "kg")
		self.to_lb_button = Button(self.win, Point(375, 120), 40, 22, "lb")
		self.to_slug_button = Button(self.win, Point(375, 160), 40, 22, "slug")
		self.to_oz_button = Button(self.win, Point(375, 200), 40, 22, "oz")
		self.to_c_button = Button(self.win, Point(375, 240), 40, 22, "c")
		self.to_st_button = Button(self.win, Point(375, 280), 40, 22, "st")

		self.from_kg_button.activate()
		self.from_lb_button.activate()
		self.from_slug_button.activate()
		self.from_oz_button.activate()
		self.from_c_button.activate()
		self.from_st_button.activate()
		self.to_kg_button.activate()
		self.to_lb_button.activate()
		self.to_slug_button.activate()
		self.to_oz_button.activate()
		self.to_c_button.activate()
		self.to_st_button.activate()

		self.from_buttons = [self.from_kg_button, self.from_lb_button, self.from_slug_button, self.from_oz_button, self.from_c_button, self.from_st_button]
		self.to_buttons = [self.to_kg_button, self.to_lb_button, self.to_slug_button, self.to_oz_button, self.to_c_button, self.to_st_button]

	def get_value(self):
		return float(self.value.getText())

	def interact(self):
		while True:
			click = self.win.getMouse()
			if self.convert_button.clicked(click):
				return "convert_button"
			if self.clean_button.clicked(click):
				for button in self.from_buttons:
					button.activate()
				for button in self.to_buttons:
					button.activate()
				self.value.setText("")


	def choose_conversion(self):
		chosen_buttons = []

		from_click = self.win.getMouse()
		for button in self.from_buttons:
			if button.clicked(from_click):
				chosen_buttons.append(button)
				other_buttons = [x for x in self.from_buttons if x != button]
				for other_bt in other_buttons:
					other_bt.deactivate()

		to_click = self.win.getMouse()
		for button in self.to_buttons:
			if button.clicked(to_click):
				chosen_buttons.append(button)
				other_buttons = [x for x in self.to_buttons if x != button]
				for other_bt in other_buttons:
					other_bt.deactivate()

		return chosen_buttons

	def convert(self, chosen_buttons):
		if chosen_buttons[0] == self.from_kg_button:
			if chosen_buttons[1] == self.to_lb_button:
				new_value = self.kg_to_lb()
			elif chosen_buttons[1] == self.to_slug_button:
				new_value = self.kg_to_slug()
			elif chosen_buttons[1] == self.to_st_button:
				new_value = self.kg_to_st()
			elif chosen_buttons[1] == self.to_oz_button:
				new_value = self.kg_to_oz()
			elif chosen_buttons[1] == self.to_c_button:
				new_value = self.kg_to_c()
		elif chosen_buttons[0] == self.from_lb_button:
			if chosen_buttons[1] == self.to_kg_button:
				new_value = self.lb_to_kg()
			elif chosen_buttons[1] == self.to_slug_button:
				new_value = self.lb_to_slug()
			elif chosen_buttons[1] == self.to_st_button:
				new_value = self.lb_to_st()
			elif chosen_buttons[1] == self.to_oz_button:
				new_value = self.lb_to_oz()
			elif chosen_buttons[1] == self.to_c_button:
				new_value = self.lb_to_c()
		elif chosen_buttons[0] == self.from_slug_button:
			if chosen_buttons[1] == self.to_kg_button:
				new_value = self.slug_to_kg()
			elif chosen_buttons[1] == self.to_lb_button:
				new_value = self.slug_to_lb()
			elif chosen_buttons[1] == self.to_st_button:
				new_value = self.slug_to_st()
			elif chosen_buttons[1] == self.to_oz_button:
				new_value = self.slug_to_oz()
			elif chosen_buttons[1] == self.to_c_button:
				new_value = self.slug_to_c()
		elif chosen_buttons[0] == self.from_st_button:
			if chosen_buttons[1] == self.to_kg_button:
				new_value = self.st_to_kg()
			elif chosen_buttons[1] == self.to_slug_button:
				new_value = self.st_to_slug()
			elif chosen_buttons[1] == self.to_lb_button:
				new_value = self.st_to_lb()
			elif chosen_buttons[1] == self.to_oz_button:
				new_value = self.st_to_oz()
			elif chosen_buttons[1] == self.to_c_button:
				new_value = self.st_to_c()
		elif chosen_buttons[0] == self.from_oz_button:
			if chosen_buttons[1] == self.to_kg_button:
				new_value = self.oz_to_kg()
			elif chosen_buttons[1] == self.to_slug_button:
				new_value = self.oz_to_slug()
			elif chosen_buttons[1] == self.to_st_button:
				new_value = self.oz_to_st()
			elif chosen_buttons[1] == self.to_lb_button:
				new_value = self.oz_to_lb()
			elif chosen_buttons[1] == self.to_c_button:
				new_value = self.oz_to_c()
		elif chosen_buttons[0] == self.from_c_button:
			if chosen_buttons[1] == self.to_kg_button:
				new_value = self.c_to_kg()
			elif chosen_buttons[1] == self.to_slug_button:
				new_value = self.c_to_slug()
			elif chosen_buttons[1] == self.to_st_button:
				new_value = self.c_to_st()
			elif chosen_buttons[1] == self.to_oz_button:
				new_value = self.c_to_oz()
			elif chosen_buttons[1] == self.to_lb_button:
				new_value = self.c_to_lb()

		return new_value

	def kg_to_lb(self):	
		value = self.get_value()
		new_value = value / 0.45359237
		return new_value

	def kg_to_slug(self):
		value = self.get_value()
		new_value = value / 14.593903
		return new_value

	def kg_to_st(self):
		value = self.get_value()
		new_value = value / 6.35029318
		return new_value

	def kg_to_oz(self):
		value = self.get_value()
		new_value = value / 0.028349523125
		return new_value

	def kg_to_c(self):
		value = self.get_value()
		new_value = value / 0.0002
		return new_value

	def lb_to_kg(self):
		value = self.get_value()
		new_value = value * 0.45359237
		return new_value

	def lb_to_slug(self):
		value = self.get_value()
		new_value = value * 0.45359237 / 14.593903
		return new_value

	def lb_to_st(self):
		value = self.get_value()
		new_value = value * 0.45359237 / 6.35029318
		return new_value

	def lb_to_oz(self):
		value = self.get_value()
		new_value = value * 0.45359237 / 0.028349523125
		return new_value

	def lb_to_c(self):
		value = self.get_value()
		new_value = value * 0.45359237 / 0.0002
		return new_value

	def slug_to_kg(self):
		value = self.get_value()
		new_value = value * 14.593903
		return new_value

	def slug_to_lb(self):
		value = self.get_value()
		new_value = value * 14.593903 / 0.45359237
		return new_value

	def slug_to_st(self):
		value = self.get_value()
		new_value = value * 14.593903 / 6.35029318
		return new_value

	def slug_to_oz(self):
		value = self.get_value()
		new_value = value * 14.593903 / 0.028349523125
		return new_value

	def slug_to_c(self):
		value = self.get_value()
		new_value = value * 14.593903 / 0.0002
		return new_value

	def st_to_kg(self):
		value = self.get_value()
		new_value = value * 6.35029318
		return new_value

	def st_to_lb(self):
		value = self.get_value()
		new_value = value * 14
		return new_value

	def st_to_slug(self):
		value = self.get_value()
		new_value = value * 6.35029318 / 14.593903
		return new_value

	def st_to_oz(self):
		value = self.get_value()
		new_value = value * 6.35029318 / 0.028349523125
		return new_value

	def st_to_c(self):
		value = self.get_value()
		new_value = value * 6.35029318 / 0.0002
		return new_value

	def oz_to_kg(self):
		value = self.get_value()
		new_value = value * 0.028349523125
		return new_value

	def oz_to_lb(self):
		value = self.get_value()
		new_value = value / 16
		return new_value

	def oz_to_slug(self):
		value = self.get_value()
		new_value = value * 0.028349523125 / 14.593903
		return new_value

	def oz_to_st(self):
		value = self.get_value()
		new_value = value * 0.028349523125 / 6.35029318
		return new_value

	def oz_to_c(self):
		value = self.get_value()
		new_value = value * 0.028349523125 / 0.0002
		return new_value

	def c_to_kg(self):
		value = self.get_value()
		new_value = value * 0.0002
		return new_value

	def c_to_lb(self):
		value = self.get_value()
		new_value = value * 0.0002 / 0.45359237
		return new_value

	def c_to_slug(self):
		value = self.get_value()
		new_value = value * 0.0002 / 14.593903
		return new_value

	def c_to_st(self):
		value = self.get_value()
		new_value = value * 0.0002 / 6.35029318
		return new_value

	def c_to_oz(self):
		value = self.get_value()
		new_value = value * 0.0002 / 0.028349523125
		return new_value

	def present_result(self, result):
		result = Text(Point(250, 190), "%5f" % result)
		result.setSize(10)
		result.draw(self.win)