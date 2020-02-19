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




#DFS into the array use backtrack, terminate when current sum exceeds target
def combo_sum_backtrack(k:int, pizzas: list):

	ret = []
	max_type = -1	#make this a global var? So to reduce repetitions in the root recursive processes

	max_type, combinations = backtrack(0, pizzas, k, [], max_type, ret)
	
	max_points = -1
	best_choice = []
	for tup in combinations:
		if sum(tup) > max_points:
			max_points = sum(tup)
			best_choice = tup


	#Get the indices for the best choice of pizzas
	best_indices = []
	for i in best_choice:
		best_indices.append(pizzas.index(i))

	return max_type, best_indices

def backtrack(ind, pizzas, k, cur_list, best, ret):

	if sum(cur_list) == k:

		best = len(cur_list)
		#ret.append(tuple(cur_list))
		return best, cur_list

	elif sum(cur_list) > k:
		return -1, []

	#Case sublist sum less than k
	else:
		best = len(cur_list)
		for i in range(ind , len(pizzas), 1):

			cur_list.append(pizzas[i])
			
			new_best, new_ret = backtrack(i+1, pizzas, k, cur_list, best, ret)

			if new_best >= best:
				#print(f"new best is {new_best}, best is {best}")
				best = new_best
				ret.append(tuple(cur_list))

			cur_list.pop()

	return best, ret

	
#'''
#Test Ground
#ret = combo_sum_backtrack(17, [2, 5, 6, 8])
#print(ret)
#'''