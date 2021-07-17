"""
Conversor de Unidades

Miguel Sapage - 96291
Desempenho - 2020/201
"""

from graphics import *
from button import Button
from mass import Mass
from volume import Volume
from temperature import Temperature
from pressure import Pressure
from energy import Energy

def execute_chosen_conversion(unit):
	chosen_buttons = unit.choose_conversion()
	while True:
		if chosen_buttons == None:
			break
		interaction = unit.interact()
		if interaction == "convert_button":
			new_value = unit.convert(chosen_buttons)
			result = unit.present_result(new_value)
		elif interaction == "clear_button":
			execute_chosen_conversion(unit)
			break
		elif interaction == "quit_button":
			break

def main():

	win = GraphWin("Conversor de Unidades", 500, 350)

	Text(Point(250, 30), "Conversor de Unidades").draw(win)
	text = Text(Point(250, 330), "Escolha as unidades que deseja converter")
	text.setSize(10)
	text.draw(win)
	mass_button = Button(win, Point(125, 80), 140, 22, "Massa")
	volume_button = Button(win, Point(375, 80), 140, 22, "Volume")
	temperature_button = Button(win, Point(125, 120), 140, 22, "Temperatura")
	pressure_button = Button(win, Point(375, 120), 140, 22, "Pressão")
	energy_button = Button(win, Point(125, 160), 140, 22, "Energia")
	force_button = Button(win, Point(375, 160), 140, 22, "Força")
	velocity_button = Button(win, Point(125, 200), 140, 22, "Velocidade")
	time_button = Button(win, Point(375, 200), 140, 22, "Tempo")
	power_button = Button(win, Point(125, 240), 140, 22, "Potência")
	lenght_button = Button(win, Point(375, 240), 140, 22, "Comprimento")
	ferquency_button = Button(win, Point(125, 280), 140, 22, "Ferquência")
	specific_mass_button = Button(win, Point(375, 280), 140, 22, "Massa Específica")
	quit_button = Button(win, Point(465, 330), 45, 22, "Sair")
	mass_button.activate()
	volume_button.activate()
	temperature_button.activate()
	pressure_button.activate()
	energy_button.activate()
	force_button.activate()
	velocity_button.activate()
	time_button.activate()
	power_button.activate()
	lenght_button.activate()
	ferquency_button.activate()
	specific_mass_button.activate()
	quit_button.activate()

	while True:
		click = win.getMouse()

		if mass_button.clicked(click):
			mass = Mass()
			execute_chosen_conversion(mass)
		elif volume_button.clicked(click):
			volume = Volume()
			execute_chosen_conversion(volume)
		elif temperature_button.clicked(click):
			temperature = Temperature()
			execute_chosen_conversion(temperature)
		elif pressure_button.clicked(click):
			pressure = Pressure()
			execute_chosen_conversion(pressure)
		elif energy_button.clicked(click):
			energy = Energy()
			execute_chosen_conversion(energy)
		elif force_button.clicked(click):
			continue
		elif velocity_button.clicked(click):
			continue
		elif time_button.clicked(click):
			continue
		elif power_button.clicked(click):
			continue
		elif lenght_button.clicked(click):
			continue
		elif ferquency_button.clicked(click):
			continue
		elif specific_mass_button.clicked(click):
			continue
		elif quit_button.clicked(click):
			break

	win.close()

main()