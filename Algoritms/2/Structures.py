import random
def Anagrams():
    str1 = str(input("Dведите первое предложение: "))
    str2 = str(input("Введите второе предложение: "))
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    m1 = list(str1)
    m2 = list(str2)
    m1.sort()
    m2.sort()
    print(m1)
    print(m2)
    if m1 == m2:
        check = True
    else:
        check = False
    print(check)
    return check


# Anagrams()
def Number():
    nums = input()
    s = nums.split()
    for i in range(len(s)):
        s[i] = int(s[i])
    s.sort()
    print(s)
    res = []
    b = None
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1] - 1:
            if b is None:
                b = s[i]
        else:
            if b is None:
                res.append(str(s[i]))
            else:
                res.append(f"{b} - {s[i]}")
                b = None
    print(", ".join(res))


# Number()
s = [10, 5, 6, 4, 3, 1, 1, 6]
k = 15


def Podotrezki(s, k):
    a = 0
    check = 0
    for j in range(len(s)):
        for i in range(j, len(s)):
            a += s[i]
            if a == k:
                check += 1
                a = 0
                break
            elif a > k:
                a = 0
                break

    print(check)


# Podotrezki(s, k)
s = [[0, 1],[750, 2],[500, 1],[250, 2], [1000, 1]]


def X(s):
    def get_x(s):
        return s[0]

    if len(s) % 2 != 0:
        print("Невозможно указать заданную прямую")

    s.sort(key=get_x)
    print(s)
    d = {}
    center = 0
    for i in range(len(s)):
        center += s[i][0]
    center /= len(s)
    print("Center: ", center)
    for i in range(len(s)):
        x = s[i][0]
        y = s[i][1]
        if x == center:
            continue
        for j in range(len(s)):
            x1 = s[j][0]
            y1 = s[j][1]
            if center - x == x1 - center and y == y1:
                flag = True
                break
            else:
                flag = False
        if not flag:
            break
    print(flag)
    return flag


#X(s)
# 1) Найти среднее арифметическое по х
# 2) Сортировать по х
# 3) Искать симметричность(расстояние до прямий одинаковое и у одинаковое)
# 4) Если не одинак, то ретурн фалсе
def f():
    #a = random.randint(1, 500)
    a = 27
    print(a)
    check = 0
    paths = {}
    d = {}
    while a!= -1:
        path =[a]
        while a != 1:
            b = a
            if a%2 == 0:
                a/=2
            else:
                a*=3
                a+=1
            a = int(a)
            d[b] = a
            check +=1
            path.append(a)
        print(path)
        for key,value in d.items():
            print(key, ":", value)
        print("Кол-во шагов: ", check)
        for i in range(len(path)):
            paths[path[i]]=path[i+1:]
        sorted(paths.keys())
        print(paths)
        a = int(input("Введите новое значение. Для выхода введите -1: "))
    return a


f()