select e.id, e.nm, e.rez, sum(x.val) as v_rez, sum(x.val) - e.rez as delt
 from eq.eq_equations e
join eq.eq_equations_x ex on e.id = ex.id_eq
join eq.eq_xs x on x.id = ex.id_x
where e.id_task = 100
group by e.id, e.nm, e.rez
order by delt desc