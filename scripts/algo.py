##!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

def longest_subarray_less_k(k:int, pizzas: list):

	#Assuming pizzas to be a sorted list of ints

	best = -1
	window = []
	cur_sum = 0
	length = len(pizzas)

	#Parse the small-sliced pizzas first, then bigger ones
	indices = [x for x in range(len(pizzas))]
	cur_max = 0
	best_order = []
	for i in range(1,len(indices)+1):
		iterations = list(itertools.combinations(indices,i))
		for iteration in iterations:
			cur_slices = 0
			for index in iteration:
				cur_slices += pizzas[index]
			if cur_slices>k:
				continue
			elif cur_slices>cur_max:
				cur_max = cur_slices
				best_order = iteration
	return len(best_order),best_order


	#returns number of items in the window, and actual list of window
	return best, window



'''
#Test Ground
ret = longest_subarray_less_k(8, [1,2,3,4,5])
print(ret)
'''