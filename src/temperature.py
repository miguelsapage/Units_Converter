from graphics import *
from button import Button

class Temperature:
	def __init__(self):
		self.win = GraphWin("Temperatura", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Temperatura").draw(self.win)

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

		self.from_C_button = Button(self.win, Point(125, 80), 40, 22, "°C")
		self.from_F_button = Button(self.win, Point(125, 120), 40, 22, "°F")
		self.from_K_button = Button(self.win, Point(125, 160), 40, 22, "K")
		self.from_R_button = Button(self.win, Point(125, 200), 40, 22, "R")

		self.to_C_button = Button(self.win, Point(375, 80), 40, 22, "°C")
		self.to_F_button = Button(self.win, Point(375, 120), 40, 22, "°F")
		self.to_K_button = Button(self.win, Point(375, 160), 40, 22, "K")
		self.to_R_button = Button(self.win, Point(375, 200), 40, 22, "R")

		self.from_C_button.activate()
		self.from_F_button.activate()
		self.from_K_button.activate()
		self.from_R_button.activate()
		self.to_C_button.activate()
		self.to_F_button.activate()
		self.to_K_button.activate()
		self.to_R_button.activate()

		self.from_buttons = [self.from_C_button, self.from_F_button, self.from_K_button, self.from_R_button]
		self.to_buttons = [self.to_C_button, self.to_F_button, self.to_K_button, self.to_R_button]

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
		if chosen_buttons[0] == self.from_C_button:
			if chosen_buttons[1] == self.to_F_button:
				new_value = self.C_to_F()
			elif chosen_buttons[1] == self.to_K_button:
				new_value = self.C_to_K()
			elif chosen_buttons[1] == self.to_R_button:
				new_value = self.C_to_R()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_F_button:
			if chosen_buttons[1] == self.to_C_button:
				new_value = self.F_to_C()
			elif chosen_buttons[1] == self.to_K_button:
				new_value = self.F_to_K()
			elif chosen_buttons[1] == self.to_R_button:
				new_value = self.F_to_R()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_K_button:
			if chosen_buttons[1] == self.to_C_button:
				new_value = self.K_to_C()
			elif chosen_buttons[1] == self.to_F_button:
				new_value = self.K_to_F()
			elif chosen_buttons[1] == self.to_R_button:
				new_value = self.K_to_R()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_R_button:
			if chosen_buttons[1] == self.to_C_button:
				new_value = self.R_to_C()
			elif chosen_buttons[1] == self.to_K_button:
				new_value = self.R_to_K()
			elif chosen_buttons[1] == self.to_F_button:
				new_value = self.R_to_F()
			else:
				new_value = self.get_value()

		return new_value

	def C_to_F(self):	
		value = self.get_value()
		new_value = value * 1.8 + 32
		return new_value

	def C_to_K(self):
		value = self.get_value()
		new_value = value + 273.15
		return new_value

	def C_to_R(self):
		value = self.get_value()
		new_value = (value + 273.15) * 1.8
		return new_value

	def F_to_C(self):
		value = self.get_value()
		new_value = (value - 32) / 1.8
		return new_value

	def F_to_K(self):
		value = self.get_value()
		new_value = (value - 32) / 1.8 + 273.15
		return new_value

	def F_to_R(self):
		value = self.get_value()
		new_value = value + 459.67
		return new_value

	def K_to_C(self):
		value = self.get_value()
		new_value = value - 273.15
		return new_value

	def K_to_F(self):
		value = self.get_value()
		new_value = (value - 273.15) * 1.8 + 32
		return new_value

	def K_to_R(self):
		value = self.get_value()
		new_value = value * 1.8
		return new_value

	def R_to_C(self):
		value = self.get_value()
		new_value = value / 1.8 - 273.15
		return new_value

	def R_to_F(self):
		value = self.get_value()
		new_value = value - 459.67
		return new_value

	def R_to_K(self):
		value = self.get_value()
		new_value = value / 1.8
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.3f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)