ZooKeeper入门指南
==

## 系统要求
请参阅[管理指南](http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_systemReq)中的[系统要求](http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_systemReq)。

## 下载
要获取ZooKeeper发行版，请从其中一个Apache下载镜像下载最新的 [稳定版本](http://zookeeper.apache.org/releases.html)

## 单机操作
在单机模式下设置ZooKeeper服务器非常简单。服务器包含在单个JAR文件中，因此安装包括创建配置。
一旦你下载了一个稳定的ZooKeeper版本，
要启动ZooKeeper，您需要一个配置文件。这是一个示例，在conf / zoo.cfg中创建它：
```
tickTime=2000
# windows dataDir 不能使用反斜杠（\）
dataDir=/var/lib/zookeeper
clientPort=2181
```

- tickTime :
ZooKeeper使用的基本时间单位（以毫秒为单位）。它用于做心跳，最小会话超时将是tickTime的两倍。

- dataDir
存储内存数据库快照的位置，(没有配置dataLogDir)数据库更新的事务日志。

- clientPort
侦听客户端连接的端口
```
# linux
bin/zkServer.sh start
# windows
zkServer.cmd
```

## 连接到ZooKeeper
```
# linux
$ bin/zkCli.sh -server 127.0.0.1:2181
# windows
bin/zkCli.cmd -server 127.0.0.1:2181
```
相关命令
```
ZooKeeper -server host:port cmd args
        stat path [watch]
        set path data [version]
        ls path [watch]
        delquota [-n|-b] path
        ls2 path [watch]
        setAcl path acl
        setquota -n|-b val path
        history
        redo cmdno
        printwatches on|off
        delete path [version]
        sync path
        listquota path
        rmr path
        get path [watch]
        create [-s] [-e] path data acl
        addauth scheme auth
        quit # 退出
        getAcl path
        close
        connect host:port
```
- ls 您可以尝试一些简单的命令来感受这个简单的命令行界面。首先，从发出list命令开始，如在ls中，产生：
```
[zkshell: 8] ls /
[zookeeper]
```

- create 创建一个新的znode
```
[zkshell: 9] create /zk_test my_data
Created /zk_test
```

- get 通过运行get命令验证数据是否与znode相关联，如下所示：
```
[zkshell：12] get / zk_test
my_data
cZxid = 5
ctime = Fri Jun 05 13:57:06 PDT 2009
mZxid = 5
mtime = Fri Jun 05 13:57:06 PDT 2009
pZxid = 5
cversion = 0
dataVersion = 0
aclVersion = 0
ephemeralOwner = 0
dataLength = 7
numChildren = 0
```

- set 我们可以通过发出set命令来更改与zk_test相关的数据，如下所示：
```
[zkshell：14] set / zk_test垃圾
cZxid = 5
ctime = Fri Jun 05 13:57:06 PDT 2009
mZxid = 6
mtime = Fri Jun 05 14:01:52 PDT 2009
pZxid = 5
cversion = 0
dataVersion = 1
aclVersion = 0
ephemeralOwner = 0
dataLength = 4
numChildren = 0
# （注意我们在设置数据之后做了一个get，确实确实改变了。
[zkshell：15] get / zk_test
破烂
cZxid = 5
ctime = Fri Jun 05 13:57:06 PDT 2009
mZxid = 6
mtime = Fri Jun 05 14:01:52 PDT 2009
pZxid = 5
cversion = 0
dataVersion = 1
aclVersion = 0
ephemeralOwner = 0
dataLength = 4
numChildren = 0
```

- delete 最后，让我们通过发出以下命令删除节点：
```
[zkshell：16] delete / zk_test
[zkshell：17] ls /
[动物园管理员]
[zkshell：18]
```

## 运行ZooKeeper集群
在单机模式下运行ZooKeeper便于评估，开发和测试。但在生产中，您应该以Replicated 模式运行ZooKeeper。同一应用程序中的复制服务器组称为仲裁(quorum)，在Replicated模式下，仲裁(quorum)中的所有服务器都具有相同配置文件的副本。
> 对于复制(Replicated)模式，至少需要三台服务器，强烈建议您使用奇数个服务器。如果您只有两台服务器，那么您处于这样的情况：如果其中一台服务器出现故障，则没有足够的机器来构成多数仲裁。两台服务器本质上 不如 单一服务器稳定，因为有两个单点故障。

```
tickTime=2000
dataDir=/var/lib/zookeeper
clientPort=2181
initLimit=5
syncLimit=2
server.1=zoo1:2888:3888
server.2=zoo2:2888:3888
server.3=zoo3:2888:3888
```

- TODO 集群解释

```
The new entry, initLimit is timeouts ZooKeeper uses to limit the length of time the ZooKeeper servers in quorum have to connect to a leader. The entry syncLimit limits how far out of date a server can be from a leader.

With both of these timeouts, you specify the unit of time using tickTime. In this example, the timeout for initLimit is 5 ticks at 2000 milleseconds a tick, or 10 seconds.

The entries of the form server.X list the servers that make up the ZooKeeper service. When the server starts up, it knows which server it is by looking for the file myid in the data directory. That file has the contains the server number, in ASCII.

Finally, note the two port numbers after each server name: " 2888" and "3888". Peers use the former port to connect to other peers. Such a connection is necessary so that peers can communicate, for example, to agree upon the order of updates. More specifically, a ZooKeeper server uses this port to connect followers to the leader. When a new leader arises, a follower opens a TCP connection to the leader using this port. Because the default leader election also uses TCP, we currently require another port for leader election. This is the second port in the server entry.
```
```
新条目initLimit是暂停ZooKeeper用于限制仲裁中ZooKeeper服务器连接到领导者的时间长度。条目syncLimit限制服务器与领导者的过期时间。

使用这两个超时，您可以使用tickTime指定时间 单位。在这个例子中，initLimit的超时是2000个milleseconds的5个滴答，或者是10秒。

表单server.X的条目列出了构成ZooKeeper服务的服务器。当服务器启动时，它通过在数据目录中查找文件myid来知道它是哪个服务器 。该文件包含服务器编号，ASCII格式。

最后，记下每个服务器名称后面的两个端口号：“2888”和“3888”。对等方使用以前的端口连接到其他对等方。  
这种连接是必要的，以便对等方可以进行通信，例如，就更新的顺序达成一致。更具体地说，ZooKeeper服务器使用此端口将关注者连接到领导者。当新的领导者出现时，跟随者使用此端口打开与领导者的TCP连接。  
由于默认的领导者选举也使用TCP，我们目前需要另一个端口进行领导者选举。这是服务器条目中的第二个端口。
```

> 如果要在一台计算机上测试多个服务器，请将servername指定为localhost，并为该服务器中的每个server.X 指定唯一的仲裁和领导者选举端口（即上例中的2888：3888,2889：3889,2890：3890）配置文件。当然，单独的dataDir和不同的clientPort也是必需的（在上面复制的示例中，在单个localhost上运行，您仍然会有三个配置文件）。

> 请注意，在一台计算机上设置多台服务器不会产生任何冗余。如果发生导致机器死机的事情，所有zookeeper服务器都将脱机。完全冗余要求每台服务器都有自己的机器。它必须是完全独立的物理服务器。同一物理主机上的多个虚拟机仍然容易受到该主机的完全故障的影响。

- 其他优化
还有一些其他配置参数可以大大提高性能：
要在更新时获得较低的延迟，请务必拥有专用的事务日志目录。默认情况下，事务日志与数据快照和myid文件放在同一目录中。dataLogDir参数指示用于事务日志的不同目录。
