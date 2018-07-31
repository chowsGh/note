## [Redis 教程[http://www.runoob.com/redis/redis-tutorial.html]](http://www.runoob.com/redis/redis-tutorial.html)
1. Redis介绍
Redis是当前比较热门的NOSQL系统之一，它是一个key-value存储系统。和Memcache类似，但很大程度补偿了Memcache的不足，它支持存储的value类型相对更多，包括string、list、set、zset和hash。这些数据类型都支持push/pop、add/remove及取交集并集和差集及更丰富的操作。在此基础上，Redis支持各种不同方式的排序。
和Memcache一样，Redis数据都是缓存在计算机内存中，不同的是，Memcache只能将数据缓存到内存中，无法自动定期写入硬盘，这就表示，一断电或重启，内存清空，数据丢失。所以Memcache的应用场景适用于缓存无需持久化的数据。而Redis不同的是它会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，实现数据的持久化。
2. Redis的安装
下面介绍在Linux环境下，Redis的安装与部署
	1. 首先上官网下载Redis 压缩包，地址：http://redis.io/download 下载稳定版3.0.7即可。
	1. 通过远程管理工具，将压缩包拷贝到Linux服务器中，执行解压操作
	1. 执行make 对Redis解压后文件进行编译(推荐跑make test)
\o/ All tests passed without errors!

编译完成之后，可以看到解压文件redis-3.0.7 中会有对应的src、conf等文件夹，这和windows下安装解压的文件一样，大部分安装包都会有对应的类文件、配置文件和一些命令文件。
4、编译成功后，进入src文件夹，执行make install进行Redis安装
5、安装完成，界面如下

## config
- redis protected mode 需要修改redis.conf
bind 192.168.78.128

## 命令
- [command doc[https://redis.io/commands/]](https://redis.io/commands/)
- 客户端 redis-cli -h host -p port -a password
- key

``` shell
	COMMAND KEY_NAME
#查找与关键字匹配的键
	keys ${like key}
#获取键对应的值
	get ${key}
#设置键值
	set ${key} ${value}
#hashmap (Hash) 多用于保存对象
	HMSET key field value
	HGETALL key
	HGET key field
#列表(List)
	LPUSH key field
	LRANGE key start end
#查询剩余时间
	PTTL KEYNAME
```

- 安全

``` shell
	#获取是否有密码
	CONFIG get requirepass
	#设置密码
	CONFIG set requirepass "${password}"
	#取消密码
	CONFIG set requirepass ""
```

## client
 - java
 	- Jedis
 	- lettuce
 		- Advanced Redis client for thread-safe sync, async, and reactive usage. Supports Cluster, Sentinel, Pipelining, and codecs.

#todo list
 http://www.epubit.com.cn/article/200
 http://vdisk.weibo.com/s/aQrMod2amRiKD
 http://www.cnblogs.com/fanzhidongyzby/p/4098546.html
 https://www.datadoghq.com/pdf/Understanding-the-Top-5-Redis-Performance-Metrics.pdf
