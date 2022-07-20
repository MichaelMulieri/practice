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


print(valGreaterThanSecond([5,2,3,2,1,4]))

"""Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]"""

def biggieSize(inputList):
    for i in range(len(inputList)):
        if inputList[i] > -1:
            inputList[i] = "big"
    return inputList

print(biggieSize([-1,3,5,-5]))

"""Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
(Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it"""

def countPositives(inputList):
    sum = 0
    for i in range(len(inputList)):
        if inputList[i] > 0:
            sum+=1
    inputList[-1] = sum
    return inputList


print(countPositives([1,6,-4,-2,-7,-2]))

"""Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7"""

def sumTotal(inputList):
    sum = 0
    for i in range(len(inputList)):
        sum += inputList[i]
    return sum

print(sumTotal([1,2,3,4]))
print(sumTotal([6,3,-2]))
