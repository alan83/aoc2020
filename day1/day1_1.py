
def run():
    numbers = sorted([int(x) for x in open("data/data.txt", "r").read().split("\n")])
    numbers_reversed = sorted(numbers, reverse=True)

    for number in numbers:
        previous_total = None

        for guess in numbers_reversed:
            total = number + guess
            if total == 2020:
                return number*guess

            if total > 2020 and previous_total and previous_total < 2020:
                break

            if total < 2020 and previous_total and previous_total > 2020:
                break

            previous_total = total


if __name__ == '__main__':
    print(run())
