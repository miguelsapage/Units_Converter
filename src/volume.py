from graphics import *
from button import Button

class Volume:
	def __init__(self):
		self.win = GraphWin("Volume", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Volume").draw(self.win)

		self.value = Entry(Point(250, 110), 10).draw(self.win)

		result_bracket = Rectangle(Point(200, 180), Point(300, 200))
		result_bracket.setFill("white")
		result_bracket.draw(self.win)

		Image(Point(250, 150), "img/down_arrow.png").draw(self.win)

		self.convert_button = Button(self.win, Point(250, 260), 75, 22, "Converter")
		self.convert_button.activate()
		self.clean_button = Button(self.win, Point(250, 285), 75, 22, "Limpar")
		self.clean_button.activate()
		self.quit_button = Button(self.win, Point(465, 330), 45, 22, "Sair")
		self.quit_button.activate()

		self.from_L_button = Button(self.win, Point(125, 80), 40, 22, "L")
		self.from_gal_button = Button(self.win, Point(125, 120), 40, 22, "gal")
		self.from_fl_oz_button = Button(self.win, Point(125, 160), 40, 22, "fl oz")
		self.from_cup_button = Button(self.win, Point(125, 200), 40, 22, "cup")
		self.from_pint_button = Button(self.win, Point(125, 240), 40, 22, "pint")

		self.to_L_button = Button(self.win, Point(375, 80), 40, 22, "L")
		self.to_gal_button = Button(self.win, Point(375, 120), 40, 22, "gal")
		self.to_fl_oz_button = Button(self.win, Point(375, 160), 40, 22, "fl oz")
		self.to_cup_button = Button(self.win, Point(375, 200), 40, 22, "cup")
		self.to_pint_button = Button(self.win, Point(375, 240), 40, 22, "pint")

		self.from_L_button.activate()
		self.from_gal_button.activate()
		self.from_fl_oz_button.activate()
		self.from_cup_button.activate()
		self.from_pint_button.activate()
		self.to_L_button.activate()
		self.to_gal_button.activate()
		self.to_fl_oz_button.activate()
		self.to_cup_button.activate()
		self.to_pint_button.activate()

		self.from_buttons = [self.from_L_button, self.from_gal_button, self.from_fl_oz_button, self.from_cup_button, self.from_pint_button]
		self.to_buttons = [self.to_L_button, self.to_gal_button, self.to_fl_oz_button, self.to_cup_button, self.to_pint_button]

	def get_value(self):
		return float(self.value.getText())

	def interact(self):
		while True:
			click = self.win.getMouse()
			if self.convert_button.clicked(click):
				return "convert_button"
			elif self.clean_button.clicked(click):
				for button in self.from_buttons:
					button.activate()
				for button in self.to_buttons:
					button.activate()
				self.value.setText("")
				self.result.undraw()
				return "clear_button"
			elif self.quit_button.clicked(click):
				self.win.close()
				return "quit_button"

	def choose_conversion(self):
		chosen_buttons = []
		while True:
			click = self.win.getMouse()
			if any([x.clicked(click) for x in self.from_buttons]):
				for button in self.from_buttons:
					if button.clicked(click):
						chosen_buttons.append(button)
						other_buttons = [x for x in self.from_buttons if x != button]
						for other_bt in other_buttons:
							other_bt.deactivate()
			elif any([x.clicked(click) for x in self.to_buttons]):
				for button in self.to_buttons:
					if button.clicked(click):
						chosen_buttons.append(button)
						other_buttons = [x for x in self.to_buttons if x != button]
						for other_bt in other_buttons:
							other_bt.deactivate()
			elif self.quit_button.clicked(click):
				self.win.close()
				return None
			if len(chosen_buttons) == 2:
				break

		return chosen_buttons

	def convert(self, chosen_buttons):
		if chosen_buttons[0] == self.from_L_button:
			if chosen_buttons[1] == self.to_gal_button:
				new_value = self.L_to_gal()
			elif chosen_buttons[1] == self.to_fl_oz_button:
				new_value = self.L_to_fl_oz()
			elif chosen_buttons[1] == self.to_cup_button:
				new_value = self.L_to_cup()
			elif chosen_buttons[1] == self.to_pint_button:
				new_value = self.L_to_pint()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_gal_button:
			if chosen_buttons[1] == self.to_L_button:
				new_value = self.gal_to_L()
			elif chosen_buttons[1] == self.to_fl_oz_button:
				new_value = self.gal_to_fl_oz()
			elif chosen_buttons[1] == self.to_cup_button:
				new_value = self.gal_to_cup()
			elif chosen_buttons[1] == self.to_pint_button:
				new_value = self.gal_to_pint()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_fl_oz_button:
			if chosen_buttons[1] == self.to_L_button:
				new_value = self.fl_oz_to_L()
			elif chosen_buttons[1] == self.to_gal_button:
				new_value = self.fl_oz_to_gal()
			elif chosen_buttons[1] == self.to_cup_button:
				new_value = self.fl_oz_to_cup()
			elif chosen_buttons[1] == self.to_pint_button:
				new_value = self.fl_oz_to_pint()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_cup_button:
			if chosen_buttons[1] == self.to_L_button:
				new_value = self.cup_to_L()
			elif chosen_buttons[1] == self.to_fl_oz_button:
				new_value = self.cup_to_fl_oz()
			elif chosen_buttons[1] == self.to_gal_button:
				new_value = self.cup_to_gal()
			elif chosen_buttons[1] == self.to_pint_button:
				new_value = self.cup_to_pint()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_pint_button:
			if chosen_buttons[1] == self.to_L_button:
				new_value = self.pint_to_L()
			elif chosen_buttons[1] == self.to_fl_oz_button:
				new_value = self.pint_to_fl_oz()
			elif chosen_buttons[1] == self.to_cup_button:
				new_value = self.pint_to_cup()
			elif chosen_buttons[1] == self.to_gal_button:
				new_value = self.pint_to_gal()
			else:
				new_value = self.get_value()

		return new_value

	def L_to_gal(self):	
		value = self.get_value()
		new_value = value / 3.785411784
		return new_value

	def L_to_fl_oz(self):
		value = self.get_value()
		new_value = value / 0.473176473 * 16
		return new_value

	def L_to_cup(self):
		value = self.get_value()
		new_value = value / 0.24
		return new_value

	def L_to_pint(self):
		value = self.get_value()
		new_value = value / 0.473176473
		return new_value

	def gal_to_L(self):
		value = self.get_value()
		new_value = value * 3.785411784
		return new_value

	def gal_to_fl_oz(self):
		value = self.get_value()
		new_value = value * 128
		return new_value

	def gal_to_cup(self):
		value = self.get_value()
		new_value = value * 3.785411784 / 0.24
		return new_value

	def gal_to_pint(self):
		value = self.get_value()
		new_value = value * 8
		return new_value

	def fl_oz_to_L(self):
		value = self.get_value()
		new_value = value * 0.473176473 / 16
		return new_value

	def fl_oz_to_gal(self):
		value = self.get_value()
		new_value = value / 128
		return new_value

	def fl_oz_to_cup(self):
		value = self.get_value()
		new_value = value * 0.473176473 / 16 / 0.24
		return new_value

	def fl_oz_to_pint(self):
		value = self.get_value()
		new_value = value / 16
		return new_value

	def cup_to_L(self):
		value = self.get_value()
		new_value = value * 0.24
		return new_value

	def cup_to_gal(self):
		value = self.get_value()
		new_value = value * 0.24 / 3.785411784
		return new_value

	def cup_to_fl_oz(self):
		value = self.get_value()
		new_value = value * 0.24 / 0.473176473 * 16
		return new_value

	def cup_to_pint(self):
		value = self.get_value()
		new_value = value * 0.24 / 0.473176473
		return new_value

	def pint_to_L(self):
		value = self.get_value()
		new_value = value * 0.473176473
		return new_value

	def pint_to_gal(self):
		value = self.get_value()
		new_value = value / 8
		return new_value

	def pint_to_fl_oz(self):
		value = self.get_value()
		new_value = value  * 16
		return new_value

	def pint_to_cup(self):
		value = self.get_value()
		new_value = value * 0.473176473 / 0.24
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)