def equalToSum(ind, res, sum, arr, size, value, sequence):
    if ind == size:
        if sum == value:
            sequence.append(list(res))
        return
    

    # * pick the element
    res.append(arr[ind])
    sum += arr[ind]
    equalToSum(ind+1, res, sum,arr,size, value, sequence)
    sum -= arr[ind]
    res.pop()

    # * to not pick
    equalToSum(ind+1, res, sum,arr,size, value, sequence)


# * Passing and Printing Parameters in this Area
arr = [1,2,1]
n = len(arr)
value = 2
sequence = []
equalToSum(0,[],0,arr,n,value,sequence)

for seq in sequence:
    print(seq)
