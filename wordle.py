import requests
from datetime import *

baseLink = "https://www.nytimes.com/svc/wordle/v2/{}.json"
solutions = {}

def printTable(solutions):
    maxLenDates = len(max(list(solutions.keys()) + ["Date"], key=len)) + 2
    maxLenSolutions = len(max(list(solutions.values()) + ["Solution"], key=len)) + 2

    print('+' + '-' * (maxLenDates + 1) + '+' + '-' * (maxLenSolutions + 1) + '+')
    print('| ' + "Date" + ' ' * (maxLenDates - len("Date")) + '| ' + "Solution" + ' ' * (maxLenSolutions - len("Solution")) + '|')
    print('+' + '=' * (maxLenDates + 1) + '+' + '=' * (maxLenSolutions + 1) + '+')
    for date, solution in solutions.items():
        print('| ' + date + ' ' * (maxLenDates - len(date)) + '| ' + solution + ' ' * (maxLenSolutions - len(solution)) + '|')
    print('+' + '-' * (maxLenDates + 1) + '+' + '-' * (maxLenSolutions + 1) + '+')

def main():
    numberOfDays = int(input("Enter the number days you want to get the answers for : "))
    numberOfDays = min(numberOfDays, 5)

    for i in range(numberOfDays):
        day = (date.today() + timedelta(days = i)).strftime("%Y-%m-%d")
        link = baseLink.format(day)
        res = requests.get(link).json()
        solutions[res["print_date"]] = res["solution"]

    printTable(solutions)

if __name__ == "__main__":
    main()