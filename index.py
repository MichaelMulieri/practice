"""Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original 
list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, 
have the function return False
Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]"""


def valGreaterThanSecond(inputList):
    newList = []
    secondVal = inputList[1]
    for i in range(len(inputList)):
        if inputList[i] > secondVal:
            newList.append(inputList[i])
    print(len(newList))
    return newList


print(valGreaterThanSecond([5, 2, 3, 2, 1, 4]))

"""Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]"""


def biggieSize(inputList):
    for i in range(len(inputList)):
        if inputList[i] > -1:
            inputList[i] = "big"
    return inputList


print(biggieSize([-1, 3, 5, -5]))

"""Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
(Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it"""


def countPositives(inputList):
    sum = 0
    for i in range(len(inputList)):
        if inputList[i] > 0:
            sum += 1
    inputList[-1] = sum
    return inputList


print(countPositives([1, 6, -4, -2, -7, -2]))

"""Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7"""


def sumTotal(inputList):
    sum = 0
    for i in range(len(inputList)):
        sum += inputList[i]
    return sum


print(sumTotal([1, 2, 3, 4]))
print(sumTotal([6, 3, -2]))

"""Average - Create a function that takes a list and returns the average of all the values.
Example: average([1,2,3,4]) should return 2.5"""


def Average(inputList):
    sum = 0
    for val in inputList:
        sum += val
    return float(sum)/float(len(inputList))


print(Average([1, 2, 3, 4]))

"""Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0"""


def Length(lst):
    total = 0
    for val in lst:
        total += 1
    return total


print(Length([37, 2, 1, -9]))
print(Length([]))

"""Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False"""


def Minimum(lst):
    if len(lst) == 0:
        return False
    result = lst[0]
    for val in lst:
        if val < result:
            result = val
    return result


print(Minimum([37, 2, 1, -9]))
print(Minimum([]))

"""Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False"""


def Maximum(lst):
    if len(lst) == 0:
        return False
    result = lst[0]
    for val in lst:
        if val > result:
            result = val
    return result


print(Maximum([2, 37, 1, -9]))

"""Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }"""


def uAna(lst):
    uDict = {'sumTotal': None, 'average': None,
             'minimum': None, 'maximum': None, 'length': 0}

    if len(lst) == 0:
        return False

    else:
        uDict['sumTotal'] = 0
        uDict['maximum'] = lst[0]
        uDict['minimum'] = lst[0]

    for val in lst:
        if val > uDict['maximum']:
            uDict['maximum'] = val
        elif val < uDict['minimum']:
            uDict['minimum'] = val

        uDict['sumTotal'] += val
        uDict['length'] += 1
    uDict['average'] = uDict['sumTotal']/len(lst)

    return uDict


print(uAna([37, 2, 1, -9]))

# alternate aproach


def ultimate_analysis(someList):
    sum = 0
    min = someList[0]
    max = someList[0]
    length = len(someList)
    for item in someList:
        sum += item
        if item < min:
            min = item
        elif item > max:
            max = item
    average = float(sum)/float(length)
    ultimateDict = {'sumTotal': sum, 'average': average,
                    'minimum': min, 'maximum': max, 'length': length}
    return (ultimateDict)


"""Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. 
(This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]"""


def Revlst(lst):
    halfLength = int(len(lst) / 2)
    for i in range(halfLength):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

    return lst


print(Revlst([37, 2, 1, -9]))
