def pascalsTriangle(n):
    res = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j==0 or j==i:
                temp_list.append(1)
            else:
                temp_list.append(res[i-1][j-1]+res[i-1][j])
        res.append(temp_list)
    return res

ros = int(input("Enter the number of rows : "))
print(pascalsTriangle(ros))


#only print the row of the given number

def get_pascal_row(k):
    if k < 0:
        return []

    row = [1]
    
    for i in range(k):
        next_val = row[-1] * (k - i) // (i + 1)
        row.append(next_val)
    
    return row

'''
Here's a step-by-step breakdown of how this approach works for k = 3:

- Initialize the row list as [1].
- First iteration (i = 0):
  next_val = row[-1] * (k - i) // (i + 1) = 1 * (3 - 0) // (0 + 1) = 3
  Append 3 to the row list: [1, 3].
- Second iteration (i = 1):
  next_val = row[-1] * (k - i) // (i + 1) = 3 * (3 - 1) // (1 + 1) = 3
  Append 3 to the row list: [1, 3, 3].
- Third iteration (i = 2):
  next_val = row[-1] * (k - i) // (i + 1) = 3 * (3 - 2) // (2 + 1) = 1
  Append 1 to the row list: [1, 3, 3, 1].
- The final row list is [1, 3, 3, 1].
  Using row[-1] accesses the last element of the row list, which is the previously calculated value. 
This allows us to generate the next value in the row based on the pattern observed in Pascal's triangle.

'''