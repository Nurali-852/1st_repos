def filt(n):
    if n<2: 
        return False
    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False
    return True

l = [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]

ans = list(filter(lambda x: filt(x), l)) #filter(function, iterable) из списка l каждый икс проходит через функцию
print(ans)
    