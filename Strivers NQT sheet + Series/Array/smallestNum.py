
# Default approach using Sort()
# T.C : O(nlogn)
def small_num(list):
    list.sort()
    return list[0]


list = [2,5,1,7,4]
res = small_num(list)
print(res)




# Optimized Approach
# O(n)
def small_num(list):
    min_val = list[0]
    for x in range(len(list)):
        if min_val > list[x]:
            min_val = list[x]
    return min_val

list = [2,5,1,0,4]
res = small_num(list)
print(res)

list3 = [3,6,7,9,2]
res = small_num(list3)
print(res)