a = [1,0,1]
b = [1,0,1]
c = [1,1,1]

def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    counter =0
    while counter <= (len(list1)-1):
        if list1[counter] != list2[counter]:
            return False
        counter += 1
    
    return True 


print(is_equal(a,b))
print(is_equal(b,c))
print(is_equal(a,c))