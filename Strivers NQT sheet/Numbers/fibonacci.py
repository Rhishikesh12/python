def fib(num):
    if num == 0:
        return [0]
    if num == 1:
        return [0, 1]
    series = fib(num - 1)
    series.append(series[-1] + series[-2])
    return series

num = 8
res = fib(num)
print(res)
