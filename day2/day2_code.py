def fib_n(n):
    x = 1
    y = 1
    res = []
    for i in range(n):
        if i+1 == n:
            continue
        if i+1 == 1:
            res.append(0)
        if i+1 <= 2:
            res.append(1)
        else:
                ans = x + y
                res.append(ans)
                x = y
                y = ans
    return res

print(fib_n(0))

def arnums(*args):
    expected = 10
    lenght = len(args)
    cnt1 = cnt2 = 1
    res = set()
    for x in range (lenght):
        for y in range(lenght):
            if x != y and args[x] + args[y] == expected:
                pair = min(args[x], args[y]), max(args[x], args[y])
                res.add(pair)
    return res

in1 = [3, 7, 10]
print(arnums(1, 2, 3, 4, 5, 6, 7, 8, 9))

