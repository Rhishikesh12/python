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