def filt_pr(s):
    ss = []
    for i in s:
        if i < 2:
            continue
        check = True
        for j in range(2, int(pow(i, 1/2))+1):
            if i%j == 0:
                check = False
                break
        if check:
            ss.append(i)
    return ss

arr = list(map(int, input().split()))

print(filt_pr(arr))