import random

def coin_fliping(probability_of_tail):
    probability_of_head = 1 - float(probability_of_tail)
    coin_literals = ['head', 'tail']
    flip_output_list = random.choices(coin_literals, weights=(probability_of_head, probability_of_tail), k=1)
    result = flip_output_list[0]
    return result

def random_goalkeeper_direction_case(probability_of_head):
    taken = 0
    for i in range(0, 1000):
        if coin_fliping(probability_of_head) == "tail":
            shooter_desicion = "left"
        else:
            shooter_desicion = "right"
        
        if coin_fliping(probability_of_head) == "tail":
            goalkeeper_desicion = "left"
        else:
            goalkeeper_desicion = "right"
        
        if shooter_desicion == goalkeeper_desicion:
            taken += 1
    
    return taken

probability_of_tail = 0.7
print(f"goalkeeper managed to catch {random_goalkeeper_direction_case(probability_of_tail)} in random goalkeeper direction jump case.")