from eq import *


def get_task():
    t = Task()
    t.xs[0] = 1
    t.xs[1] = 2.3
    t.xs[2] = 4.1
    t.xs[3] = 11.7
    t.xs[4] = 3.14

    t.eqs.append(Equation([0, 1], 50))
    t.eqs.append(Equation([1, 2], 7))
    t.eqs.append(Equation([1, 3], 19))
    t.eqs.append(Equation([2, 3, 4], 40))

    return t


def set_task_data(xs, task_id):
    return -1
