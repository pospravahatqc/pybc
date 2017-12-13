from pbc import log_decorator

# @log_decorator
def fibn(n):
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