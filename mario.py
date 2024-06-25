def main():
    height = get_int("Enter height: ")
    width = get_int("Enter width: ")

    for i in range(height):
        print("#" * width)


def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            print("Not an integer")


main()
