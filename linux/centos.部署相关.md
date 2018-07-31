## CentOS yum
## [CentOS7/RHEL7安装EPEL扩展仓库步骤详解](http://blog.csdn.net/gatieme/article/details/70232358)
  - yum -y install epel-release
- yum install
- yum update
- **安装开发环境 gcc 等 yum groupinstall "Development Tools"**
- 查看是否安装 yum list installed | grep ffmpeg

## ssh 服务
1. 安装 yum list | grep ssh , yum install ssh
2. service sshd start

## ftp 服务 | ftp 客户端
1. yum 安装 vsftpd： yum install vsftpd
2. 如果需要连接其他 FTP 服务器，则可以安装 FTP 客户端。 yum install ftp
3. 创建ftp 用户adduser userftp, passwd userftp
4. ??????? 禁止 ftp用户用ssh 登陆 usermod -s /sbin/nologin userftp
5. 打开配置文件：sudo vi /etc/vsftpd/vsftpd.conf
6. 关闭匿名访问：anonymous_enable=NO
7. 去掉 local_enable 的注释Uncomment this to allow local users to log in.，修改为开启：local_enable=YES
8. ??????? 设置用户的主目录：(不设置时，默认为用户的家目录/home/userftp) local_root=/data/test
9. 重启服务：sudo service vsftpd restart
10. 设置开机自启动：chkconfig vsftpd on
11. 连接测试
```
ftp userftp@112.126.74.124
ftp> pwd
Remote directory: /home/userftp
ftp> quit
221 Goodbye.
```

# linux （centos）[镜像源修改](http://mirrors.aliyun.com/help/centos)
1. 备份 mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
2. CentOS 6 执行  curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo 或者 wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
- 之后运行yum makecache生成缓存

# 防火墙
防火墙（iptables）是一种系统服务，位于：/etc/init.d/iptables
防火墙的配置信息，保存在这个文件中：/etc/sysconfig/iptables
防火墙服务的启动，停止，重启，查询状态，保存配置等命令如下：
```
# service iptables start/stop/restart/status/save
```
### 关闭防火墙
CentOS 7、RedHat 7 之前的 Linux 发行版防火墙开启和关闭( iptables ):

