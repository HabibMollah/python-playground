import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    reader = list(reader)[::-1]
    previous_cases = {}
    new_cases = {}

    # create initial previous_case dict with cumulative cases
    for i in range(len(reader)):
        state = reader[i]["state"]
        cases = int(reader[i]["cases"])
        if state not in previous_cases:
            previous_cases[state] = []
        if len(previous_cases[state]) < 15:
            previous_cases[state].insert(0, cases)

    # update previous_case dict with daily cases
    for state in previous_cases:
        daily_cases = []
        for i in range(len(previous_cases[state])):
            if i > 0:
                daily_cases.append(
                    previous_cases[state][i] - previous_cases[state][i - 1]
                )
            else:
                daily_cases.append(previous_cases[state][i])
        previous_cases[state] = daily_cases

    # iterate over previous_cases dict and update the new_cases dict with the last 14 items from the values
    for state in previous_cases:
        if len(previous_cases[state]) > 14:
            new_cases[state] = previous_cases[state][-14:]
        else:
            new_cases[state] = previous_cases[state]
    return new_cases


# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    for state in states:
        cases = new_cases[state]
        previous_week_avrg = sum(cases[:7]) / 7
        last_week_avrg = sum(cases[7:]) / 7
        change_percentage = (
            (last_week_avrg - previous_week_avrg) / previous_week_avrg
        ) * 100
        if change_percentage < 0:
            print(
                f"{state} had a 7-day average of {int(last_week_avrg)} and a decrease of {abs(int(change_percentage))}%."
            )
        if change_percentage >= 0:
            print(
                f"{state} had a 7-day average of {int(last_week_avrg)} and an increase of {int(change_percentage)}%."
            )


main()
