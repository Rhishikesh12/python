'''
1) SubSequences are not SubArrays,
2) SubSequences can be contiguous or non-contiguous, but subarrays are contiguous.
3) subsequences follows array order.
4) subarrys can be a subsequences.

Given : 

arr = [3,2,1]  return all the subSequences

'''
def subSequences(start, arr, res, n, subsequences):
    if start == n:
        subsequences.append(list(res))
        return

    # pick and add the element to the subsequence
    res.append(arr[start])
    subSequences(start + 1, arr, res, n, subsequences)
    res.pop()

    # dont pick the element
    subSequences(start + 1, arr, res, n, subsequences)


arr = [3, 2, 1]
subsequences = []
subSequences(0, arr, [], len(arr), subsequences)

for subseq in subsequences:
    print(subseq)
