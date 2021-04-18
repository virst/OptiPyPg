CREATE OR REPLACE PACKAGE mc_utils IS

  -- Author  : VMV
  -- Created : 10.04.2021 11:55:52
  -- Purpose : 

  TYPE t_string IS TABLE OF VARCHAR2(4000);

  TYPE t_num IS TABLE OF NUMBER;

  FUNCTION regexp_split_to_table(text VARCHAR2
                                ,pattern VARCHAR2) RETURN t_string
    PIPELINED;

  FUNCTION generate_series(b NUMBER
                          ,e NUMBER) RETURN t_num
    PIPELINED;

END mc_utils;
/
CREATE OR REPLACE PACKAGE BODY mc_utils IS

  FUNCTION regexp_split_to_table(text VARCHAR2
                                ,pattern VARCHAR2) RETURN t_string
    PIPELINED IS
  
  BEGIN
    FOR rec IN (SELECT regexp_substr(text, pattern, 1, LEVEL) str
                  FROM dual
                CONNECT BY regexp_substr(text, pattern, 1, LEVEL) IS NOT NULL)
    LOOP
      PIPE ROW(rec.str);
    END LOOP;
  END;

  FUNCTION generate_series(b NUMBER
                          ,e NUMBER) RETURN t_num
    PIPELINED IS
    rez NUMBER;
  BEGIN
    rez := b;
    LOOP
      EXIT WHEN rez > e;
      PIPE ROW(rez);
      rez := rez + 1;
    END LOOP;
  END;

END mc_utils;
/
