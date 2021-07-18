from graphics import *
from button import Button
from math import pi

class Frequency:
	def __init__(self):
		self.win = GraphWin("Frequência", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Frequência").draw(self.win)

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

		self.from_Hz_button = Button(self.win, Point(125, 80), 50, 22, "Hz")
		self.from_rad_s_button = Button(self.win, Point(125, 120), 50, 22, "rad/s")
		self.from_rpm_button = Button(self.win, Point(125, 160), 50, 22, "rpm")

		self.to_Hz_button = Button(self.win, Point(375, 80), 50, 22, "Hz")
		self.to_rad_s_button = Button(self.win, Point(375, 120), 50, 22, "rad/s")
		self.to_rpm_button = Button(self.win, Point(375, 160), 50, 22, "rpm")

		self.from_Hz_button.activate()
		self.from_rad_s_button.activate()
		self.from_rpm_button.activate()
		self.to_Hz_button.activate()
		self.to_rad_s_button.activate()
		self.to_rpm_button.activate()

		self.from_buttons = [self.from_Hz_button, self.from_rad_s_button, self.from_rpm_button]
		self.to_buttons = [self.to_Hz_button, self.to_rad_s_button, self.to_rpm_button]

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
		if chosen_buttons[0] == self.from_Hz_button:
			if chosen_buttons[1] == self.to_rad_s_button:
				new_value = self.Hz_to_rad_s()
			elif chosen_buttons[1] == self.to_rpm_button:
				new_value = self.Hz_to_rpm()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_rad_s_button:
			if chosen_buttons[1] == self.to_Hz_button:
				new_value = self.rad_s_to_Hz()
			elif chosen_buttons[1] == self.to_rpm_button:
				new_value = self.rad_s_to_rpm()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_rpm_button:
			if chosen_buttons[1] == self.to_Hz_button:
				new_value = self.rpm_to_Hz()
			elif chosen_buttons[1] == self.to_rad_s_button:
				new_value = self.rpm_to_rad_s()
			else:
				new_value = self.get_value()

		return new_value

	def Hz_to_rad_s(self):	
		value = self.get_value()
		new_value = value * 2*pi
		return new_value

	def Hz_to_rpm(self):
		value = self.get_value()
		new_value = value * 60
		return new_value

	def rad_s_to_Hz(self):
		value = self.get_value()
		new_value = value / 2*pi
		return new_value

	def rad_s_to_rpm(self):
		value = self.get_value()
		new_value = value / 2*pi * 60
		return new_value

	def rpm_to_Hz(self):
		value = self.get_value()
		new_value = value / 60
		return new_value

	def rpm_to_rad_s(self):
		value = self.get_value()
		new_value = value / 60 * 2*pi
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)