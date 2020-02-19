##!/usr/bin/env python
# -*- coding: utf-8 -*-




#Write output for the project
def write_output(number_of_pizzas: int, pizza_types: list):

	OUTPUT_DIR = "../output/"

	with open(OUTPUT_DIR + "output.txt", "w") as file:

		file.write(str(number_of_pizzas) + "\n")
		for p in pizza_types:
			file.write(str(p) + " ")

	return True


