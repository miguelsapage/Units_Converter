"""
Conversor de Unidades

Miguel Sapage - 96291
Desempenho - 2020/201
"""

from graphics import *
from button import Button

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

	win.getMouse()
	win.close()

main()