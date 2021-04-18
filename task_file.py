from eq import *


def get_task(fn):
    t = Task()

    file = open(fn + '.x')
    for line in file:
        if line.isspace():
            continue
        ss = [s.strip() for s in line.split('=')]
        t.xs[ss[0]] = float(ss[1])

    file = open(fn + '.eq')
    for line in file:
        if line.isspace():
            continue
        ss = [s.strip() for s in line.split('=')]
        t.eqs.append(Equation([s.strip() for s in ss[0].split(',') if s != ''], int(ss[1])))

    return t


def set_task_data(xs, fn):
    f = open(fn + '.rez', 'w')
    n = 0
    for x in xs:
        n = n + 1
        f.write(str(x) + " = " + str(xs[x].varValue) + '\n')
    f.close()
    return n
