# 主从复制
## what is replication
### 使用范围
## why need replication
## how to use replication
1. 修改主数据库 配置
  - 配置二进制日志（bin-log）
  ```
[mysqld]
log-bin=mysql-bin
server-id=1
  ```
  - **重启mysql**(必须)
2. 创建 从数据库访问 帐号
```
mysql>
CREATE USER 'repl'@'%.mydomain.com' IDENTIFIED BY 'slavepass';
mysql>
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%.mydomain.com';
```
3. 获取主数据库 二进制坐标（Binary Log Coordinates）
  1. SHOW MASTER STATUS 如果是空，即记录数据开始就开启了二进制日志
  2. 已经记录过二进制日志 需要开启两个mysql客户端 一次执行 下面指令找到二进制坐标
    1. FLUSH TABLES WITH READ LOCK;
    2. SHOW MASTER STATUS;
    ```
    +------------------+----------+--------------+------------------+
    | File             | Position | Binlog_Do_DB | Binlog_Ignore_DB |
    +------------------+----------+--------------+------------------+
    | mysql-bin.000003 | 73       | test         | manual,mysql     |
    +------------------+----------+--------------+------------------+
    ```
4. 主数据库快照
为保证数据的一致性，dump 出脚本 然后记录  SHOW MASTER STATUS; 的坐标 file, position 用于导入到从数据库
5. 配置从数据库
```
[mysqld]
server-id=2
```
6. 从数据库设置主数据库
CHANGE MASTER TO MASTER_HOST='192.168.35.1', MASTER_USER='repl', MASTER_PASSWORD='slavepass',MASTER_LOG_FILE='mysql-bin.000003',MASTER_LOG_POS=73;
stop slave;
start slave;

## replication scenarios
1. 数据备份
2. 读写分离

## 工作原理


## 参考
[MySQL主从复制(Master-Slave)实践](https://www.cnblogs.com/gl-developer/p/6170423.html)
