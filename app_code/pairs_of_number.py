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
