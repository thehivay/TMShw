# 10 a)
def task_10(number):
    a = len(str(number))
    b = number//(10**(a-1))
    c = 3 <= b <= 8
    return a, c


print(task_10(34567))


# 10 b)
def task_10(number):
    a = len(str(number))
    b = int(number[0])
    c = 3 <= b <= 5
    return a, c


print(task_10('1234'))



