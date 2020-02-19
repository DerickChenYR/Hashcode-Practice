#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helper import parse_input,write_output
from algo import longest_subarray_less_k
import sys

def main():
    filename = sys.argv[1]
    data = parse_input(filename)
    num_pizzas, pizzas = longest_subarray_less_k(data["maximum_slices"],data["sizes"])
    write_output(num_pizzas,pizzas)
main()