from collections import namedtuple
import random


class Stone:

    def __init__(self, weight=1):
        self.weight = weight
        self.chaos = random.randint(0, 100)


def make_stones():
    stones = []
    for i in range(8):
        stones.append(Stone())
    stones.append(Stone(1.5))
    stones.sort(key=lambda x: x.chaos)
    return stones


def balance(left_side, right_side):
    left_side_weight, right_side_weight = 0, 0
    for stone in left_side:
        left_side_weight += stone.weight

    for stone in right_side:
        right_side_weight += stone.weight

    if left_side_weight == right_side_weight:
        print('The left side is equal to the right side!')
        return ''
    elif left_side_weight > right_side_weight:
        print('The left side is heavier. The stone must be there!')
        return left_side
    else:
        print('The right side is heavier. The stone must be there!')
        return right_side


def select_stones(stones):
    print('Select the stones to weigh on the left. Enter each number'
          ' seperated by a space')
    valid_choices = False
    while (not valid_choices):
        s = ''
        for stone in stones:
            s += str(stones.index(stone)) + ' '
        left_input = input(s + '\n')
        left_input = left_input.split(' ')
        valid_choices = validate_stone_choice(left_input, len(stones))
    left_stones = []
    for choice in left_input:
        left_stones.append(stones[int(choice)])

    print('Select the stones to weigh on the right. Enter each number'
          ' seperated by a space')
    remaining_stones = [x for x in stones if x not in left_stones]
    valid_choices = False
    while (not valid_choices):
        s = ''
        for stone in remaining_stones:
            s += str(stones.index(stone)) + ' '
        right_input = input(s + '\n')
        right_input = right_input.split(' ')
        valid_choices = validate_stone_choice(right_input, len(stones))
        for choice in right_input:
            if choice in left_input:
                valid_choices = False
                print("You can weigh a stone twice!")
    right_stones = []
    for choice in right_input:
        right_stones.append(stones[int(choice)])

    remaining_stones = [x for x in stones if x not in left_stones
                        and x not in right_stones]

    Stones = namedtuple('Stones', 'l_side, r_side, remaining')
    selected_stones = Stones(left_stones, right_stones, remaining_stones)

    return selected_stones


def validate_stone_choice(choices, length):
    for choice in choices:
        if choice.isdigit():
            if int(choice) < length:
                return True
    print('Invalid choice')
    return False


def keep_stones(stones):
    '''used to reset the index of each stone'''
    return [x for x in stones]


def game_builder():
    stones = make_stones()
    print(intro)

    weigh_ins = 0
    while (weigh_ins < 2):
        sel_stones = select_stones(stones)
        balance_results = balance(sel_stones.l_side, sel_stones.r_side)
        if (balance_results):
            stones = keep_stones(balance_results)
        else:
            stones = sel_stones.remaining

        if len(stones) == 1 and weigh_ins < 2 and stones[0].weight == 1.5:
            print("You got lucky, but you didn't solve the puzzle correctly!")
            break
        weigh_ins += 1

    if len(stones) == 1 and stones[0].weight == 1.5:
        print('Congratulations. You are correct')
    else:
        print('Sorry, you are incorrect')


'''Dialog'''
intro = 'You are presented with nine stones, all of which appear identical, ' \
'although one weighs slightly more than the others because it contains a rare '\
'jewel. You are also given two balancing scales, though each may only be used '\
'once. Can you determine which stone contains the jewel?\n'

if __name__ == '__main__':
    game_builder()
