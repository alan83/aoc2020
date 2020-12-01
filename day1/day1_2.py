import timeit


def run():
    numbers = sorted([int(x) for x in open("data/data.txt", "r").read().split("\n")])
    numbers_reversed = sorted(numbers, reverse=True)

    for number in numbers:
        part = calculate(2020-number, numbers, numbers_reversed)
        if part:
            result= part*number
            print(result)
            return result


def calculate(required_total, numbers, numbers_reversed):
    for number in numbers:
        previous_total = None

        for guess in numbers_reversed:
            total = number + guess
            if total == required_total:
                return number*guess

            if total > required_total and previous_total and previous_total < required_total:
                break

            if total < required_total and previous_total and previous_total > required_total:
                break

            previous_total = total

    return None


if __name__ == '__main__':
    print(timeit.timeit('run()', setup="from __main__ import run", number=100))
