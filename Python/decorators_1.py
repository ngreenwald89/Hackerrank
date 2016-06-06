total_numbers = int(input())
raw_numbers = []
for inp in range(total_numbers):
    raw_numbers.append(input().strip())

def prefixes(func):
    def inner(args):
        cleaned = [arg[-10:] for arg in args]
        return func(cleaned)
    return inner

@prefixes
def sort_and_print(numbers):
    numbers = sorted(numbers)
    [print('+91 ' + str(num[:5]) + ' ' + str(num[5:])) for num in numbers]

sort_and_print(raw_numbers)