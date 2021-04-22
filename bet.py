import numpy as np
from itertools import permutations
from typing import List, Set, Tuple, Dict


def odds_to_probabilities(odds: List[float]):
	# NOTE: need to account for higher odds having larger differences?
	# print(odds)

	probs = list(map(lambda x: 1/x, odds))
	# print(probs)

	total_prob = sum(probs)

	# print(total_prob)

	edge = 1 / total_prob

	true_probs = list(map(lambda x: x * edge, probs))
	# print(true_probs)

	# print(1/total_prob)

	return true_probs, edge


def race_place_prob(place: int, probs: List[float], place_index: int):
	pass


def calc_matched_bet(stake, back_odds, lay_odds, commission, stake_returned=True):
	if stake_returned:
		return (stake * back_odds) / (lay_odds - commission)
	else:
		return (stake * (back_odds-1)) / (lay_odds - commission)





def race_order_probability(win_probs: List[float]):
	# assert sum(win_probs) == 1.0

	result_prob = 1.0
	total_prob = 1.0
	for prob in win_probs:
		result_prob *= (prob / total_prob)
		total_prob -= prob

	return result_prob


def race_place_conditions_probability(win_probs, conditions: List[Set[int]]):
	runner_win_probs = [(i, win_probs[i]) for i in range(len(win_probs))]

	condition_prob = 0.0
	total_prob = 0.0

	for perm in permutations(runner_win_probs):
		perm_prob = race_order_probability([x[1] for x in perm])

		total_prob += perm_prob
		cond_satisfied = True

		for i, p in enumerate(perm):
			runner, win_prob = p
			if conditions[runner] is not None:
				if i not in conditions[runner]:
					cond_satisfied = False
					break
		
		if cond_satisfied:
			condition_prob += perm_prob

	return condition_prob


		
				



odds = [8.5, 2.6, 18.0, 4.8, 26.0, 31.0, 6.5, 3.1]
print("Odds: ", odds)
probs, edge = odds_to_probabilities(odds)
print("Bookmaker Edge: ", 1-edge)
print("Win Probs: ", list(map(lambda x: round(x,3), probs)))

conditions = [None for _ in range(len(probs))]
conditions[1] = {0,1,2,3}
conditions[3] = {0,1,2,3}
conditions[7] = {0,1,2,3}

# place_conditions = {1: 4,
# 					3: 4,
# 					7: 4}
# rank_conditions = {}
cond_prob = race_place_conditions_probability(probs, conditions)
print("Cond prob: ", cond_prob)









# odds = [2, 16, 6, 14, 4.2, 4.8, 21]
# probs, edge = odds_to_probabilities(odds)





