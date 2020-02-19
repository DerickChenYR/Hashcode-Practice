#!/usr/bin/env python
# -*- coding: utf-8 -*-
from helper import parse_input
import sys

def main():
    filename = sys.argv[1]
    data = parse_input(filename)
    print(data)
main()