#  To get the all possible subsequences

def equalToSum1(ind, res, sum, arr, size, value, sequence):
    if ind == size:
        if sum == value:
            sequence.append(list(res))
        return
    
    # * pick the element
    res.append(arr[ind])
    sum += arr[ind]
    equalToSum1(ind+1, res, sum,arr,size, value, sequence)
    sum -= arr[ind]
    res.pop()

    # * to not pick
    equalToSum1(ind+1, res, sum,arr,size, value, sequence)



# to get the only one random subsequence

def equalToSum2(ind, res, sum, arr, size, value, sequence2):
    if ind == size:
        if sum == value:
            sequence2.append(list(res))
            return True
        return False
    
    # * pick the element
    res.append(arr[ind])
    sum += arr[ind]
    if equalToSum2(ind+1, res, sum,arr,size, value, sequence2) == True:
        return True
    sum -= arr[ind]
    res.pop()

    # * to not pick
    if equalToSum2(ind+1, res, sum,arr,size, value, sequence2) == True:
        return True
    
    return False



# to get the count of total subsequences

def equalToSum(ind, sum, arr, size, value):
    if ind == size:
        if sum == value:
            return 1
        else :
            return 0
    
    # * pick the element
    sum += arr[ind]
    l = equalToSum(ind+1, sum,arr,size, value)
    sum -= arr[ind]

    # * to not pick
    r = equalToSum(ind+1, sum,arr,size, value)
    return l + r




# * Passing and Printing Parameters in this Area (Ignore This Part)
arr = [1,2,1,3,4,5,6,2,8,9]
n = len(arr)
value = 8
sequence = []
sequence2 = []


equalToSum1(0,[],0,arr,n,value,sequence)

equalToSum2(0,[],0,arr,n,value,sequence2)

print("All Subsequences : ")
for seq in sequence:
    print(seq)

print("One single random subsequence : ")
for seq in sequence2:
    print(seq)

print("To count the total number of subSequences :")
print(equalToSum(0,0,arr,n,value))
