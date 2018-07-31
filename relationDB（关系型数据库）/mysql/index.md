[TOC]

# 安装

- [使用yum 安装linux (centos/red hat)](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)

  1. 下载仓库，去mysql 官网，然后下载对应系统版本的 rpm 包(wget {{url}})
  2. 安装仓库 yum install {{mysql.rpm}} 或者 rpm -Uvh platform-and-version-specific-package-name.rpm
  3. 检查需要安装的mysql，yum repolist all | grep mysql

    - shell> sudo yum-config-manager --disable mysql57-community
    - shell> sudo yum-config-manager --enable mysql56-community

  4. a. 也可以创建mysql 的repo

  5. b. 检查可以安装的mysql yum repolist enabled | grep mysql

  6. 查看可以安装的 mysql 包名，yum list | grep mysql ，然后安装mysql yum install mysql-community-server
  7. 启动mysql
  8. 5.7 mysql 启动了以后初始化密码sudo grep 'temporary password' /var/log/mysqld.log，
  9. mysql -u root -p 登录以后修改密码
  10. ALTER USER 'root'@'%' IDENTIFIED BY '-pl,0okm';#如果有密码安全级别 Your password does not satisfy the current policy requirements
  11. 修改密码安全级别, set global validate_password_policy=0

    ```
    Policy    Tests Performed
    0 or LOW     Length
    1 or MEDIUM     Length; numeric, lowercase/uppercase, and special characters
    2 or STRONG     Length; numeric, lowercase/uppercase, and special characters; dictionary file
    ```

