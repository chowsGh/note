# MySQL Server Logs
- summary
  - Log Type, Information Written to Log.
  - Error log, Problems encountered starting, running, or stopping mysqld
  - General query log
Established client connections and statements received from clients
  - Binary log
Statements that change data (also used for replication)
  - Relay log
Data changes received from a replication master server
  - Slow query log
Queries that took more than long_query_time seconds to execute
  - DDL log (metadata log)
Metadata operations performed by DDL statements

## 慢查询日志 Slow query log
- [MySQL慢查询（一） - 开启慢查询](http://www.cnblogs.com/luyucheng/p/6265594.html)
  - 操作步骤
    1. 慢查询配置默认是关闭状态，查询 慢查询 slow_query_log (1,ON|0,OFF),long_query_time(超过这个时间，记录慢查询单位秒可以为小数字)参数，slow_query_log_file="/var/log/slow.log"(慢查询日志路径，**注意 mysql运行的用户有该文件的写权限，如果出现权限问题可以参考SElinux**)。show global variables like 'slow%'
- 慢查询日志分析
