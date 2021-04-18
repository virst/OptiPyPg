from pulp import *
from task_ora import get_task, set_task_data
import time

task_id = 'task4'

start = time.time()

t = get_task(task_id)
print("Загружено.")
xs = LpVariable.dicts("X", t.xs, lowBound=0, cat='Integer')

problem = pulp.LpProblem('0', LpMinimize)
problem += lpSum([t.xs[i] * xs[i] for i in t.xs])
for e in t.eqs:
    problem += lpSum([xs[x] for x in e.xs]) == e.rez
print("Заполнено.")
problem.solve()

time_o = time.time() - start
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Сохранение результата.")
print(set_task_data(xs, task_id))
print("Итог:")
print(value(problem.objective))
stop = time.time()
print("Время оптимизации:")
print(time_o)
print("Время общее:")
print(stop - start)
