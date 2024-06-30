# TODO
from cs50 import get_float

coins = [0.25, 0.10, 0.05, 0.01]

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

count = 0
while change > 0:
    for coin in coins:
        if change >= coin:
            change = round(change - coin, 2)
            count += 1
            break

print(count)
