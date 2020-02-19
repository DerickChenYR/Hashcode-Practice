##!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_input(filename):
    with open("filename") as f:
        lines = f.readlines()
        maximum_slices = lines[0].split()[0]
        num_types = lines[0].split()[1]
        sizes = lines[1].split()
    return maximum_slices,num_types,sizes