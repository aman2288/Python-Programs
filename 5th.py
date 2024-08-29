# 5.Define a function sum()and a function multiply()that sums and multiplies (respectively) all the numbers in a list of numbers. 
# Example :- sum([1, 2, 3, 4])should return 10, and multiply([1,2, 3, 4])should return 24.

def calc_sum():
    list = [1, 2, 3, 4,5]
    sum = 0
    for number in list:
        sum += number
    return sum


def calc_multiply():
    list = [1, 2, 3, 4]
    multiply = 1
    for number in list:
        multiply *= number
    return multiply
print(calc_sum())
print(calc_multiply())
