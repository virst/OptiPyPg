import cx_Oracle as ora
from eq import *


def get_task(task_id):
    t = Task()
    dsnStr = ora.makedsn(host="172.30.2.139", port="1521", sid="ORCL")
    con = ora.connect(user="RWC", password="RWC", dsn=dsnStr)
    print("Database opened successfully")

    cur = con.cursor()
    cur.execute('SELECT X, K FROM toilp_mc_x order by 1')
    rows = cur.fetchall()
    for row in rows:
        t.xs[str(row[0])] = float(row[1])
    print("X's - loaded")

    cur.execute("SELECT X, REZ FROM toilp_mc_eq")
    rows = cur.fetchall()
    for row in rows:
        t.eqs.append(Equation([s.strip() for s in row[0].split(',') if s != ''], int(row[1])))

    print("Equations - loaded")
    cur.close()
    con.close()

    return t


def set_task_data(xs, task_id):
    dsnStr = ora.makedsn(host="172.30.2.139", port="1521", sid="ORCL")
    con = ora.connect(user="RWC", password="RWC", dsn=dsnStr)
    cur = con.cursor()

    n = 0
    update_query = "update toilp_mc_x set rez_v = :v where x = :x"
    for x in xs:
        n = n + 1
        cur.execute(update_query, {':v': xs[x].varValue, ':x': x})
        print(n)
    cur.close()
    con.commit()
    con.close()

    return n
