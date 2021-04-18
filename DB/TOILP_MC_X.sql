-- Create table
create table TOILP_MC_EQ
(
  x         VARCHAR2(4000),
  eq        CHAR(2),
  rez       NUMBER,
  st        VARCHAR2(5),
  dt        DATE,
  c_p       CHAR(1),
  f_max_all NUMBER,
  f_min_all NUMBER
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
-- Create/Recreate indexes 
create unique index I43213424 on TOILP_MC_EQ (ST, DT, C_P)
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
