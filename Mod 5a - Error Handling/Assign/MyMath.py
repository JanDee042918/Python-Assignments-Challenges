""" High level calculation for average and standard deviation using list and math module. """

import math

print(math.__doc__)
#print(math.sqrt.__doc__)
help(math.sqrt)

class MyMath:
    """
        Class used to request users to input numbers to add to the list.
        Average and standard deviation of the populated list will then be calculated.
    """

    def __init__(self, num_list = []):
        self.num_list  = num_list


num_list = []
NUM = 0

def prompt_error():
    prompt_error = print('Error: "Character entered cannot invoke calculations ', end='')


while 1:
    NUM += 1
    phrase_one = "Enter a number to add to the list"
    phrase_two = " or enter a non-numeric character to quit input: "
    sentence = phrase_one + phrase_two
    userInput = input(sentence)

    try:
        int(userInput)
        IT_IS = True
        
    except:
        IT_IS = False
   
    if IT_IS is False:
        print("~Input prompt ended~")
        break

    num_list.append(int(userInput))

print("Your list is", num_list)


def average(numbers):
    """Calculates and returns the average of a list of numbers."""

    try:
        sums = 0

        for nums in numbers:
            sums = sums + nums

        avg = sums / len(numbers)

        return avg
    
    except Exception:
        prompt_error()
        print('for average"')

def raised_difference(numbers):
    """
        Calls the function "average" to calculate and return the average
        of the raised difference of the list of numbers and the average.
    """
    try:

        raised_differences = 0
        sum_raised_difference = 0

        for nums in numbers:
            raised_differences = (nums - average(numbers)) ** 2
            sum_raised_difference =  sum_raised_difference + raised_differences

        avg2 = sum_raised_difference / len(numbers)

        return avg2

    except Exception:
        print(end="")

def standard_deviation(numbers):
    """
        Calls the function "raisedDifference" to calculate
        and return the standard deviation of the list of numbers.
    """
    try:
        standard_deviations = math.sqrt(raised_difference(numbers))
        return standard_deviations

    except Exception:
        prompt_error()
        print('for standard deviations"')


averageOfList = average(num_list)
stdDevOfList = standard_deviation(num_list)

print("Average =", averageOfList)
print("Standard Deviations =", stdDevOfList)