
list1 = [8,3,2,0,7]

# creating sum_list function

def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
total = sumOfList(list1, len(list1))

print("Sum of all elements in given list: ", total)