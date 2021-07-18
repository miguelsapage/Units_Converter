from graphics import *
from button import Button

class Length:
	def __init__(self):
		self.win = GraphWin("Comprimento", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Comprimento").draw(self.win)

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

		self.from_m_button = Button(self.win, Point(125, 80), 40, 22, "m")
		self.from_ft_button = Button(self.win, Point(125, 120), 40, 22, "ft")
		self.from_mile_button = Button(self.win, Point(125, 160), 40, 22, "mile")
		self.from_NM_button = Button(self.win, Point(125, 200), 40, 22, "NM")
		self.from_in_button = Button(self.win, Point(125, 240), 40, 22, "in")
		self.from_yd_button = Button(self.win, Point(125, 280), 40, 22, "yd")

		self.to_m_button = Button(self.win, Point(375, 80), 40, 22, "m")
		self.to_ft_button = Button(self.win, Point(375, 120), 40, 22, "ft")
		self.to_mile_button = Button(self.win, Point(375, 160), 40, 22, "mile")
		self.to_NM_button = Button(self.win, Point(375, 200), 40, 22, "NM")
		self.to_in_button = Button(self.win, Point(375, 240), 40, 22, "in")
		self.to_yd_button = Button(self.win, Point(375, 280), 40, 22, "yd")

		self.from_m_button.activate()
		self.from_ft_button.activate()
		self.from_mile_button.activate()
		self.from_NM_button.activate()
		self.from_in_button.activate()
		self.from_yd_button.activate()
		self.to_m_button.activate()
		self.to_ft_button.activate()
		self.to_mile_button.activate()
		self.to_NM_button.activate()
		self.to_in_button.activate()
		self.to_yd_button.activate()

		self.from_buttons = [self.from_m_button, self.from_ft_button, self.from_mile_button, self.from_NM_button, self.from_in_button, self.from_yd_button]
		self.to_buttons = [self.to_m_button, self.to_ft_button, self.to_mile_button, self.to_NM_button, self.to_in_button, self.to_yd_button]

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
		if chosen_buttons[0] == self.from_m_button:
			if chosen_buttons[1] == self.to_ft_button:
				new_value = self.m_to_ft()
			elif chosen_buttons[1] == self.to_mile_button:
				new_value = self.m_to_mile()
			elif chosen_buttons[1] == self.to_yd_button:
				new_value = self.m_to_yd()
			elif chosen_buttons[1] == self.to_NM_button:
				new_value = self.m_to_NM()
			elif chosen_buttons[1] == self.to_in_button:
				new_value = self.m_to_in()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_ft_button:
			if chosen_buttons[1] == self.to_m_button:
				new_value = self.ft_to_m()
			elif chosen_buttons[1] == self.to_mile_button:
				new_value = self.ft_to_mile()
			elif chosen_buttons[1] == self.to_yd_button:
				new_value = self.ft_to_yd()
			elif chosen_buttons[1] == self.to_NM_button:
				new_value = self.ft_to_NM()
			elif chosen_buttons[1] == self.to_in_button:
				new_value = self.ft_to_in()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_mile_button:
			if chosen_buttons[1] == self.to_m_button:
				new_value = self.mile_to_m()
			elif chosen_buttons[1] == self.to_ft_button:
				new_value = self.mile_to_ft()
			elif chosen_buttons[1] == self.to_yd_button:
				new_value = self.mile_to_yd()
			elif chosen_buttons[1] == self.to_NM_button:
				new_value = self.mile_to_NM()
			elif chosen_buttons[1] == self.to_in_button:
				new_value = self.mile_to_in()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_yd_button:
			if chosen_buttons[1] == self.to_m_button:
				new_value = self.yd_to_m()
			elif chosen_buttons[1] == self.to_mile_button:
				new_value = self.yd_to_mile()
			elif chosen_buttons[1] == self.to_ft_button:
				new_value = self.yd_to_ft()
			elif chosen_buttons[1] == self.to_NM_button:
				new_value = self.yd_to_NM()
			elif chosen_buttons[1] == self.to_in_button:
				new_value = self.yd_to_in()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_NM_button:
			if chosen_buttons[1] == self.to_m_button:
				new_value = self.NM_to_m()
			elif chosen_buttons[1] == self.to_mile_button:
				new_value = self.NM_to_mile()
			elif chosen_buttons[1] == self.to_yd_button:
				new_value = self.NM_to_yd()
			elif chosen_buttons[1] == self.to_ft_button:
				new_value = self.NM_to_ft()
			elif chosen_buttons[1] == self.to_in_button:
				new_value = self.NM_to_in()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_in_button:
			if chosen_buttons[1] == self.to_m_button:
				new_value = self.in_to_m()
			elif chosen_buttons[1] == self.to_mile_button:
				new_value = self.in_to_mile()
			elif chosen_buttons[1] == self.to_yd_button:
				new_value = self.in_to_yd()
			elif chosen_buttons[1] == self.to_NM_button:
				new_value = self.in_to_NM()
			elif chosen_buttons[1] == self.to_ft_button:
				new_value = self.in_to_ft()
			else:
				new_value = self.get_value()

		return new_value

	def m_to_ft(self):	
		value = self.get_value()
		new_value = value / 0.3048
		return new_value

	def m_to_mile(self):
		value = self.get_value()
		new_value = value / 1609
		return new_value

	def m_to_yd(self):
		value = self.get_value()
		new_value = value / 0.3048 / 3
		return new_value

	def m_to_NM(self):
		value = self.get_value()
		new_value = value / 0.3048 / 6076.1
		return new_value

	def m_to_in(self):
		value = self.get_value()
		new_value = value / 0.3048 * 12
		return new_value

	def ft_to_m(self):
		value = self.get_value()
		new_value = value * 0.3048
		return new_value

	def ft_to_mile(self):
		value = self.get_value()
		new_value = value * 0.3048 / 1609
		return new_value

	def ft_to_yd(self):
		value = self.get_value()
		new_value = value / 3
		return new_value

	def ft_to_NM(self):
		value = self.get_value()
		new_value = value / 6076.1
		return new_value

	def ft_to_in(self):
		value = self.get_value()
		new_value = value * 12
		return new_value

	def mile_to_m(self):
		value = self.get_value()
		new_value = value * 1609
		return new_value

	def mile_to_ft(self):
		value = self.get_value()
		new_value = value * 1609 / 0.3048
		return new_value

	def mile_to_yd(self):
		value = self.get_value()
		new_value = value * 1609 / 0.3048 / 3
		return new_value

	def mile_to_NM(self):
		value = self.get_value()
		new_value = value * 1609 / 0.3048 / 6076.1
		return new_value

	def mile_to_in(self):
		value = self.get_value()
		new_value = value * 1609 / 0.3048 * 12
		return new_value

	def yd_to_m(self):
		value = self.get_value()
		new_value = value * 3 * 0.3048
		return new_value

	def yd_to_ft(self):
		value = self.get_value()
		new_value = value * 3
		return new_value

	def yd_to_mile(self):
		value = self.get_value()
		new_value = value * 3 * 0.3048 / 1609
		return new_value

	def yd_to_NM(self):
		value = self.get_value()
		new_value = value * 3 / 6076.1
		return new_value

	def yd_to_in(self):
		value = self.get_value()
		new_value = value * 3 * 12
		return new_value

	def NM_to_m(self):
		value = self.get_value()
		new_value = value * 6076.1 * 0.3048
		return new_value

	def NM_to_ft(self):
		value = self.get_value()
		new_value = value * 6076.1
		return new_value

	def NM_to_mile(self):
		value = self.get_value()
		new_value = value * 6076.1 * 0.3048 / 1609
		return new_value

	def NM_to_yd(self):
		value = self.get_value()
		new_value = value * 6076.1 / 3
		return new_value

	def NM_to_in(self):
		value = self.get_value()
		new_value = value * 6076.1 * 12
		return new_value

	def in_to_m(self):
		value = self.get_value()
		new_value = value / 12 * 0.3048
		return new_value

	def in_to_ft(self):
		value = self.get_value()
		new_value = value / 12
		return new_value

	def in_to_mile(self):
		value = self.get_value()
		new_value = value / 12 * 0.3048 / 1609
		return new_value

	def in_to_yd(self):
		value = self.get_value()
		new_value = value / 36
		return new_value

	def in_to_NM(self):
		value = self.get_value()
		new_value = value / 12 / 6076.1
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)