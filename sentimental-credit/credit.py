# TODO
import re
from cs50 import get_string

pattern = r"^((34|37)\d{13}$|(51|52|53|54|55)\d{14}$|4\d{12}(\d{3})?$)"
card_initials = {
    "AMEX": ["34", "37"],
    "MASTERCARD": ["51", "52", "53", "54", "55"],
    "VISA": ["4"],
}


def main():
    card_num = get_string("Number: ").strip()
    result = re.match(pattern, card_num)

    if not result:
        print("INVALID")
        return

    else:
        for key in card_initials:
            for i in card_initials[key]:
                if card_num.startswith(i):
                    if checksum(card_num):
                        print(key)
                        return
                    print("INVALID")
                    return


def checksum(card_num):
    times_two = ""
    for i in range(len(card_num) - 2, -1, -2):
        times_two += str(int(card_num[i]) * 2)

    sum_of_digits = 0
    for i in times_two:
        sum_of_digits += int(i)

    final_sum = sum_of_digits
    for i in range(len(card_num) - 1, -1, -2):
        final_sum += int(card_num[i])

    return final_sum % 10 == 0


main()
