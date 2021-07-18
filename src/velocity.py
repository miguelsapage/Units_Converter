from graphics import *
from button import Button

class Velocity(object):
	def __init__(self):
		self.win = GraphWin("Velocidade", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Velocidade").draw(self.win)

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

		self.from_ms_button = Button(self.win, Point(125, 80), 50, 22, "m/s")
		self.from_ft_min_button = Button(self.win, Point(125, 120), 50, 22, "ft/min")
		self.from_kmh_button = Button(self.win, Point(125, 160), 50, 22, "km/h")
		self.from_kt_button = Button(self.win, Point(125, 200), 50, 22, "kt")
		self.from_mph_button = Button(self.win, Point(125, 240), 50, 22, "mph")

		self.to_ms_button = Button(self.win, Point(375, 80), 50, 22, "m/s")
		self.to_ft_min_button = Button(self.win, Point(375, 120), 50, 22, "ft/min")
		self.to_kmh_button = Button(self.win, Point(375, 160), 50, 22, "km/h")
		self.to_kt_button = Button(self.win, Point(375, 200), 50, 22, "kt")
		self.to_mph_button = Button(self.win, Point(375, 240), 50, 22, "mph")

		self.from_ms_button.activate()
		self.from_ft_min_button.activate()
		self.from_kmh_button.activate()
		self.from_kt_button.activate()
		self.from_mph_button.activate()
		self.to_ms_button.activate()
		self.to_ft_min_button.activate()
		self.to_kmh_button.activate()
		self.to_kt_button.activate()
		self.to_mph_button.activate()

		self.from_buttons = [self.from_ms_button, self.from_ft_min_button, self.from_kmh_button, self.from_kt_button, self.from_mph_button]
		self.to_buttons = [self.to_ms_button, self.to_ft_min_button, self.to_kmh_button, self.to_kt_button, self.to_mph_button]

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
		if chosen_buttons[0] == self.from_ms_button:
			if chosen_buttons[1] == self.to_ft_min_button:
				new_value = self.ms_to_ft_min()
			elif chosen_buttons[1] == self.to_kmh_button:
				new_value = self.ms_to_kmh()
			elif chosen_buttons[1] == self.to_kt_button:
				new_value = self.ms_to_kt()
			elif chosen_buttons[1] == self.to_mph_button:
				new_value = self.ms_to_mph()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_ft_min_button:
			if chosen_buttons[1] == self.to_ms_button:
				new_value = self.ft_min_to_ms()
			elif chosen_buttons[1] == self.to_kmh_button:
				new_value = self.ft_min_to_kmh()
			elif chosen_buttons[1] == self.to_kt_button:
				new_value = self.ft_min_to_kt()
			elif chosen_buttons[1] == self.to_mph_button:
				new_value = self.ft_min_to_mph()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_kmh_button:
			if chosen_buttons[1] == self.to_ms_button:
				new_value = self.kmh_to_ms()
			elif chosen_buttons[1] == self.to_ft_min_button:
				new_value = self.kmh_to_ft_min()
			elif chosen_buttons[1] == self.to_kt_button:
				new_value = self.kmh_to_kt()
			elif chosen_buttons[1] == self.to_mph_button:
				new_value = self.kmh_to_mph()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_kt_button:
			if chosen_buttons[1] == self.to_ms_button:
				new_value = self.kt_to_ms()
			elif chosen_buttons[1] == self.to_kmh_button:
				new_value = self.kt_to_kmh()
			elif chosen_buttons[1] == self.to_ft_min_button:
				new_value = self.kt_to_ft_min()
			elif chosen_buttons[1] == self.to_mph_button:
				new_value = self.kt_to_mph()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_mph_button:
			if chosen_buttons[1] == self.to_ms_button:
				new_value = self.mph_to_ms()
			elif chosen_buttons[1] == self.to_kmh_button:
				new_value = self.mph_to_kmh()
			elif chosen_buttons[1] == self.to_kt_button:
				new_value = self.mph_to_kt()
			elif chosen_buttons[1] == self.to_ft_min_button:
				new_value = self.mph_to_ft_min()
			else:
				new_value = self.get_value()

		return new_value

	def ms_to_ft_min(self):	
		value = self.get_value()
		new_value = value / 0.00508
		return new_value

	def ms_to_kmh(self):
		value = self.get_value()
		new_value = value / 0.2778
		return new_value

	def ms_to_kt(self):
		value = self.get_value()
		new_value = value / 0.51444444444444
		return new_value

	def ms_to_mph(self):
		value = self.get_value()
		new_value = value / 0.447
		return new_value

	def ft_min_to_ms(self):
		value = self.get_value()
		new_value = value * 0.00508
		return new_value

	def ft_min_to_kmh(self):
		value = self.get_value()
		new_value = value * 0.00508 / 0.2778
		return new_value

	def ft_min_to_kt(self):
		value = self.get_value()
		new_value = value * 0.00508 / 0.51444444444444
		return new_value

	def ft_min_to_mph(self):
		value = self.get_value()
		new_value = value * 0.00508 / 0.447
		return new_value

	def kmh_to_ms(self):
		value = self.get_value()
		new_value = value * 0.2778
		return new_value

	def kmh_to_ft_min(self):
		value = self.get_value()
		new_value = value * 0.2778 / 0.00508
		return new_value

	def kmh_to_kt(self):
		value = self.get_value()
		new_value = value * 0.2778 / 0.51444444444444
		return new_value

	def kmh_to_mph(self):
		value = self.get_value()
		new_value = value * 0.2778 / 0.447
		return new_value

	def kt_to_ms(self):
		value = self.get_value()
		new_value = value * 0.51444444444444
		return new_value

	def kt_to_ft_min(self):
		value = self.get_value()
		new_value = value * 0.51444444444444 / 0.00508
		return new_value

	def kt_to_kmh(self):
		value = self.get_value()
		new_value = value * 0.51444444444444 / 0.2778
		return new_value

	def kt_to_mph(self):
		value = self.get_value()
		new_value = value * 0.51444444444444 / 0.447
		return new_value

	def mph_to_ms(self):
		value = self.get_value()
		new_value = value * 0.447
		return new_value

	def mph_to_ft_min(self):
		value = self.get_value()
		new_value = value * 0.447 / 0.00508
		return new_value

	def mph_to_kmh(self):
		value = self.get_value()
		new_value = value  * 0.447 / 0.2778
		return new_value

	def mph_to_kt(self):
		value = self.get_value()
		new_value = value * 0.447 / 0.51444444444444
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)