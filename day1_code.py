def fib_n(n):
    x = 1
    y = 1
    for i in range(n):
        if i+1 <= 2:
            print(1)
        else:
                ans = x + y
                print(ans)
                x = y
                y = ans
                
fib_n(8)

def arnums(*args):
    lenght = len(args)
    cnt1 = cnt2 = 1
    for x in args:
        cnt1 += 1
        for y in args:
            cnt2 += 1
            if cnt1 != cnt2:
                if cnt2 >= lenght - cnt1:
                    if x + y == 10:
                        print(x, " ", y)

arnums(3, 7, 10)