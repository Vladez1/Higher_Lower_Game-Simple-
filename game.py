import random
from game_data import data
from art import logo, vs
import methods

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {methods.format_data(account_a)}.")
    print(vs)
    print(f"Against B: {methods.format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess != "a" and guess != "b":
        guess = input("Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = methods.check_answer(guess, a_follower_count, b_follower_count)
    methods.clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
