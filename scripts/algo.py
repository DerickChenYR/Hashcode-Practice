##!/usr/bin/env python
# -*- coding: utf-8 -*-



def longest_subarray_less_k(k:int, pizzas: list):

	#Assuming pizzas to be a sorted list of ints

	best = -1
	window = []
	cur_sum = 0
	length = len(pizzas)

	#Parse the small-sliced pizzas first, then bigger ones
	for i in range(length):

		new_pizza = pizzas[i]
		

		#Current sum exceeds target value, going further down the list would result in a less optimal output
		if cur_sum + new_pizza > k:
			continue

		else:
			window.append(new_pizza)
			cur_sum += new_pizza
			best = max(best, len(window))



	return best



'''
#Test Ground
ret = longest_subarray_less_k(8, [1,2,3,4,5])
print(ret)
'''