def average(arr):
    return sum(arr)/ len(arr)

arr = [1,2,3,4,5]
res = average(arr)
print(res)

# Python does not provide avg() method to calculate average of elements

#  Using while Loop
array = [1, 2, 3, 4, 5]
total = 0
count = 0
index = 0

while index < len(array):
    total += array[index]
    count += 1
    index += 1

average = total / count
print(average)
