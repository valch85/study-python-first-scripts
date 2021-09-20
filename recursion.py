def test(x):
    if x > 9 :
        return test(x - 10)
    else:
        print('real value',x)
        return x

x = int(input())
y = test(x)
print('this should be real value',y)