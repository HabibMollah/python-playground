import sys
from cs50 import get_string

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <name>")
    sys.exit(1)

contacts = {
    "David": "123",
    "Carter": "456",
    "Molly": "789",
    "Carter": "3241",
    "John": "234",
}

# for key in contacts:
if sys.argv[1] in contacts:
    print(f"Found: {contacts[sys.argv[1]]}")
else:
    print("Not found")
