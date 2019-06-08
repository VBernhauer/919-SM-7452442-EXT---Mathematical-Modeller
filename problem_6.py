#! /usr/bin/env python

#
# to run this script in the terminal:
# ./path/to/script/problem_6.py <integer>
#
# Example:
# ./path/to/script/problem_6.py 100 
# gives the result for the first one hundred natural numbers.
# 

import sys


n = int(sys.argv[1])

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