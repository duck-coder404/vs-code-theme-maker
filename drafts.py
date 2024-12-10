import random

count = 0
trys = 7
options = ["tails", "heads"]


def wins_in_row(count, trys, options):
    last = options[random.randint(0, 1)]

    while True:
        curent = options[random.randint(0, 1)]
        if count == trys:
            break
        elif curent == last:
            count = count + 1
            winner = curent
        else:
            count = 1
        last = curent
    return winner

winner = wins_in_row(count, trys, options)

print(f"{winner} won {trys} times in a row")
