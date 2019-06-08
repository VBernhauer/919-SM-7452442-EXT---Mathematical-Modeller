#! /usr/bin/env python

def get_sums(n):

	k = 0
	sum_k = 0
	sum_sq_k = 0

	for _ in range(n):
		
		k = k + 1
		sum_k = sum_k + k
		
		sq_k = k ** 2
		sum_sq_k = sum_sq_k + sq_k

	sum_k_sq = sum_k ** 2

	print("sum of the squares of the first " + str(n) + " natural numbers is " + str(sum_sq_k))
	print("square of the sum of the first " + str(n) + " natural numbers is " + str(sum_k_sq))

get_sums(100)