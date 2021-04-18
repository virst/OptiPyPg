SELECT e.x
      ,e.rez
      ,SUM(x.rez_v) rez_v
      ,e.rez - SUM(x.rez_v) delt
  FROM toilp_mc_eq e
 CROSS JOIN TABLE(mc_utils.regexp_split_to_table(e.x, '[^,]+')) t
  JOIN toilp_mc_x x
    ON x.x = TRIM(t.column_value)
 GROUP BY e.x
         ,e.rez
 ORDER BY delt desc
