from graphics import *
from button import Button

class Power:
	def __init__(self):
		self.win = GraphWin("Potência", 500, 350)
		Text(Point(250, 30), "Conversor de Unidades de Potência").draw(self.win)

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

		self.from_W_button = Button(self.win, Point(125, 80), 50, 22, "W")
		self.from_bhp_button = Button(self.win, Point(125, 120), 50, 22, "bhp")
		self.from_cv_button = Button(self.win, Point(125, 160), 50, 22, "cv")
		self.from_kcal_h_button = Button(self.win, Point(125, 200), 50, 22, "kcal/h")

		self.to_W_button = Button(self.win, Point(375, 80), 50, 22, "W")
		self.to_bhp_button = Button(self.win, Point(375, 120), 50, 22, "bhp")
		self.to_cv_button = Button(self.win, Point(375, 160), 50, 22, "cv")
		self.to_kcal_h_button = Button(self.win, Point(375, 200), 50, 22, "kcal/h")

		self.from_W_button.activate()
		self.from_bhp_button.activate()
		self.from_cv_button.activate()
		self.from_kcal_h_button.activate()
		self.to_W_button.activate()
		self.to_bhp_button.activate()
		self.to_cv_button.activate()
		self.to_kcal_h_button.activate()

		self.from_buttons = [self.from_W_button, self.from_bhp_button, self.from_cv_button, self.from_kcal_h_button]
		self.to_buttons = [self.to_W_button, self.to_bhp_button, self.to_cv_button, self.to_kcal_h_button]

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
		if chosen_buttons[0] == self.from_W_button:
			if chosen_buttons[1] == self.to_bhp_button:
				new_value = self.W_to_bhp()
			elif chosen_buttons[1] == self.to_cv_button:
				new_value = self.W_to_cv()
			elif chosen_buttons[1] == self.to_kcal_h_button:
				new_value = self.W_to_kcal_h()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_bhp_button:
			if chosen_buttons[1] == self.to_W_button:
				new_value = self.bhp_to_W()
			elif chosen_buttons[1] == self.to_cv_button:
				new_value = self.bhp_to_cv()
			elif chosen_buttons[1] == self.to_kcal_h_button:
				new_value = self.bhp_to_kcal_h()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_cv_button:
			if chosen_buttons[1] == self.to_W_button:
				new_value = self.cv_to_W()
			elif chosen_buttons[1] == self.to_bhp_button:
				new_value = self.cv_to_bhp()
			elif chosen_buttons[1] == self.to_kcal_h_button:
				new_value = self.cv_to_kcal_h()
			else:
				new_value = self.get_value()
		elif chosen_buttons[0] == self.from_kcal_h_button:
			if chosen_buttons[1] == self.to_W_button:
				new_value = self.kcal_h_to_W()
			elif chosen_buttons[1] == self.to_cv_button:
				new_value = self.kcal_h_to_cv()
			elif chosen_buttons[1] == self.to_bhp_button:
				new_value = self.kcal_h_to_bhp()
			else:
				new_value = self.get_value()

		return new_value

	def W_to_bhp(self):	
		value = self.get_value()
		new_value = value / 745.7
		return new_value

	def W_to_cv(self):
		value = self.get_value()
		new_value = value / 735
		return new_value

	def W_to_kcal_h(self):
		value = self.get_value()
		new_value = value / 0.8598
		return new_value

	def bhp_to_W(self):
		value = self.get_value()
		new_value = value * 745.7
		return new_value

	def bhp_to_cv(self):
		value = self.get_value()
		new_value = value * 745.7 / 735
		return new_value

	def bhp_to_kcal_h(self):
		value = self.get_value()
		new_value = value * 745.7 / 0.8598
		return new_value

	def cv_to_W(self):
		value = self.get_value()
		new_value = value * 735
		return new_value

	def cv_to_bhp(self):
		value = self.get_value()
		new_value = value * 735 / 745.7
		return new_value

	def cv_to_kcal_h(self):
		value = self.get_value()
		new_value = value * 735 / 0.8598
		return new_value

	def kcal_h_to_W(self):
		value = self.get_value()
		new_value = value * 0.8598
		return new_value

	def kcal_h_to_bhp(self):
		value = self.get_value()
		new_value = value * 0.8598 / 745.7
		return new_value

	def kcal_h_to_cv(self):
		value = self.get_value()
		new_value = value * 0.8598 / 735
		return new_value

	def present_result(self, result):
		self.result = Text(Point(250, 190), "%.5f" % result)
		self.result.setSize(10)
		self.result.draw(self.win)