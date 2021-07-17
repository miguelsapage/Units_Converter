from graphics import *
from button import Button

class Pressure:
	def __init__(self):
		self.win = GraphWin("Pressão", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Pressão").draw(self.win)

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

		self.from_Pa_button = Button(self.win, Point(125, 80), 50, 22, "Pa")
		self.from_bar_button = Button(self.win, Point(125, 120), 50, 22, "bar")
		self.from_atm_button = Button(self.win, Point(125, 160), 50, 22, "atm")
		self.from_lbf_in2_button = Button(self.win, Point(125, 200), 50, 22, "lb-f/in²")
		self.from_in_Hg_button = Button(self.win, Point(125, 240), 50, 22, "in Hg")

		self.to_Pa_button = Button(self.win, Point(375, 80), 50, 22, "Pa")
		self.to_bar_button = Button(self.win, Point(375, 120), 50, 22, "bar")
		self.to_atm_button = Button(self.win, Point(375, 160), 50, 22, "atm")
		self.to_lbf_in2_button = Button(self.win, Point(375, 200), 50, 22, "lb-f/in²")
		self.to_in_Hg_button = Button(self.win, Point(375, 240), 50, 22, "in Hg")

		self.from_Pa_button.activate()
		self.from_bar_button.activate()
		self.from_atm_button.activate()
		self.from_lbf_in2_button.activate()
		self.from_in_Hg_button.activate()
		self.to_Pa_button.activate()
		self.to_bar_button.activate()
		self.to_atm_button.activate()
		self.to_lbf_in2_button.activate()
		self.to_in_Hg_button.activate()

		self.from_buttons = [self.from_Pa_button, self.from_bar_button, self.from_atm_button, self.from_lbf_in2_button, self.from_in_Hg_button]
		self.to_buttons = [self.to_Pa_button, self.to_bar_button, self.to_atm_button, self.to_lbf_in2_button, self.to_in_Hg_button]

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
		if chosen_buttons[0] == self.from_Pa_button:
			if chosen_buttons[1] == self.to_bar_button:
				new_value = self.Pa_to_bar()
			elif chosen_buttons[1] == self.to_atm_button:
				new_value = self.Pa_to_atm()
			elif chosen_buttons[1] == self.to_lbf_in2_button:
				new_value = self.Pa_to_lbf_in2()
			elif chosen_buttons[1] == self.to_in_Hg_button:
				new_value = self.Pa_to_in_Hg()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_bar_button:
			if chosen_buttons[1] == self.to_Pa_button:
				new_value = self.bar_to_Pa()
			elif chosen_buttons[1] == self.to_atm_button:
				new_value = self.bar_to_atm()
			elif chosen_buttons[1] == self.to_lbf_in2_button:
				new_value = self.bar_to_lbf_in2()
			elif chosen_buttons[1] == self.to_in_Hg_button:
				new_value = self.bar_to_in_Hg()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_atm_button:
			if chosen_buttons[1] == self.to_Pa_button:
				new_value = self.atm_to_Pa()
			elif chosen_buttons[1] == self.to_bar_button:
				new_value = self.atm_to_bar()
			elif chosen_buttons[1] == self.to_lbf_in2_button:
				new_value = self.atm_to_lbf_in2()
			elif chosen_buttons[1] == self.to_in_Hg_button:
				new_value = self.atm_to_in_Hg()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_lbf_in2_button:
			if chosen_buttons[1] == self.to_Pa_button:
				new_value = self.lbf_in2_to_Pa()
			elif chosen_buttons[1] == self.to_atm_button:
				new_value = self.lbf_in2_to_atm()
			elif chosen_buttons[1] == self.to_bar_button:
				new_value = self.lbf_in2_to_bar()
			elif chosen_buttons[1] == self.to_in_Hg_button:
				new_value = self.lbf_in2_to_in_Hg()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_in_Hg_button:
			if chosen_buttons[1] == self.to_Pa_button:
				new_value = self.in_Hg_to_Pa()
			elif chosen_buttons[1] == self.to_atm_button:
				new_value = self.in_Hg_to_atm()
			elif chosen_buttons[1] == self.to_lbf_in2_button:
				new_value = self.in_Hg_to_lbf_in2()
			elif chosen_buttons[1] == self.to_bar_button:
				new_value = self.in_Hg_to_bar()
			else:
				new_value = self.get_value()

		return new_value

	def Pa_to_bar(self):	
		value = self.get_value()
		new_value = value / 100000
		return new_value

	def Pa_to_atm(self):
		value = self.get_value()
		new_value = value / 101325
		return new_value

	def Pa_to_lbf_in2(self):
		value = self.get_value()
		new_value = value / 6895
		return new_value

	def Pa_to_in_Hg(self):
		value = self.get_value()
		new_value = value / 3386
		return new_value

	def bar_to_Pa(self):
		value = self.get_value()
		new_value = value * 100000
		return new_value

	def bar_to_atm(self):
		value = self.get_value()
		new_value = value * 100000 / 101325
		return new_value

	def bar_to_lbf_in2(self):
		value = self.get_value()
		new_value = value * 100000 / 6895
		return new_value

	def bar_to_in_Hg(self):
		value = self.get_value()
		new_value = value * 100000 / 3386
		return new_value

	def atm_to_Pa(self):
		value = self.get_value()
		new_value = value * 101325
		return new_value

	def atm_to_bar(self):
		value = self.get_value()
		new_value = value * 101325 / 100000
		return new_value

	def atm_to_lbf_in2(self):
		value = self.get_value()
		new_value = value * 101325 / 6895
		return new_value

	def atm_to_in_Hg(self):
		value = self.get_value()
		new_value = value * 101325 / 3386
		return new_value

	def lbf_in2_to_Pa(self):
		value = self.get_value()
		new_value = value * 6895
		return new_value

	def lbf_in2_to_bar(self):
		value = self.get_value()
		new_value = value * 6895 / 100000
		return new_value

	def lbf_in2_to_atm(self):
		value = self.get_value()
		new_value = value * 6895 / 101325
		return new_value

	def lbf_in2_to_in_Hg(self):
		value = self.get_value()
		new_value = value * 6895 / 3386
		return new_value

	def in_Hg_to_Pa(self):
		value = self.get_value()
		new_value = value * 3386
		return new_value

	def in_Hg_to_bar(self):
		value = self.get_value()
		new_value = value * 3386 / 100000
		return new_value

	def in_Hg_to_atm(self):
		value = self.get_value()
		new_value = value  * 3386 / 101325
		return new_value

	def in_Hg_to_lbf_in2(self):
		value = self.get_value()
		new_value = value * 3386 / 6895
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)