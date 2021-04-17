import psycopg2
from eq import *


def get_task(task_id):
    t = Task()
    con = psycopg2.connect(
        database="v_test",
        user="virst",
        password="111399",
        host="192.168.1.80",
        port="5432"
    )

    print("Database opened successfully")

    cur = con.cursor()
    cur.execute("SELECT nm, k FROM eq.eq_xs x where x.id_task = " + str(task_id) + "order by 1")
    rows = cur.fetchall()
    for row in rows:
        t.xs[row[0]] = row[1]
    print("X's - loaded")

    cur.execute("SELECT id, rez FROM eq.eq_equations e where e.id_task = " + str(task_id))
    rows = cur.fetchall()
    eq_list = {}
    for row in rows:
        eq_list[row[0]] = row[1]

    n = 0
    ln = len(eq_list)
    for el in eq_list:
        n = n + 1
        print(str(n) + "/" + str(ln))
        t.eqs.append(Equation([], eq_list[el]))
        cur.execute('''SELECT x.nm FROM eq.eq_equations e
            join eq.eq_equations_x ex on ex.id_eq = e.id
            join eq.eq_xs x on ex.id_x = x.id
            where e.id = ''' + str(el))
        rows = cur.fetchall()
        for row in rows:
            t.eqs[-1].xs.append(row[0])

    print("Equations - loaded")
    cur.close()
    con.close()

    return t


def set_task_data(xs, task_id):
    n = 0
    con = psycopg2.connect(
        database="v_test",
        user="virst",
        password="111399",
        host="192.168.1.80",
        port="5432"
    )
    cur = con.cursor()
    update_query = "update eq.eq_xs set val = %s where nm = %s and id_task = %s"
    for x in xs:
        n = n + 1
        item_tuple = (xs[x].varValue, x, task_id)
        cur.execute(update_query, item_tuple)
        print(n)
    cur.close()
    con.commit()
    con.close()
    return n
