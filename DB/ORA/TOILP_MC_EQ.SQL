-- Create table
create table TOILP_MC_X
(
  c_st    VARCHAR2(5),
  c_dt    DATE,
  p_st    VARCHAR2(5),
  p_dt    DATE,
  x       NUMBER not null,
  k       NUMBER,
  rez_x   NUMBER,
  f_rez_x NUMBER,
  f_max_x NUMBER,
  f_min_x NUMBER,
  rez_v   NUMBER
)
tablespace RWC
  pctfree 10
  initrans 1
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
-- Create/Recreate primary, unique and foreign key constraints 
alter table TOILP_MC_X
  add constraint TOILP_MC_X_PK primary key (X)
  using index 
  tablespace RWC
  pctfree 10
  initrans 2
  maxtrans 255
  storage
  (
    initial 64K
    next 1M
    minextents 1
    maxextents unlimited
  );
