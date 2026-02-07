#Maximumelement
def max_ele_(arr):
    max_ele=arr[0]

    for i in arr:
        if i>max_ele:
            max_ele=i
    return max_ele
    
arr=[1,2,3,0]
print(max_ele_(arr))


#Minelemt
def min_ele_(arr):
    min_ele=arr[0]

    for i in arr:
        if i<min_ele:
            min_ele=i
    return min_ele

arr=[1,2,3,0]
print(min_ele_(arr))


#secondlargest

def second_largest(arr):
    if len(arr) < 2:
        return "Second largest not possible"

    largest = float('-inf')
    second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num

    if second_largest == float('-inf'):
        return "All elements are equal or no second largest"
    
    return second_largest

    arr = [10, 20, 4, 45, 99]
print(second_largest(arr))
