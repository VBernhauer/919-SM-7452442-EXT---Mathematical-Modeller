#!/usr/bin/python


######## PRINT LIST ##########################################
# The function "find_combinations" is an adaptation of recursion problem published in: 
# https://stackoverflow.com/questions/19984579/recursion-python-coins-combination-list
def find_combinations(n, coins):
    if n < 0:
        return []
    if n == 0:
         return [[]]
    all_changes = []

    for last_used_coin in coins:
        combos = find_combinations(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            all_changes.append(combo)

    return all_changes

# filter repeated combinations using the same coins out of the list of all combinations
def filter_repeated_combinations(n, coins):

	coin_combinations = find_combinations(n, coins)
	
	for coin_combination in coin_combinations:
		sorted_coin_combination = coin_combination.sort(reverse=True)
	
	unique_coin_combinations = []
	for coin_combination in coin_combinations:
		if coin_combination not in unique_coin_combinations:
			unique_coin_combinations.append(coin_combination)

	return unique_coin_combinations

# get total number of combination of coins
def get_unique_combinations(n, coins):

	unique_combinations = filter_repeated_combinations(n, coins)
	sum_unique_combinations = len(unique_combinations)

	return unique_combinations

######## ONLY COUNT ##########################################
# This problem has been solved here:
# https://github.com/Vitosh/AlgoTests/blob/master/wk7_Coins.py

def get_number_of_combinations(i, n, coins, number_of_coins):
	i = i + 1
	if n < 0 or (number_of_coins <= 0):
		return 0
	if n == 0: 
		return 1

	return get_number_of_combinations(i, n, coins, number_of_coins - 1) + get_number_of_combinations(i, n - coins[number_of_coins - 1], coins, number_of_coins)


######## RUN #################################################
only_count = True

n = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
number_of_coins = len(coins)

if only_count:
	i = 0
	print(get_number_of_combinations(i, n, coins, number_of_coins))
else:
	### works only for small numbers, memory problems ###
	print(get_unique_combinations(n, coins))