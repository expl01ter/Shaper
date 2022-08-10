from turtle import *
from pifiglet import Figlet
import colorama
import time

f = Figlet(font='standard')

while True:
	print(Fore.VIOLET + f.renderText('SHAPER') + Style.RESET_ALL)
	print("Shaper V1.1")
	print(" ")
	s=input("Введите цвет лининий на английском языке: ")
	x=input("Введите цвет заливки на английском языке: ")
	print(" ")
	y=input("Введите толщину линий в пикселях: ")
	n=int(input("Введите количество сторон: "))
	f=int(input("Введите размер длин: "))
	print(" ")
	i=0
	width(y)
	color(s)
	begin_fill()
	while i<n:
		forward(f)
		left(360/n)
		i=i+1
	color(x)
	end_fill()
	print(" ")
	print(Fore.GREEN + "Finish!" + Style.RESET_ALL)
	exitonclick()
