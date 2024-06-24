def main():
    height = get_height()

    for i in range(height):
        print("#" * (i + 1))


def get_height():
    while True:
        try:
            height = int(input("Enter height: "))
            if height > 0:
                return height
        except ValueError:
            print("Not an integer")


main()
