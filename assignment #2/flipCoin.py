import sys
import random

probability_of_head = float(sys.argv[1])
probability_of_tail = 1 - float(probability_of_head)
coin_literals = ['head', 'tail']
flip_output_list = random.choices(coin_literals, weights=(probability_of_head, probability_of_tail), k=1)
result = flip_output_list[0]
if result == 'head':
    res = 1
else:
    res = 0
print(res)