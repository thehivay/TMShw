def task_2(st):
    x = len(st)
    y = x//2
    result = st[y:x]+st[:y]
    result = st[y:x]+st[0:y]
    return result


print('Первый способ task_2:', task_2('123456789'))



def task_2(st):
    a = len(st)
    a1 = a//2
    st1 = st[:a1]
    st2 = st[a1:]
    result = st2 + st1
    return result


print('Второй способ task_2:', task_2('123456789'))
