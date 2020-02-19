##!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_input(filename):
    with open(f'../input/{filename}') as f:
        lines = f.readlines()
        maximum_slices = int(lines[0].split()[0])
        num_types = int(lines[0].split()[1])
        sizes = [int(x) for x in lines[1].split()]
        sizes = sorted(sizes)
    return {"maximum_slices":maximum_slices,"num_types":num_types,"sizes":sizes}



#Write output for the project
def write_output(number_of_pizzas: int, pizza_types: list, filename: str):

	OUTPUT_DIR = "../output/"

	with open(OUTPUT_DIR + filename, "w") as file:

		file.write(str(number_of_pizzas) + "\n")
		for p in pizza_types:
			file.write(str(p) + " ")

	return True

