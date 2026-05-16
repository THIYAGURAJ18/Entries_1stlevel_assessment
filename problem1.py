def second_largest(arr):
    first = second = float('-inf')

    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x

    return -1 if second == float('-inf') else second



print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))  
print(second_largest([10, 10, 10]))            
print(second_largest([5, 3]))                  
print(second_largest([-1, -2, -3]))            
