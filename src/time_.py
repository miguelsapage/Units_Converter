from graphics import *
from button import Button

class Time:
	def __init__(self):
		self.win = GraphWin("Tempo", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Tempo").draw(self.win)

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

		self.from_s_button = Button(self.win, Point(125, 80), 50, 22, "s")
		self.from_min_button = Button(self.win, Point(125, 120), 50, 22, "min")
		self.from_h_button = Button(self.win, Point(125, 160), 50, 22, "h")
		self.from_days_button = Button(self.win, Point(125, 200), 50, 22, "dias")

		self.to_s_button = Button(self.win, Point(375, 80), 50, 22, "s")
		self.to_min_button = Button(self.win, Point(375, 120), 50, 22, "min")
		self.to_h_button = Button(self.win, Point(375, 160), 50, 22, "h")
		self.to_days_button = Button(self.win, Point(375, 200), 50, 22, "dias")

		self.from_s_button.activate()
		self.from_min_button.activate()
		self.from_h_button.activate()
		self.from_days_button.activate()
		self.to_s_button.activate()
		self.to_min_button.activate()
		self.to_h_button.activate()
		self.to_days_button.activate()

		self.from_buttons = [self.from_s_button, self.from_min_button, self.from_h_button, self.from_days_button]
		self.to_buttons = [self.to_s_button, self.to_min_button, self.to_h_button, self.to_days_button]

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
		if chosen_buttons[0] == self.from_s_button:
			if chosen_buttons[1] == self.to_min_button:
				new_value = self.s_to_min()
			elif chosen_buttons[1] == self.to_h_button:
				new_value = self.s_to_h()
			elif chosen_buttons[1] == self.to_days_button:
				new_value = self.s_to_days()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_min_button:
			if chosen_buttons[1] == self.to_s_button:
				new_value = self.min_to_s()
			elif chosen_buttons[1] == self.to_h_button:
				new_value = self.min_to_h()
			elif chosen_buttons[1] == self.to_days_button:
				new_value = self.min_to_days()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_h_button:
			if chosen_buttons[1] == self.to_s_button:
				new_value = self.h_to_s()
			elif chosen_buttons[1] == self.to_min_button:
				new_value = self.h_to_min()
			elif chosen_buttons[1] == self.to_days_button:
				new_value = self.h_to_days()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_days_button:
			if chosen_buttons[1] == self.to_s_button:
				new_value = self.days_to_s()
			elif chosen_buttons[1] == self.to_h_button:
				new_value = self.days_to_h()
			elif chosen_buttons[1] == self.to_min_button:
				new_value = self.days_to_min()
			else:
				new_value = self.get_value()

		return new_value

	def s_to_min(self):	
		value = self.get_value()
		new_value = value / 60
		return new_value

	def s_to_h(self):
		value = self.get_value()
		new_value = value / 3600
		return new_value

	def s_to_days(self):
		value = self.get_value()
		new_value = value / 3600 / 24
		return new_value

	def min_to_s(self):
		value = self.get_value()
		new_value = value * 60
		return new_value

	def min_to_h(self):
		value = self.get_value()
		new_value = value / 60
		return new_value

	def min_to_days(self):
		value = self.get_value()
		new_value = value / 60 / 24
		return new_value

	def h_to_s(self):
		value = self.get_value()
		new_value = value * 3600
		return new_value

	def h_to_min(self):
		value = self.get_value()
		new_value = value * 60
		return new_value

	def h_to_days(self):
		value = self.get_value()
		new_value = value / 24
		return new_value

	def days_to_s(self):
		value = self.get_value()
		new_value = value * 3600 * 24
		return new_value

	def days_to_min(self):
		value = self.get_value()
		new_value = value * 60 * 24
		return new_value

	def days_to_h(self):
		value = self.get_value()
		new_value = value * 24
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)