- [使用二进制文件安装](https://dev.mysql.com/doc/refman/5.6/en/binary-installation.html)

- windows 下载msi 安装包直接安装

  ## [INFORMATION_SCHEMA Tables(mysql 数据库 信息数据库)](https://dev.mysql.com/doc/refman/5.7/en/information-schema.html)

- INFORMATION_SCHEMA provides access to database metadata, information about the MySQL server such as the name of a database or table, the data type of a column, or access privileges. Other terms that are sometimes used for this information are data dictionary and system catalog.

  # mysql 配置文件 /etc/my.cnf

# 慢查询日志

1. 开启慢查询，设置变量

  - show variables like '%slow%';
  - slow_query_log_file="/var/log/slow_query.log", slow_query_log=ON|OFF 或者(1|0)
  - long_query_time=2.0 查询时间超过这个值就会被记录下载
  - 如果在my.cnf 里面设置了以后 重启mysql 就会根据 my.cnf里的参数来设置。
  - 也可以 设置全局 变量 set global slow_query_log_file="/var/log/slow.log"
  - 如果设置on 后没有 开启慢查询，则检查my.cnf 里面配置的 error_log 的异常日志文件 例如 /var/log/mysqld.log 查看异常
  - [慢查询 linux 权限问题](http://blog.csdn.net/reblue520/article/details/50824702)

2. 生成慢查询日志

3. 分析慢查询日志

  - 通用环境

    - mysqldumpslow，mysql官方自带的分析工具，但是需要perl环境 -

  - linux 环境

    - ，[percona-toolkit下载](https://www.percona.com/downloads/percona-toolkit/LATEST/)

# 使用delete 跟 where 条件 删除表数据 后 表存储空间没有变小

- 如果是 MyISAM 需要用 OPTIMIZE table t_user_device优化表， 记录数过大的话，执行过程会很慢，需要找一个 空闲时间,
- "Table" "Op" "Msg_type" "Msg_text"
- "karaoke-province.t_user_device" "optimize" "status" "OK"

# 查询某个数据库各个表大小

SELECT TABLE_NAME,(DATA_LENGTH+INDEX_LENGTH)/1024 as 'Size (KB)',TABLE_ROWS FROM information_schema.tables where TABLE_SCHEMA = '${schema-name}'

# 查询数据库 信息

SHOW TABLE STATUS FROM '{{schema-name}};

# HeidiSQL

What's this? HeidiSQL is a useful and reliable tool designed for web developers using the popular **MySQL server**, **Microsoft SQL** databases and **PostgreSQL**. It enables you to browse and edit data, create and edit tables, views, procedures, triggers and scheduled events. Also, you can export structure and data either to SQL file, clipboard or to other servers. ... read about features or see some screenshots.

# 查看索引 show index from {{tableName}}

# 建立索引[MySQL索引背后的数据结构及算法之基础篇](http://database.51cto.com/art/201107/275006_all.htm)

# 检查sql语句 EXPLAIN select count(id) from t_user_device where old_user_id='chows'

- [MySQL Explain](https://my.oschina.net/heweipo/blog/807661)
- "id" "select_type" "table" "type" "possible_keys" "key" "key_len" "ref" "rows" "Extra"
- "1" "SIMPLE" "t_user_device" "ref" "old_user_id" "old_user_id" "62" "const" "4" "Using where"

```
Explain命令
用于分析sql语句的执行情况和成本预估
今天我们重点学习type指标
指标逐渐降低：

systme>const>eq_ref>ref>fulltext>ref_or_null>index_merge>unique_subquery>index_subquery>range>index>all
1
1.const
如果是根据主键或唯一索引 只取出确定的一行数据。是最快的一种。
2.range
索引或主键，在某个范围内时
3.index
仅仅只有索引被扫描
4.all
全表扫描，最令人心痛
```

# 显示哪些线程正在运行

- SHOW PROCESSLIST; 非root 用户则会显示 自己所用的线程，root 用户最多显示100条

  # 显示全部线程

- show full processlist;

# 杀掉mysql在 SHOW PROCESSLIST; 中查询到在运行的查询 id 表示 thread_id;

kill thread_id; 因为navicat mysql 奔溃 导致原来的长时间查询没有断，影响mysql server 性能

# 查询数据库版本

select version(); || mysql> status;

# mysql 用户创建 修改[官方文档](https://dev.mysql.com/doc/refman/5.5/en/sql-syntax-server-administration.html)，[mysql用户创建没有通过密码验证](https://www.cnblogs.com/ivictor/p/5142809.html)

```
# host = {{%|127.0.0.1|172.16.4.94}}, 在create user, grant 的shihou host 要相同
# password = {{pl_0okm}}， 设置密码的时候 有密码验证级别select @@validate_password_policy
#Policy    Tests Performed
#0 or LOW    Length
#1 or MEDIUM    Length; numeric, lowercase/uppercase, and special characters
#2 or STRONG    Length; numeric, lowercase/uppercase, and special characters; dictionary file
# 如果需要其他ip连接 需要将host设置成%
CREATE USER 'jeffrey'@'{{host}}' IDENTIFIED BY '{{password}}}';
GRANT ALL ON .* TO 'jeffrey'@'{{host}}';
RENAME USER 'jeffrey'@'%' TO 'blkg_demo'@'%';
SET PASSWORD FOR 'blkg_demo'@'%' = PASSWORD('blkg_demo_2017');
flush privileges;
```

# select current_timestamp, current_timestamp(); 时间戳

# 查询外间关系

select CONSTRAINT_NAME,TABLE_NAME, COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where CONSTRAINT_SCHEMA = 'ott-karaoke-central' and CONSTRAINT_NAME <> 'PRIMARY' and CONSTRAINT_NAME <>'UNIQUESONGLIST' ORDER BY TABLE_NAME

# 查询所有的表

select table_name as '表名', '' as '描述' from information_schema.tables where table_schema='ott-karaoke-central' select table_name as '表名', '' as '描述' from information_schema.tables where table_schema='karaoke-province'

# 拼接字符串

CONCAT('resources/upload/player/hd/',code,'.jpg')

# 字段转换

- CAST(value as type);
- CONVERT(value, type);

  - CONVERT(prize,SIGNED)

# 复制表

<http://www.jb51.net/article/41570.htm> create table as （仅仅复制数据） insert into table(c1,c3) select c1,c3 from table2 create table like （复制表结构）

# 通用客户端 dbeaver 支持有 jdbc 的数据库

# 常用操作

1. 备份表

  - 使用场景
  - 用户

use information_schema; select _from COLUMNS where TABLE_SCHEMA='ott-karaoke-central' and COLUMN_DEFAULT IS NOT null; use `ott-karaoke-central`; show index from t_column ;#where key_name != 'PRIMARY'; select TABLE_NAME,TABLE_COMMENT from INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA = 'karaoke-province' order by TABLE_NAME select_ from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where CONSTRAINT_SCHEMA='ott-karaoke-central' AND CONSTRAINT_NAME <> 'PRIMARY' and REFERENCED_COLUMN_NAME is not null order by TABLE_NAME;

select * from INFORMATION_SCHEMA.TABLE_CONSTRAINTS show index from t_action_log where key_name != 'PRIMARY' show index from t_action_log_detail where key_name != 'PRIMARY'

show INFORMATION_SCHEMA

# 数据库升级

- 5.7 加入了 sql_mode 的元素，默认的sqlmod是 select 语句中如果 有group by 则select 的字段必须要是group by 出现的，

# mysql DQL (Data Query Language数据查询语言)

```
- select
- group by
- having
- where, and, or
- in exist
- 子查询
```

# mysql DML (Data Manipulation Language 数据操作语言)

```
- insert into t1 (c1,c2)... select c1,c2 from t2
```

# mysql DDL (Data Define Language 数据定义语言)

```
- 备份数据
- create table {{t1}} as select * from {{t2}}
    - 根据查询数据的表 创建 表
- create table {{t1}} like select * from {{t2}}
    - 根据查询数据的表 创建 原表 结构一样， 数据一样的表
```

# mysql 函数

- locate 类似indexOf

  - SELECT * FROM `blkg-show-province-demo`.ai_song where locate('10006', concat(Label1,Label2,Label3,Label4,Label5)) > 0;

- concat

  - concat(str1, str2,...),如果有任何一个参数为null，则返回值为null。

- concat_ws

  - concat_ws({{separator}}, str1, str2, ...)

- group_concat

- substring | SUBSTRING_INDEX

  - SELECT SUBSTRING('foobarbar' FROM 4);
  - SELECT SUBSTRING('Quadratically',5,6);
  - str=www.google.com; substring_index(str,'.',1)
  - str=www.google.com; substring_index(substring_index(str,'.',-2),'.',1);

- max|min

- first|last

- avg
- sum
- length
- NOW|CURRENT_TIMESTAMP、SYSDATE

  - CURRENT_TIMESTAMP是NOW的同义词，也就是说两者是相同的。
  - SYSDATE函数返回的是执行到当前函数时的时间，而NOW返回的是执行SQL语句时的时间。
  - select now();

- sleep({{x}}) :查询暂停{{x}}s

  - select sleep({{x}});

    # 常用逻辑

  - 组内排序，可以使用max(datetime, int) 来实现，或者使用子查询，查询

    # 基本数据结构

  - text

  - blob

    # 其他

- 条件选择 case when {{condition}} then {{value1}} else {{value2}} end

  - 可以在select 中使用 例如 select case when 1 > 2 then '1 less then 2' else '1 greater then 2' end;