即时生效，重启失效
```
#开启
service iptables start
#关闭
service iptables stop
重启生效

#开启
chkconfig iptables on
#关闭
chkconfig iptables off
```
[防火墙相关命令](https://www.cnblogs.com/moxiaoan/p/5683743.html)
CentOS 7、RedHat 7 之后的 Linux 发行版防火墙开启和关闭( firewall ):
```
systemctl stop firewalld.service
```

### 开放端口
CentOS 7、RedHat 7 之前的 Linux 发行版开放端口

```
#命令方式开放5212端口命令

#开启5212端口接收数据
/sbin/iptables -I INPUT -p tcp --dport 5212 -j ACCEPT


#开启5212端口发送数据
/sbin/iptables -I OUTPUT -p tcp --dport 5212 -j ACCEPT

#保存配置
/etc/rc.d/init.d/iptables save

#重启防火墙服务
/etc/rc.d/init.d/iptables restart

#查看是否开启成功
/etc/init.d/iptables status
```
CentOS 7、RedHat 7 之后的 Linux 发行版开放端口
```
firewall-cmd --zone=public --add-port=5121/tcp --permanent
# 查看开放端口
firewall-cmd --zone=public --list-ports
3306/tcp 6379-6389/tcp 3000-20000/tcp
# --zone 作用域
# --add-port=5121/tcp 添加端口，格式为：端口/通讯协议
# --permanent 永久生效，没有此参数重启后失效
firewall-cmd --reload
修改以后重启防火墙
删除
firewall-cmd --zone= public --remove-port=80/tcp --permanent

```

# 常用工具
  - wget, wget -h 查看帮助
    - 常用命令 wget -O {{outputfile}} {{url}}
    - 后台下载 ：-b，可以配合 -o 输出下载日志
    - 断点续传：-c
    - 限速下载：--limit-rate={{rata || 300k}}
  - curl 类似 wget 的下载工具
    - curl url -output {toDir} 下载到指定路径
  - 软件管理工具 yum,rpm > CentOS, apt-get > 乌邦图
    - [CentOS yum 源的配置与使用](https://www.cnblogs.com/mchina/archive/2013/01/04/2842275.html)
      - yum list installed | grep ^M #查询安装软件中 以 M开头的软件
      - Not using downloaded repomd.xml because it is older than what we have: 遇到这个问题的时候清理缓存yum clean all.

# linux 环境变量设置
  - 查看环境变量
    1. 使用echo命令查看单个环境变量。例如：
echo $PATH
    2. 使用env查看所有环境变量。例如：
env
    3. 使用set查看所有本地定义的环境变量。
  - 三种环境变量设置方法，**:** 用来分割两个环境变量，**$** 用来引用已经存在的环境变量
    1. 系统全局环境变量： 修改/etc/profile文件, 在末尾添加
    ```
    export PATH=$JAVA_HOME/bin:$PATH
    ```
    2. 用户环境变量： /home/{user}/.bash_profile 文件, 在末尾添加
    ```
    export PATH=$JAVA_HOME/bin:$PATH
    ```
    3. 直接在shell 里面设置
    ```
    export PATH=$JAVA_HOME/bin:$PATH
    ```      

# 部署相关环境
- java
  1. tar.gz 包
  2. tar -zxvf {tar.gz} -C {toDir}
  3. 设置环境变量 到 全局或者用户。
```
export JAVA_HOME=/usr/share/jdk1.6.0_14
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
```
更新环境变量
```
source /etc/profile
```
  4.检查安装版本
```
java -version
```
- tomcat
  - 注意给添加可执行权限
- MySQL
  - 在mysql 官网下载mysql.rpm 源，用yum install mysql.rpm 完成源的下载。然后在安装对应版本的mysql
- nginx 配置自签名证书 http://blog.csdn.net/qq_26819733/article/details/53431662
- nginx（https://www.nginx.com/resources/admin-guide/）
  - 编译源码安装

  ```
  查看版本
  [root@iZ25sabz8p5Z soft]# lsb_release -a
  LSB Version: :core-4.1-amd64:core-4.1-noarch
  Distributor ID: CentOS
  Description: CentOS Linux release 7.0.1406 (Core)
  Release:7.0.1406
  Codename: Core
  [root@iZ25sabz8p5Z soft]#
  nginx的一些模块依赖一些lib库，在安装nginx之前，须先安装这些lib库，
  依赖库主要有g++、gcc、openssl-devel、pcre-devel和zlib-devel 所以执行如下命令安装
  1. yum install gcc-c++
  2.yum install pcre pcre-devel
  3.yum install zlib zlib-devel
  4.yum install openssl openssl--devel
  5.  wget http://nginx.org/download/nginx-1.9.14.tar.gz
  6. tar xvzf nginx-1.9.14.tar.gz
  7. ./configure --with-http_ssl_module
  8.make && make install
  9. cd /usr/local/nginx/sbin
  10. ./nginx
  #也可以用yum 直接安装 但是需要创建nginx 的仓库源参考
  ```
  - [通过yum安装](http://nginx.org/en/linux_packages.html)
    1. create the file named /etc/yum.repos.d/nginx.repo with content:

    ```
    [nginx]
    name=nginx repo
    baseurl=http://nginx.org/packages/OS/OSRELEASE/$basearch/
    gpgcheck=0
    enabled=1
    ```
    Replace “OS” with “rhel” or “centos”, depending on the distribution used, and “OSRELEASE” with “6” or “7”, for 6.x or 7.x versions, respectively.
    $basearch 用	x86_64, i386 替换。
    2. yum install -y nginx
  - 如果同时运行多个 nginx 需要通过编译的方式 重新make install 到其他路径
  - 其他常用 方式 http://nginx.org/en/docs/beginners_guide.html#conf_structure
    - Serving Static Content， 静态资源
    - Setting Up a Simple Proxy Server，简单代理服务， 原理是重定向到目标地址
    - Setting Up FastCGI Proxying， FastCGI 服务器代理。FastCGI = 快速通用网关接口（Fast Common Gateway Interface／FastCGI），主要使用场景是 PHP,JSP 等动态服务器页面的代理服务

      ```
      Nging和FastCGI合作
Nginx不支持对外部程序的直接调用或者解析，
所有的外部程序（包括PHP）必须通过FastCGI接口来调用。
FastCGI接口在Linux下是socket（这个socket可以是文件socket，也可以是ip socket）。
接下来以Nginx下PHP的运行过程来说明。
PHP-FPM是管理FastCGI的一个管理器，它作为PHP的插件存在。
FastCGI进程管理器php-fpm自身初始化，
启动主进程php-fpm和启动start_servers个CGI 子进程。
主进程php-fpm主要是管理fastcgi子进程，监听9000端口。  
fastcgi子进程等待来自Web Server的连接。
当客户端请求到达Web Server Nginx是时，
Nginx通过location指令，
将所有以php为后缀的文件都交给127.0.0.1:9000来处理，
即Nginx通过location指令，将所有以php为后缀的文件都交给127.0.0.1:9000来处理。
FastCGI进程管理器PHP-FPM选择并连接到一个子进程CGI解释器。
Web server将CGI环境变量和标准输入发送到FastCGI子进程。
FastCGI子进程完成处理后将标准输出和错误信息从同一连接返回Web Server。
当FastCGI子进程关闭连接时，请求便告处理完成。
FastCGI子进程接着等待并处理来自FastCGI进程管理器（运行在 WebServer中）的下一个连接。
      ```

    - 反向代理
    - 负载均衡
- [redis](https://redis.io/download)
  1. Download, extract and compile Redis with:(下载，解压，编译)
```
$ wget http://download.redis.io/releases/redis-4.0.2.tar.gz
$ tar xzf redis-4.0.2.tar.gz
$ cd redis-4.0.2
$ make
```
注意查看 README
使用make 的时候需要 gcc 来编译
如果遇到报错信息： error: jemalloc/jemalloc.h: No such file or directory 解决方案：http://www.phperz.com/article/14/1219/42002.html，原因是默认分配器是jemalloc，如果没有就会报错，这是个时候需要make MALLOC=libc
建议使用 make V=1 > &make.log& 保存编译信息，同理 make install V=1 > &make_install.log&
如果要安装到 某个路径 make PREFIX={/usr/redis} install V=1 > make_install.log
如果出现编译异常，可以查看 解压目录中的 README.txt cd deps
make hiredis jemalloc linenoise lua geohash-int
  2. The binaries that are now compiled are available in the src directory. Run Redis with:（开启redis服务）
```
$ src/redis-server
```
  3. You can interact with Redis using the built-in client:（使用客户端访问）
```
$ src/redis-cli
redis> set foo bar
OK
redis> get foo
"bar"
```
  4. 配置
```
# 后台开启
daemonize yes
# 绑定ip
bind 127.0.0.1 或者 bind 120.25.158.242
# 绑定端口
port 6379
# pid 文件的位置
pidfile /var/run/redis/redis_6379.pid
# 日志 文件的位置
logfile /var/log/redis/redis_6379.log
# A reasonable value for this option is 300 seconds, which is the new
# Redis default starting with Redis 3.2.1.
tcp-keepalive 300
# The filename where to dump the DB
dbfilename dump_6381.rdb
# Note that you must specify a directory here, not a file name.
dir /var/lib/redis/
# Require clients to issue AUTH <PASSWORD> before processing any other，
# Warning: since Redis is pretty fast an outside user can try up to 150k passwords per second   against a good box. This means that you should use a very strong password otherwise it will be   very easy to break.
#密码，建议设置为复杂的密码
requirepass Lt^-^2016
# 缓存最大值
maxmemory 1024mb
```
  5. 启动/停止/重启
    - redis-server {redis.conf}
    - 客户端关闭 redis-cli -h 127.0.0.1 -p 6379 -a myRedis shutdown
  6. 客户端连接 redis-cli -h 127.0.0.1 -p 6379 -a myRedis
  7. 可以复制 utils/redis_init.script 到 /etc/init.d/redis_6379 并修改配置，可以实现 start/stop 启动/关闭 redis。[quick start](https://redis.io/topics/quickstart)
  8. redis-cli 客户端命令
    - info redis相关信息
  9. 查看redis 版本redis-server --version，redis-cli 同理
  
  可视化工具 Redis Desktop Manager windows
- mongodb
- nodejs
  - [使用包管理工具安装](https://nodejs.org/en/download/package-manager/)
  - 或者简单使用 yum -y install nodejs
- rsync
