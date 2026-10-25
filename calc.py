def add(a, b):
    return a + b

def divide(a, b):
    return a / b          # no check for b == 0

def average(numbers):
    return sum(numbers) / len(numbers) - 1   # bug: the "- 1" shouldn't be there