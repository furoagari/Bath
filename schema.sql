drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  N text not null,
  MagX text not null,
  MagY text not null,
  MagZ text not null,
  AccX text not null,
  AccY text not null,
  AccZ text not null,
  Uv text not null,
  Lx text not null,
  Humi text not null,
  Temp text not null,
  Press text not null
);
