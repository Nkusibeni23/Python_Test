import random

def is_correct_input(num):
    return num == '0' or num == '1'

def get_coin_side():
    return random.choice(['head', 'tail'])

def get_side_name(num):
    return 'head' if num == '0' else 'tail'

def view_side(user_bet):
    print("My bet is", get_side_name(user_bet))

def get_result(user_bet, coin_side):
    return 'win' if get_side_name(user_bet) == coin_side else 'lose'

def view_result(result):
    print(result)

def play():
    print("Start 'coin toss'")
    while True:
        user_bet = input("Input your bet\n0:head, 1:tail")
        if is_correct_input(user_bet):
            break
        print("Invalid input. Please enter 0 or 1.")
    
    view_side(user_bet)
    coin_side = get_coin_side()
    print("Coin is", coin_side)
    result = get_result(user_bet, coin_side)
    view_result(result)

play()
