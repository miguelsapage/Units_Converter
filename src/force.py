from graphics import *
from button import Button

class Force:
	def __init__(self):
		self.win = GraphWin("Força", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Força").draw(self.win)

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

		self.from_N_button = Button(self.win, Point(125, 80), 40, 22, "N")
		self.from_lbf_button = Button(self.win, Point(125, 120), 40, 22, "lb-f")
		self.from_kgf_button = Button(self.win, Point(125, 160), 40, 22, "kg-f")
		self.from_dyne_button = Button(self.win, Point(125, 200), 40, 22, "dyne")

		self.to_N_button = Button(self.win, Point(375, 80), 40, 22, "N")
		self.to_lbf_button = Button(self.win, Point(375, 120), 40, 22, "lb-f")
		self.to_kgf_button = Button(self.win, Point(375, 160), 40, 22, "kg-f")
		self.to_dyne_button = Button(self.win, Point(375, 200), 40, 22, "dyne")

		self.from_N_button.activate()
		self.from_lbf_button.activate()
		self.from_kgf_button.activate()
		self.from_dyne_button.activate()
		self.to_N_button.activate()
		self.to_lbf_button.activate()
		self.to_kgf_button.activate()
		self.to_dyne_button.activate()

		self.from_buttons = [self.from_N_button, self.from_lbf_button, self.from_kgf_button, self.from_dyne_button]
		self.to_buttons = [self.to_N_button, self.to_lbf_button, self.to_kgf_button, self.to_dyne_button]

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
				try:
					self.result.undraw()
				except:
					pass
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
			elif self.clean_button.clicked(click):
				for button in self.from_buttons:
					button.activate()
				for button in self.to_buttons:
					button.activate()
				self.value.setText("")
				return "restart"
			if len(chosen_buttons) == 2:
				break

		return chosen_buttons

	def convert(self, chosen_buttons):
		if chosen_buttons[0] == self.from_N_button:
			if chosen_buttons[1] == self.to_lbf_button:
				new_value = self.N_to_lbf()
			elif chosen_buttons[1] == self.to_kgf_button:
				new_value = self.N_to_kgf()
			elif chosen_buttons[1] == self.to_dyne_button:
				new_value = self.N_to_dyne()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_lbf_button:
			if chosen_buttons[1] == self.to_N_button:
				new_value = self.lbf_to_N()
			elif chosen_buttons[1] == self.to_kgf_button:
				new_value = self.lbf_to_kgf()
			elif chosen_buttons[1] == self.to_dyne_button:
				new_value = self.lbf_to_dyne()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_kgf_button:
			if chosen_buttons[1] == self.to_N_button:
				new_value = self.kgf_to_N()
			elif chosen_buttons[1] == self.to_lbf_button:
				new_value = self.kgf_to_lbf()
			elif chosen_buttons[1] == self.to_dyne_button:
				new_value = self.kgf_to_dyne()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_dyne_button:
			if chosen_buttons[1] == self.to_N_button:
				new_value = self.dyne_to_N()
			elif chosen_buttons[1] == self.to_kgf_button:
				new_value = self.dyne_to_kgf()
			elif chosen_buttons[1] == self.to_lbf_button:
				new_value = self.dyne_to_lbf()
			else:
				new_value = self.get_value()

		return new_value

	def N_to_lbf(self):	
		value = self.get_value()
		new_value = value / 4.448221615
		return new_value

	def N_to_kgf(self):
		value = self.get_value()
		new_value = value / 9.80665
		return new_value

	def N_to_dyne(self):
		value = self.get_value()
		new_value = value / 0.0001
		return new_value

	def lbf_to_N(self):
		value = self.get_value()
		new_value = value * 4.448221615
		return new_value

	def lbf_to_kgf(self):
		value = self.get_value()
		new_value = value * 4.448221615 / 9.80665
		return new_value

	def lbf_to_dyne(self):
		value = self.get_value()
		new_value = value * 4.448221615 / 0.0001
		return new_value

	def kgf_to_N(self):
		value = self.get_value()
		new_value = value * 9.80665
		return new_value

	def kgf_to_lbf(self):
		value = self.get_value()
		new_value = value * 9.80665 / 4.448221615
		return new_value

	def kgf_to_dyne(self):
		value = self.get_value()
		new_value = value * 9.80665 / 0.0001
		return new_value

	def dyne_to_N(self):
		value = self.get_value()
		new_value = value * 0.0001
		return new_value

	def dyne_to_lbf(self):
		value = self.get_value()
		new_value = value * 0.0001 / 4.448221615
		return new_value

	def dyne_to_kgf(self):
		value = self.get_value()
		new_value = value * 0.0001 / 9.80665
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)