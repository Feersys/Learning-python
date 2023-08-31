def Fibonachhi(n, a = 1, b = 1):
    if n < 1 :
        return a + b
    print(b)
    f = Fibonachhi(n - 1, b, a + b)
    return f

#Fibonachhi(7)


def Factorial(x):
    if x == 1:
        return x
    f = Factorial(x-1)*x
    print(f)
    return f

#Factorial(6)


def triangle(n):
    if n == 1:
        return [1]
    else:
        new_row = [1]
        last_row = triangle(n - 1)
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        print(new_row)
    return new_row

triangle(7)

def Palindrom(s):
    if len(s) == 1:
        return True
    elif s[0] == s[-1]:
        return Palindrom(s[1:-1])
    else:
        return False
print(Palindrom("tetat"))
x1 = 0
x2 = 1
for i in range(8):
    temp = x1 + x2
    x1 = x2
    x2 = temp
    #print(x1)