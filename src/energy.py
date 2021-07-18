from graphics import *
from button import Button

class Energy:
	def __init__(self):
		self.win = GraphWin("Energia", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Energia").draw(self.win)

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

		self.from_J_button = Button(self.win, Point(125, 80), 50, 22, "J")
		self.from_ft_lbf_button = Button(self.win, Point(125, 120), 50, 22, "ft*lb-f")
		self.from_Btu_button = Button(self.win, Point(125, 160), 50, 22, "Btu")
		self.from_cal_button = Button(self.win, Point(125, 200), 50, 22, "cal")

		self.to_J_button = Button(self.win, Point(375, 80), 50, 22, "J")
		self.to_ft_lbf_button = Button(self.win, Point(375, 120), 50, 22, "ft*lb-f")
		self.to_Btu_button = Button(self.win, Point(375, 160), 50, 22, "Btu")
		self.to_cal_button = Button(self.win, Point(375, 200), 50, 22, "cal")

		self.from_J_button.activate()
		self.from_ft_lbf_button.activate()
		self.from_Btu_button.activate()
		self.from_cal_button.activate()
		self.to_J_button.activate()
		self.to_ft_lbf_button.activate()
		self.to_Btu_button.activate()
		self.to_cal_button.activate()

		self.from_buttons = [self.from_J_button, self.from_ft_lbf_button, self.from_Btu_button, self.from_cal_button]
		self.to_buttons = [self.to_J_button, self.to_ft_lbf_button, self.to_Btu_button, self.to_cal_button]

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
		if chosen_buttons[0] == self.from_J_button:
			if chosen_buttons[1] == self.to_ft_lbf_button:
				new_value = self.J_to_ft_lbf()
			elif chosen_buttons[1] == self.to_Btu_button:
				new_value = self.J_to_Btu()
			elif chosen_buttons[1] == self.to_cal_button:
				new_value = self.J_to_cal()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_ft_lbf_button:
			if chosen_buttons[1] == self.to_J_button:
				new_value = self.ft_lbf_to_J()
			elif chosen_buttons[1] == self.to_Btu_button:
				new_value = self.ft_lbf_to_Btu()
			elif chosen_buttons[1] == self.to_cal_button:
				new_value = self.ft_lbf_to_cal()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_Btu_button:
			if chosen_buttons[1] == self.to_J_button:
				new_value = self.Btu_to_J()
			elif chosen_buttons[1] == self.to_ft_lbf_button:
				new_value = self.Btu_to_ft_lbf()
			elif chosen_buttons[1] == self.to_cal_button:
				new_value = self.Btu_to_cal()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_cal_button:
			if chosen_buttons[1] == self.to_J_button:
				new_value = self.cal_to_J()
			elif chosen_buttons[1] == self.to_Btu_button:
				new_value = self.cal_to_Btu()
			elif chosen_buttons[1] == self.to_ft_lbf_button:
				new_value = self.cal_to_ft_lbf()

		return new_value

	def J_to_ft_lbf(self):	
		value = self.get_value()
		new_value = value / 1.356
		return new_value

	def J_to_Btu(self):
		value = self.get_value()
		new_value = value / 1055
		return new_value

	def J_to_cal(self):
		value = self.get_value()
		new_value = value / 4.187
		return new_value

	def ft_lbf_to_J(self):
		value = self.get_value()
		new_value = value * 1.356
		return new_value

	def ft_lbf_to_Btu(self):
		value = self.get_value()
		new_value = value * 1.356 / 1055
		return new_value

	def ft_lbf_to_cal(self):
		value = self.get_value()
		new_value = value * 1.356 / 4.187
		return new_value

	def Btu_to_J(self):
		value = self.get_value()
		new_value = value * 1055
		return new_value

	def Btu_to_ft_lbf(self):
		value = self.get_value()
		new_value = value * 1055 / 1.356
		return new_value

	def Btu_to_cal(self):
		value = self.get_value()
		new_value = value * 1055 / 4.187
		return new_value

	def cal_to_J(self):
		value = self.get_value()
		new_value = value * 4.187
		return new_value

	def cal_to_ft_lbf(self):
		value = self.get_value()
		new_value = value * 4.187 / 1.356
		return new_value

	def cal_to_Btu(self):
		value = self.get_value()
		new_value = value * 4.187 / 1055
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)