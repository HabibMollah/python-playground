from cs50 import get_string

greeting = get_string("Greeting: ").lower().lstrip()
start = ""

for i in range(len(greeting)):
    if i > 4:
        break
    start += greeting[i]

if start == "hello":
    print("$0")
elif start[0] == "h":
    print("$20")
else:
    print("$100")
