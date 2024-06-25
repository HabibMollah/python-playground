from cs50 import get_int


def draw(n):
    if n < 1:
        return
    draw(n - 1)
    print("#" * n)


height = get_int("Height for pyramid: ")
draw(height)
