from cs50 import get_int

scores = []

iteration = get_int("How many numbers do you want to average: ")

for i in range(iteration):
    scores.append(get_int(f"Enter number {i + 1}: "))

print(f"Average: {sum(scores) / len(scores)}")
