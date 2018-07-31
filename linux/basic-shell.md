## man 命令来查看某个命令的详细使用方法，某些命令也可以使用--hlep 来查看。

## linux 名称是 大小写敏感的 所以针对文件名，文件夹名，软件包名，都需要严格的区分大小写

## linux 文件系统标准 [FHS](http://www.pathname.com/fhs/pub/fhs-2.3.html#INTRODUCTION)
    - [/opt,/usr/local 区别](http://blog.csdn.net/aqxin/article/details/48324377)
    - /usr：系统级的目录，可以理解为C:/Windows/，/usr/lib理解为C:/Windows/System32。
    - /usr/local：用户级的程序目录，可以理解为C:/Progrem Files/。用户自己编译的软件默认会安装到这个目录下。
    - /opt：用户级的程序目录，可以理解为D:/Software，opt有可选的意思，这里可以用于放置第三方大型软件（或游戏），当你不需要时，直接rm -rf掉即可。在硬盘容量不够时，也可将/opt单独挂载到其他磁盘上使用。
## 多使用man {{cmd}} ,{{cmd}} --help 来查看使用命令

## shell 脚本可以随意命名，但是通常用.sh来表示脚本，需要给文件加上可执行权限，也可以在文件头 #!/bin/bash 来指定使用那个 shell 终端
```
#!/bin/bash
echo "当前脚本名称为$0"
echo "总共有$#个参数，分别是$*。"
echo "第1个参数为$1，第5个为$5。"
```
```
linux中shell变量$#,$@,$0,$1,$2的含义解释:
变量说明:
$$
Shell本身的PID（ProcessID）
$!
Shell最后运行的后台Process的PID
$?
最后运行的命令的结束代码（返回值）
$-
使用Set命令设定的Flag一览
$*
所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。
$@
所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。
$#
添加到Shell的参数个数
$0
Shell本身的文件名
$1～$n
添加到Shell的各参数值。$1是第1参数、$2是第2参数…。
```
1. 条件判断
  - 文件测试语句；
  - 逻辑测试语句；
  - 整数值比较语句；
  - 字符串比较语句。

```
  -d 	测试文件是否为目录类型
  -e 	测试文件是否存在
  -f 	判断是否为一般文件
  -r 	测试当前用户是否有权限读取
  -w 	测试当前用户是否有权限写入
  -x 	测试当前用户是否有权限执行
```

```
操作符 	作用
-eq 	是否等于
-ne 	是否不等于
-gt 	是否大于
-lt 	是否小于
-le 	是否等于或小于
-ge 	是否大于或等于
```

```
= 	比较字符串内容是否相同
!= 	比较字符串内容是否不同
-z 	判断字符串内容是否为空
```

2. 循环
  - while
    ```
    #!/bin/bash
    PRICE=$(expr $RANDOM % 1000)
    TIMES=0
    echo "商品实际价格为0-999之间，猜猜看是多少？"
    while true
    do
    read -p "请输入您猜测的价格数目：" INT
    let TIMES++
    if [ $INT -eq $PRICE ] ; then
    echo "恭喜您答对了，实际价格是 $PRICE"
    echo "您总共猜测了 $TIMES 次"
    exit 0
    elif [ $INT -gt $PRICE ] ; then
    echo "太高了！"
    else
    echo "太低了！"
    fi
    done
    ```
  - for
    ```
    #!/bin/bash
    read -p "Enter The Users Password : " PASSWD
    for UNAME in `cat users.txt`
    do
    id $UNAME &> /dev/null
    if [ $? -eq 0 ]
    then
    echo "Already exists"
    else
    useradd $UNAME &> /dev/null
    echo "$PASSWD" | passwd --stdin $UNAME &> /dev/null
    if [ $? -eq 0 ]
    then
    echo "$UNAME , Create success"
    else
    echo "$UNAME , Create failure"
    fi
    fi
    done
    ```
3. case
  ```
  #!/bin/bash
  read -p "请输入一个字符，并按Enter键确认：" KEY
  case "$KEY" in
  [a-z]|[A-Z])
  echo "您输入的是 字母。"
  ;;
  [0-9])
  echo "您输入的是 数字。"
  ;;
  *)
  echo "您输入的是 空格、功能键或其他控制字符。"
  esac
  [root@linuxprobe ~]# bash Checkkeys.sh
  请输入一个字符，并按Enter键确认：6
  您输入的是 数字。
  [root@linuxprobe ~]# bash Checkkeys.sh
  请输入一个字符，并按Enter键确认：p
  您输入的是 字母。
  [root@linuxprobe ~]# bash Checkkeys.sh
  请输入一个字符，并按Enter键确认：^[[15~
  您输入的是 空格、功能键或其他控制字符。
  ```
4. if then fi; if then else fi;if then elif then else fi
```
if [ $GRADE -ge 85 ] && [ $GRADE -le 100 ] ; then
echo "$GRADE is Excellent"
elif [ $GRADE -ge 70 ] && [ $GRADE -le 84 ] ; then
echo "$GRADE is Pass"
else
echo "$GRADE is Fail"
fi
```

5. 定时任务 crontab ||  cron


## 修改开机启动
  - 命令行形式centos 6 及以前，
    - su 到root用户
    - vim /etc/inittab ,修改 id:5:default -> id:3:default;
    - 涉及到 linux 系统运行级别 0-6，具体可以参考 inittab 里面的内容
  - 修改开机启动 命令行形式centos 7 及之后的
    - su 到root用户
    - ln -sf /lib/systemd/system/<target name>.target /etc/systemd/system/default.target
    - 启动命令行形式ln -sf /lib/systemd/system/multi-user.target /etc/systemd/system/default.target

## centos 7 和 centos 7 之前的系统有很多不一样。
  - ip addr(需要修改onboot = yes) / ifconfig
    - centOS7
      1. vi /etc/sysconfig/network-scripts/ifcfg-{{网卡名称}}
      2. ONBOOT=yes
      3. service network restart
      4. ip addr

## centos 版本查看
  - lsb_release -a
  - cat /proc/version
  - cat /etc/redhat-release | cat /etc/centos-release

## 管道符、重定向与环境变量

- 输入重定向中用到的符号及其作用

|符号 |	作用|
|-----|-----|
|命令 < 文件| 	将文件作为命令的标准输入|
|命令 << 分界符 |	从标准输入中读入，直到遇见分界符才停止|
|命令 < 文件1 > 文件2 |	将文件1作为命令的标准输入并将标准输出到文件2|

- 输出重定向中用到的符号及其作用

|符号 |	作用|
|-----|-----|
|命令 > 文件 |	将标准输出重定向到一个文件中（清空原有文件的数据）|
|命令 2> 文件| 	将错误输出重定向到一个文件中（清空原有文件的数据）|
|命令 >> 文件 |	将标准输出重定向到一个文件中（追加到原有内容的后面）
|命令 2>> 文件 |	将错误输出重定向到一个文件中（追加到原有内容的后面）|
|命令 >> 文件 2>&1 或 命令 &>> 文件 |将标准输出与错误输出共同写入到文件中（追加到原有内容的后面）

- 标准输入重定向（STDIN，文件描述符为0）：默认从键盘输入，也可从其他文件或命令中输入。
- 标准输出重定向（STDOUT，文件描述符为1）：默认输出到屏幕。
- 错误输出重定向（STDERR，文件描述符为2）：默认输出到屏幕。
- 管道命令符 " | "
    - ps -ef|grep tomcat
    - 在修改用户密码时，通常都需要输入两次密码以进行确认，这在编写自动化脚本时将成为一个非常致命的缺陷。通过把管道符和passwd命令的--stdin参数相结合，我们可以用一条命令来完成密码重置操作：
    ```
    [root@linuxprobe ~]# echo "linuxprobe" | passwd --stdin root
    Changing password for user root.
    passwd: all authentication tokens updated successfully.
    ```

## [Linux中的正则表达式](http://blog.csdn.net/renwotao2009/article/details/50937038)

## 执行命令
- (1) 用绝对路径或相对路径执行的命令{{fullpath}}/{{cmd}}, ./{{cmd}}
- (2) 别名对应命令
- (3) Bash内部命令
- (4) 按照$PATH环境变量定义的目录查找顺序找到的第一个命令

## 别名 alias| unalias，只在当前 shell 终端生效，可以配置在 ~/.bash_profile 里。
- alias -p 查看所有别名
- alias  {{aliasName}}={{cmd}} 设置别名
- unalias {{aliasName}} 删除别名

## 命令通配
- 匹配多个字符 ps -ef| grep tom*
- 匹配单个字符 ls -l /dev/sda?

## 常用的转义字符
- 反斜杠（\\）：使反斜杠后面的一个变量变为单纯的字符串。
- 单引号（''）：转义其中所有的变量为单纯的字符串。
- 双引号（""）：保留其中的变量属性，不进行转义处理。
- 反引号（\`\`）：把其中的命令执行后返回结果。

## 重要的环境变量
Linux系统中最重要的10个环境变量

|变量名称 |	作用|
|---------|-----|
|HOME |	用户的主目录（即家目录）|
|SHELL |	用户在使用的Shell解释器名称|
|HISTSIZE |	输出的历史命令记录条数|
|HISTFILESIZE |	保存的历史命令记录条数|
|LANG |	系统语言、语系名称|
|MAIL |	邮件保存路径|
|RANDOM |	生成一个随机数字|
|PS1 |	Bash解释器的提示符|
|PATH |	定义解释器搜索用户执行命令的路径|
|EDITOR |	用户默认的文本编辑器|

## linux 环境变量设置
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
    2. /etc/bashrc, 为每个bash shell用户 执行
    3. ~ 表示 HOME环境变量的值，可以使用echo $HMOE 查看用户环境变量：  ~/.bash_profile 例如：/home/{user}/.bash_profile 文件, 在末尾添加
    ```
    export PATH=$JAVA_HOME/bin:$PATH
    ```
    3. 直接在shell 里面设置
    ```
    export PATH=$JAVA_HOME/bin:$PATH
    ```

## 文件管理
  - file 查看文件类型
  - [touch](https://linux.cn/article-2740-1.html),创建文件，或者修改文件时间戳。
  - mkdir
    - mkdir -p /home/{{tobeCreatedPath}}
  - stat {{file || folder}}
  - ls 查看当前目录文件以及文件夹
    - 常用参数 -l, -la(list形式显示所有文件以及文件夹)
    - ls -lah
    - ls -u -l 按名称排序
    - ls -u -lt 按访问时间排序
  - 复制文件或者文件夹  
    - cp ${source} ${target}
    - cp -r {{sourcePath}} {{targetPath}} 递归处理，将指定目录下的文件与子目录一并处理。若源文件或目录的形态，不属于目录或符号链接，则一律视为普通文件处理
        - cp -r source ./source2 ,将source 复制一份在当前文件夹 命名为source2
        - cp -r source ./source2/,将source 复制一份在source2 文件夹下
    - -f --force
  - 创建全路径，mkdir -p ${path}  
  - 移动文件|文件夹，也可以实现重命名
    - mv ${sourcePath} ${moveInToTargetPath}
  - 删除文件或文件夹
    - rm -r ${path}
    - rm -f 强制删除不用提示
    - rm -f /usr/local/bin/redis* 删除以redis 开头的 文件
  - 清空文件
    - $ > filename
  - 端口占用
    - $ netstat   -anp   |   grep  portno
  - 分割文件
    - $ split -l 1000000 catalina.out.filepart
    ```
    功能说明：切割文件。  
    语　　法：split [--help][--version][-<行数>][-b <字节>][-C <字节>][-l <行数>][要切割的文件][输出文件名]
    补充说明：split可将文件切成较小的文件，预设每1000行会切成一个小文件。  
    参　　数：  
    -<行数>或-l<行数> 　指定每多少行就要切成一个小文件。  
    -b<字节> 　指定每多少字就要切成一个小文件。支持单位:m,k  
    -C<字节> 　与-b参数类似，但切割时尽量维持每行的完整性。  
    --help 　显示帮助。  
    --version 　显示版本信息。  
    [输出文件名] 　设置切割后文件的前置文件名，split会自动在前置文件名后再加上编号。  
    使用例子：  
    split -b 100m 1111.log (按照字节分隔)  
    split -l 1000000 1111.log(按照行数分隔)  
    ```
  - **文件权限**

|isFile | user |group  | other |
|-------|-----|------|-------|
|0 | 1-3 | 4-6 | 7-9  |
  - chmod 777 -R bin   递归给/bin中的所有文件添加所有用户可执行权限  
  - chmod a|u|g|o +x -R /bin
  - chmod u+x,g+w f01　　# 为文件f01设置自己可以执行，组员可以写入的权限
  - chmod u=rwx,g=rw,o=r f01
  - chmod 764 f01
  - chmod a+x f01　　    # 对文件f01的u,g,o都设置可执行属性
  - chmod u+r-w-x # 赋予用户可读，不可写，不可执行权限
  - 文件类型

|文件类型|描述|
|----|---|
|普通文件 |	权限的10个字符中的第一位是“-"的文件|
|目录文件 |	权限的10个字符中的第一位是"d"的文件|
|硬链接文件 |	除了显示的文件数量，其他都和某个普通文件一模一样的文件|
|软链接文件 |	权限的10个字符中的第一位是“l"的文件|
|块设备文件 |	权限的10个字符中的第一位是“b"的文件|
|socket文件 |	权限的10个字符中的第一位是“s"的文件|
|字符设备文件 |	权限的10个字符中的第一位是“c"的文件|
|管道文件 |	权限的10个字符中的第一位是“p"的文件|
|setUid可执行文件 |	权限的10个字符中的第四位是“s"的文件|
|setGid可执行文件 |	权限的10个字符中的第七位是“s"的文件|
|setUid加setGid文件 |	权限的10个字符中的第四位和第七位都是“l"的文件|

- 特殊权限

```
    在复杂多变的生产环境中，单纯设置文件的rwx权限无法满足我们对安全和灵活性的需求，因此便有了SUID、SGID与SBIT的特殊权限位。这是一种对文件权限进行设置的特殊功能，可以与一般权限同时使用，以弥补一般权限不能实现的功能。下面具体解释这3个特殊权限位的功能以及用法。

1.  SUID

SUID是一种对二进制程序进行设置的特殊权限，可以让二进制程序的执行者临时拥有属主的权限（仅对拥有执行权限的二进制程序有效）。例如，所有用户都可以执行passwd命令来修改自己的用户密码，而用户密码保存在/etc/shadow文件中。仔细查看这个文件就会发现它的默认权限是000，也就是说除了root管理员以外，所有用户都没有查看或编辑该文件的权限。但是，在使用passwd命令时如果加上SUID特殊权限位，就可让普通用户临时获得程序所有者的身份，把变更的密码信息写入到shadow文件中。这很像我们在古装剧中见到的手持尚方宝剑的钦差大臣，他手持的尚方宝剑代表的是皇上的权威，因此可以惩戒贪官，但这并不意味着他永久成为了皇上。因此这只是一种有条件的、临时的特殊权限授权方法。

查看passwd命令属性时发现所有者的权限由rwx变成了rws，其中x改变成s就意味着该文件被赋予了SUID权限。另外有读者会好奇，那么如果原本的权限是rw-呢？如果原先权限位上没有x执行权限，那么被赋予特殊权限后将变成大写的S。

[root@linuxprobe ~]# ls -l /etc/shadow
----------. 1 root root 1004 Jan 3 06:23 /etc/shadow
[root@linuxprobe ~]# ls -l /bin/passwd
-rwsr-xr-x. 1 root root 27832 Jan 29 2017 /bin/passwd

2.  SGID

SGID主要实现如下两种功能：

    让执行者临时拥有属组的权限（对拥有执行权限的二进制程序进行设置）；

    在某个目录中创建的文件自动继承该目录的用户组（只可以对目录进行设置）。

SGID的第一种功能是参考SUID而设计的，不同点在于执行程序的用户获取的不再是文件所有者的临时权限，而是获取到文件所属组的权限。举例来说，在早期的Linux系统中，/dev/kmem是一个字符设备文件，用于存储内核程序要访问的数据，权限为：

    cr--r-----   1 root system 2,  1 Feb 11 2017  kmem

大家看出问题了吗？除了root管理员或属于system组成员外，所有用户都没有读取该文件的权限。由于在平时我们需要查看系统的进程状态，为了能够获取到进程的状态信息，可在用于查看系统进程状态的ps命令文件上增加SGID特殊权限位。查看ps命令文件的属性信息：

    -r-xr-sr-x   1 bin system 59346 Feb 11 2017  ps

这样一来，由于ps命令被增加了SGID特殊权限位，所以当用户执行该命令时，也就临时获取到了system用户组的权限，从而可以顺利地读取设备文件了。

前文提到，每个文件都有其归属的所有者和所属组，当创建或传送一个文件后，这个文件就会自动归属于执行这个操作的用户（即该用户是文件的所有者）。如果现在需要在一个部门内设置共享目录，让部门内的所有人员都能够读取目录中的内容，那么就可以创建部门共享目录后，在该目录上设置SGID特殊权限位。这样，部门内的任何人员在里面创建的任何文件都会归属于该目录的所属组，而不再是自己的基本用户组。此时，我们用到的就是SGID的第二个功能，即在某个目录中创建的文件自动继承该目录的用户组（只可以对目录进行设置）。

[root@linuxprobe ~]# cd /tmp
[root@linuxprobe tmp]# mkdir testdir
[root@linuxprobe tmp]# ls -ald testdir/
drwxr-xr-x. 2 root root 6 Feb 11 11:50 testdir/
[root@linuxprobe tmp]# chmod -Rf 777 testdir/
[root@linuxprobe tmp]# chmod -Rf g+s testdir/
[root@linuxprobe tmp]# ls -ald testdir/
drwxrwsrwx. 2 root root 6 Feb 11 11:50 testdir/

在使用上述命令设置好目录的777权限（确保普通用户可以向其中写入文件），并为该目录设置了SGID特殊权限位后，就可以切换至一个普通用户，然后尝试在该目录中创建文件，并查看新创建的文件是否会继承新创建的文件所在的目录的所属组名称：

[root@linuxprobe tmp]# su - linuxprobe
Last login: Wed Feb 11 11:49:16 CST 2017 on pts/0
[linuxprobe@linuxprobe ~]$ cd /tmp/testdir/
[linuxprobe@linuxprobe testdir]$ echo "linuxprobe.com" > test
[linuxprobe@linuxprobe testdir]$ ls -al test
-rw-rw-r--. 1 linuxprobe root 15 Feb 11 11:50 test

除了上面提到的SGID的这两个功能，我们再介绍两个与本小节内容相关的命令：chmod和chown。

chmod命令是一个非常实用的命令，能够用来设置文件或目录的权限，格式为“chmod [参数] 权限 文件或目录名称”。如果要把一个文件的权限设置成其所有者可读可写可执行、所属组可读可写、其他人没有任何权限，则相应的字符法表示为rwxrw----，其对应的数字法表示为760。通过前面的基础学习和当前的练习实践，现在大家可以感受到使用数字法来设置文件权限的便捷性了吧。

[root@linuxprobe ~]# ls -al test
-rw-rw-r--. 1 linuxprobe root 15 Feb 11 11:50 test
[root@linuxprobe ~]# chmod 760 test
[root@linuxprobe ~]# ls -l test
-rwxrw----. 1 linuxprobe root 15 Feb 11 11:50 test

除了设置文件或目录的权限外，还可以设置文件或目录的所有者和所属组，这里使用的命令为chown，其格式为“chown [参数] 所有者:所属组 文件或目录名称”。

chmod和chown命令是用于修改文件属性和权限的最常用命令，它们还有一个特别的共性，就是针对目录进行操作时需要加上大写参数-R来表示递归操作，即对目录内所有的文件进行整体操作。

[root@linuxprobe ~]# ls -l test
-rwxrw----. 1 linuxprobe root 15 Feb 11 11:50 test
[root@linuxprobe ~]# chown root:bin test
[root@linuxprobe ~]# ls -l test
-rwxrw----. 1 root bin 15 Feb 11 11:50 test

3.  SBIT

现在，大学里的很多老师都要求学生将作业上传到服务器的特定共享目录中，但总是有几个“破坏分子”喜欢删除其他同学的作业，这时就要设置SBIT（Sticky Bit）特殊权限位了（也可以称之为特殊权限位之粘滞位）。SBIT特殊权限位可确保用户只能删除自己的文件，而不能删除其他用户的文件。换句话说，当对某个目录设置了SBIT粘滞位权限后，那么该目录中的文件就只能被其所有者执行删除操作了。

最初不知道是哪位非资深技术人员将Sticky Bit直译成了“粘滞位”，刘遄老师建议将其称为“保护位”，这既好记，又能立刻让人了解它的作用。RHEL 7系统中的/tmp作为一个共享文件的目录，默认已经设置了SBIT特殊权限位，因此除非是该目录的所有者，否则无法删除这里面的文件。

与前面所讲的SUID和SGID权限显示方法不同，当目录被设置SBIT特殊权限位后，文件的其他人权限部分的x执行权限就会被替换成t或者T，原本有x执行权限则会写成t，原本没有x执行权限则会被写成T。

[root@linuxprobe tmp]# su - linuxprobe
Last login: Wed Feb 11 12:41:20 CST 2017 on pts/0
[linuxprobe@linuxprobe tmp]$ ls -ald /tmp
drwxrwxrwt. 17 root root 4096 Feb 11 13:03 /tmp
[linuxprobe@linuxprobe ~]$ cd /tmp
[linuxprobe@linuxprobe tmp]$ ls -ald
drwxrwxrwt. 17 root root 4096 Feb 11 13:03 .
[linuxprobe@linuxprobe tmp]$ echo "Welcome to linuxprobe.com" > test
[linuxprobe@linuxprobe tmp]$ chmod 777 test
[linuxprobe@linuxprobe tmp]$ ls -al test
-rwxrwxrwx. 1 linuxprobe linuxprobe 10 Feb 11 12:59 test

其实，文件能否被删除并不取决于自身的权限，而是看其所在目录是否有写入权限（其原理会在下个章节讲到）。为了避免现在很多读者不放心，所以上面的命令还是赋予了这个test文件最大的777权限（rwxrwxrwx）。我们切换到另外一个普通用户，然后尝试删除这个其他人创建的文件就会发现，即便读、写、执行权限全开，但是由于SBIT特殊权限位的缘故，依然无法删除该文件：

[root@linuxprobe tmp]# su - blackshield
Last login: Wed Feb 11 12:41:29 CST 2017 on pts/1
[blackshield@linuxprobe ~]$ cd /tmp
[blackshield@linuxprobe tmp]$ rm -f test
rm: cannot remove ‘test’: Operation not permitted

当然，要是也想对其他目录来设置SBIT特殊权限位，用chmod命令就可以了。对应的参数o+t代表设置SBIT粘滞位权限：

[blackshield@linuxprobe tmp]$ exit
Logout
[root@linuxprobe tmp]# cd ~
[root@linuxprobe ~]# mkdir linux
[root@linuxprobe ~]# chmod -R o+t linux/
[root@linuxprobe ~]# ls -ld linux/
drwxr-xr-t. 2 root root 6 Feb 11 19:34 linux/
```

- 隐藏权限
    ```
    Linux系统中的文件除了具备一般权限和特殊权限之外，还有一种隐藏权限，即被隐藏起来的权限，默认情况下不能直接被用户发觉。有用户曾经在生产环境和RHCE考试题目中碰到过明明权限充足但却无法删除某个文件的情况，或者仅能在日志文件中追加内容而不能修改或删除内容，这在一定程度上阻止了黑客篡改系统日志的图谋，因此这种“奇怪”的文件也保障了Linux系统的安全性。

    1.  chattr命令

    chattr命令用于设置文件的隐藏权限，格式为“chattr [参数] 文件”。如果想要把某个隐藏功能添加到文件上，则需要在命令后面追加“+参数”，如果想要把某个隐藏功能移出文件，则需要追加“-参数”。chattr命令中可供选择的隐藏权限参数非常丰富，具体如表5-6所示。

    表5-6                                  chattr命令中用于隐藏权限的参数及其作用
    参数 	作用
    i 	无法对文件进行修改；若对目录设置了该参数，则仅能修改其中的子文件内容而不能新建或删除文件
    a 	仅允许补充（追加）内容，无法覆盖/删除内容（Append Only）
    S 	文件内容在变更后立即同步到硬盘（sync）
    s 	彻底从硬盘中删除，不可恢复（用0填充原文件所在硬盘区域）
    A 	不再修改这个文件或目录的最后访问时间（atime）
    b 	不再修改文件或目录的存取时间
    D 	检查压缩文件中的错误
    d 	使用dump命令备份时忽略本文件/目录
    c 	默认将文件或目录进行压缩
    u 	当删除该文件后依然保留其在硬盘中的数据，方便日后恢复
    t 	让文件系统支持尾部合并（tail-merging）
    x 	可以直接访问压缩文件中的内容

    为了让读者能够更好地见识隐藏权限的效果，我们先来创建一个普通文件，然后立即尝试删除（这个操作肯定会成功）：

    [root@linuxprobe ~]# echo "for Test" > linuxprobe
    [root@linuxprobe ~]# rm linuxprobe
    rm: remove regular file ‘linuxprobe’? y

    实践是检验真理的唯一标准。如果您没有亲眼见证过隐藏权限强大功能的美妙，就一定不会相信原来Linux系统会如此安全。接下来我们再次新建一个普通文件，并为其设置不允许删除与覆盖（+a参数）权限，然后再尝试将这个文件删除：

    [root@linuxprobe ~]# echo "for Test" > linuxprobe
    [root@linuxprobe ~]# chattr +a linuxprobe
    [root@linuxprobe ~]# rm linuxprobe
    rm: remove regular file ‘linuxprobe’? y
    rm: cannot remove ‘linuxprobe’: Operation not permitted

    可见，上述操作失败了。

    2.  lsattr命令

    lsattr命令用于显示文件的隐藏权限，格式为“lsattr [参数] 文件”。在Linux系统中，文件的隐藏权限必须使用lsattr命令来查看，平时使用的ls之类的命令则看不出端倪：

    [root@linuxprobe ~]# ls -al linuxprobe
    -rw-r--r--. 1 root root 9 Feb 12 11:42 linuxprobe

    一旦使用lsattr命令后，文件上被赋予的隐藏权限马上就会原形毕露。此时可以按照显示的隐藏权限的类型（字母），使用chattr命令将其去掉：

    [root@linuxprobe ~]# lsattr linuxprobe
    -----a---------- linuxprobe
    [root@linuxprobe ~]# chattr -a linuxprobe
    [root@linuxprobe ~]# lsattr linuxprobe
    ---------------- linuxprobe
    [root@linuxprobe ~]# rm linuxprobe
    rm: remove regular file ‘linuxprobe’? y

    ```
- 文件或文件夹针对某个用户的权限
    - setfacl
    - getfacl



## vim 操作
三种模式 命令 查看 编辑
- 命令模式
	- 查找 /{word}
	- 翻页 ctrl + f(forward) ctrl + b(backword)
	- i 进入编辑模式
  - **u** **撤销**
- 查看模式
- 编辑模式
  - 在命令模式 直接 按 a i o 键 进入编辑模式
  - 在编辑模式 按 ESC 返回命令模式

- Vim中常用的命令

|命令 |	作用|
|-----|----|
|dd 	|删除（剪切）光标所在整行|
|5dd |	删除（剪切）从光标处开始的5行|
|yy |	复制光标所在整行|
|5yy |	复制从光标处开始的5行|
|n |	显示搜索命令定位到的下一个字符串|
|N |	显示搜索命令定位到的上一个字符串|
|u |	撤销上一步的操作|
|p |	将之前删除（dd）或复制（yy）过的数据粘贴到光标后面|

- 末行模式中可用的命令

|命令 |	作用|
|-----|----|
|:w |	保存|
|:q |	退出|
|:q! |	强制退出（放弃对文档的修改内容）|
|:wq! |	强制保存退出|
|:set nu | 	显示行号|
|:set nonu | 	不显示行号|
|:命令 |	执行该命令|
|:整数 |	跳转到该行|
|:s/one/two |	将当前光标所在行的第一个one替换成two|
|:s/one/two/g |	将当前光标所在行的所有one替换成two|
|:%s/one/two/g |	将全文中的所有one替换成two|
|?字符串 |	在文本中从下至上搜索该字符串|
|/字符串 	| 在文本中从上至下搜索该字符串|

## 查看文件系统类型
lsblk
[root@iZ94ja1ajbkZ ~]# lsblk -f
NAME    FSTYPE LABEL UUID                                 MOUNTPOINT
xvda
└─xvda1 ext4         94e4e384-0ace-437f-bc96-057dd64f42ee /
xvdb
└─xvdb1 ext3         e8b6cad6-d3a3-4c4e-a07f-7311ad843a07 /mnt

# 文件夹大小
http://www.cnblogs.com/iconfig/p/4863063.html

# fdisk -l 查看 manipulate disk partition table
#  df 查看挂载情况 df -h
- df [OPTION]... [FILE]... file system disk space usage,查看系统磁盘使用，挂载情况，传入文件夹路径可以看文件夹的使用情况
- df -h
	- 按gb 查看
- df -m
	- 按mb 查看
- df -k
	- 按kb 查看
- du --max-depth={{num}} -h {{path}}
  - 查看目录下第num层的文件及文件夹大小
- tail -f(follow) 持续输出文件末尾
- ln 创建快捷方式
  - -s 软连接 无则为硬链接，文件实时同步
  - 实例 ln -s {{from}} {{to}}, 不需要创建{{to}}的文件夹或文件
  - 删除软连接 rm -r ./{{ln}}，这里需要**特别注意**，需要rm -r  ./{{ln}},文件夹后不要带**/** ,rm -r  ./{{ln}}，安全起见，不带f参数
- ls -la 可以查看 连接的来源

# 查询内存状况
- free -[-b,-k,-m,-g] 按b,kb,mb,gb 查看内存状况
- -/+ buffers/cache:         9371      22735
    - + buffers/cache = cached + buffers + free
    - - buffers/cache = used - (cached + buffers)

```
free -m
                total       used       free     shared    buffers     cached
Mem:            32106      30824       1282      0        536      20916
-/+ buffers/cache:         9371      22735
Swap:            0          0          0
```

- 高版本linux 可以使用 free -h, used 表示使用的 内存
```
                total        used        free      shared  buff/cache   available
Mem:           5.6G        508M        3.5G        8.6M        1.5G        4.8G
Swap:          5.7G          0B        5.7G
```

# [tar 命令总结](https://www.cnblogs.com/zhenghaonihao/p/6100657.html)
- 解压 tar.gz  
    - tar -zxvf ${gzFile} -C ${toWhichFolder}
- 解压 tar.xz 成tar 文件  
    - tar -xvf ${xzFile} -C ${toWhichFolder}
- 创建压缩文件
    - tar zcvf
- zip | unzip
- zip -r ${outputPath} **${input} ${input}...**
- unzip ${zipfilePath} -d {outputPath}
- unzip -o 覆盖安装

## find 查找
- find ${path} -name ${name}
## 在文本中执行关键词搜索 过滤操作
- 文本过滤 grep {{text}} {{file}}
    - grep text /home/logfile.log;
- 过滤输出
    - ps -ef|grep tomcat
    - ls -la|grep filename

## [用户管理/组管理(user, group)](http://blog.csdn.net/guoxingege/article/details/50817459)
- 用户管理的意义

- id 查看用户信息
    - id root
    ```
    bash-4.2$ id guest_hello
    uid=1004(guest_hello) gid=1004(guest_hello) 组=1004(guest_hello)
    ```

```
管理员UID为0：系统的管理员用户。
系统用户UID为1～999： Linux系统为了避免因某个服务程序出现漏洞而被黑客提权至整台服务器，默认服务程序会有独立的系统用户负责运行，进而有效控制被破坏范围。

普通用户UID从1000开始：是由管理员创建的用于日常工作的用户。
```
- useradd，创建用户
    ```

    下面我们创建一个普通用户并指定家目录的路径、用户的UID以及Shell解释器。在下面的命令中，请注意/sbin/nologin，它是终端解释器中的一员，与Bash解释器有着天壤之别。一旦用户的解释器被设置为nologin，则代表该用户不能登录到系统中：
    参数	作用
    -d	指定用户的家目录（默认为/home/username）
    -e	账户的到期时间，格式为YYYY-MM-DD.
    -u	指定该用户的默认UID
    -g	指定一个初始的用户基本组（必须已存在）
    -G	指定一个或多个扩展用户组
    -N	不创建与用户同名的基本用户组
    -s	指定该用户的默认Shell解释器

    [root@linuxprobe ~]# useradd -d /home/linux -u 8888 -s /sbin/nologin linuxprobe
    [root@linuxprobe ~]# id linuxprobe
    uid=8888(linuxprobe) gid=8888(linuxprobe) groups=8888(linuxprobe)
    ```
- passwd 修改用户密码，

    ```
    passwd命令用于修改用户密码、过期时间、认证信息等，格式为“passwd [选项] [用户名]”。

    普通用户只能使用passwd命令修改自身的系统密码，而root管理员则有权限修改其他所有人的密码。更酷的是，root管理员在Linux系统中修改自己或他人的密码时不需要验证旧密码，这一点特别方便。既然root管理员可以修改其他用户的密码，就表示完全拥有该用户的管理权限。passwd命令中可用的参数以及作用如表5-3所示。

    表5-3                                           passwd命令中的参数以及作用

    参数	作用
    -l	锁定用户，禁止其登录
    -u	解除锁定，允许用户登录
    --stdin	允许通过标准输入修改用户密码，如echo "NewPassWord" | passwd --stdin Username
    -d	使该用户可用空密码登录系统
    -e	强制用户在下次登录时修改密码
    -S	显示用户的密码是否被锁定，以及密码所采用的加密算法名称
    接下来刘遄老师将演示如何修改用户自己的密码，以及如何修改其他人的密码（修改他人密码时，需要具有root管理员权限）：

    [root@linuxprobe ~]# passwd
    Changing password for user root.
    New password:此处输入密码值
    Retype new password: 再次输入进行确认
    passwd: all authentication tokens updated successfully.
    [root@linuxprobe ~]# passwd linuxprobe
    Changing password for user linuxprobe.
    New password:此处输入密码值
    Retype new password: 再次输入进行确认
    passwd: all authentication tokens updated successfully.
    假设您有位同事正在度假，而且假期很长，那么可以使用passwd命令禁止该用户登录系统，等假期结束回归工作岗位时，再使用该命令允许用户登录系统，而不是将其删除。这样既保证了这段时间内系统的安全，也避免了频繁添加、删除用户带来的麻烦：

    [root@linuxprobe ~]# passwd -l linuxprobe
    Locking password for user linuxprobe.
    passwd: Success
    [root@linuxprobe ~]# passwd -S linuxprobe
    linuxprobe LK 2017-12-26 0 99999 7 -1 (Password locked.)
    [root@linuxprobe ~]# passwd -u linuxprobe
    Unlocking password for user linuxprobe.
    passwd: Success
    [root@linuxprobe ~]# passwd -S linuxprobe
    linuxprobe PS 2017-12-26 0 99999 7 -1 (Password set, SHA512 crypt.)
    ```
- usermod

```
usermod命令用于修改用户的属性，格式为“usermod [选项] 用户名”。

前文曾反复强调，Linux系统中的一切都是文件，因此在系统中创建用户也就是修改配置文件的过程。用户的信息保存在/etc/passwd文件中，可以直接用文本编辑器来修改其中的用户参数项目，也可以用usermod命令修改已经创建的用户信息，诸如用户的UID、基本/扩展用户组、默认终端等。usermod命令的参数以及作用如表5-2所示。

表5-2                                            usermod命令中的参数及作用

参数	作用
-c	填写用户账户的备注信息
-d -m	参数-m与参数-d连用，可重新指定用户的家目录并自动把旧的数据转移过去
-e	账户的到期时间，格式为YYYY-MM-DD
-g	变更所属用户组
-G	变更扩展用户组
-L	锁定用户禁止其登录系统
-U	解锁用户，允许其登录系统
-s	变更默认终端
-u	修改用户的UID
大家不要被这么多参数吓坏了。我们先来看一下账户linuxprobe的默认信息：

[root@linuxprobe ~]# id linuxprobe
uid=1000(linuxprobe) gid=1000(linuxprobe) groups=1000(linuxprobe)
然后将用户linuxprobe加入到root用户组中，这样扩展组列表中则会出现root用户组的字样，而基本组不会受到影响：

[root@linuxprobe ~]# usermod -G root linuxprobe
[root@linuxprobe ~]# id linuxprobe
uid=1000(linuxprobe) gid=1000(linuxprobe) groups=1000(linuxprobe),0(root)
再来试试用-u参数修改linuxprobe用户的UID号码值。除此之外，我们还可以用-g参数修改用户的基本组ID，用-G参数修改用户扩展组ID。

[root@linuxprobe ~]# usermod -u 8888 linuxprobe
[root@linuxprobe ~]# id linuxprobe
uid=8888(linuxprobe) gid=1000(linuxprobe) groups=1000(linuxprobe),0(root)

用户移除分组
gpasswd
usermod -G {{groupName}} {{user}}
```
- userdel 删除用户

```
userdel命令用于删除用户，格式为“userdel [选项] 用户名”。
参数	作用
-f	强制删除用户
-r	同时删除用户及用户家目录
```
- gpasswd 将用户移除分组   
    - -A 设置组管理员用户 gpasswd -A {{user}} {{groupName}}
    - -a,-d 添加 用户到组，删除组内用户 gpasswd (-a|-d) {{user}} {{groupName}}
    - gpasswd -A

- groupadd，创建组
- groupdel， 删除组
- su, sudo
    - su 切换用户， su - guest_hello 完全切换，环境变量完全更新，不带“-” 则不更新环境变量
    - sudo sudo命令用于给普通用户提供额外的权限来完成原本root管理员才能完成的任务，格式为“sudo [参数] 命令名称”。sudo服务中可用的参数以及相应的作用下表所示。
        - 只有管理员才能 通过visudo 来编辑 配置文件 /etc/sudoers
            - ## Allow root to run any commands anywhere
            - guset_hello ALL=(ALL) 	ALL 来让某个用户拥有sudo权限
        - sudo -l 查看当前可以使用的命令
- /etc/passwd
- 查询当前用户 whoami
- 查看用户列表 cat /etc/passwd | grep {{useid}}  查询用户组 cat /etc/group
- groups 查看当前登录用户，查看当前所在组
- 更改用户 chown -R ${username} ${file||directory}
- change authority
- 创建组 groupadd ${groupName}
- 修改用户账户 usermod
- 添加用户到组 usermod -aG ${groupName}
- 设置用户组 usermod -g {groupname} {user}

## 查询时间
- date

## CentOS [设置开机启动](http://blog.csdn.net/jack_nichao/article/details/54093394)
## centos 7 之前的  用 chkconfig 以及 service,centos7 及其之后 使用systemctl 来控制

## 进程管理
- 查看 应用启动命令
  - ps 查询到 pid 然后cd /proc/pid
  - top - 19:30:22 up 297 days,  2:38,  1 user,  load average: 0.63, 0.81, 0.76
  Tasks: 175 total,   1 running, 174 sleeping,   0 stopped,   0 zombie
  Cpu(s):  6.4%us,  0.8%sy,  0.0%ni, 91.6%id,  0.8%wa,  0.0%hi,  0.2%si,  0.1%st
  Mem:  32877560k total, 32656428k used,   221132k free,   548260k buffers
  Swap:        0k total,        0k used,        0k free, 24348452k cached
  - top -p {{pid}} 查询某个pid 进程的状态。
- kill -9 ${PID}
- ps aux 是用BSD的格式来显示 java这个进程
显示的项目有：USER , PID , %CPU , %MEM , VSZ , RSS , TTY , STAT , START , TIME , COMMAND
ps -ef 是用标准的格式显示java这个进程
显示的项目有：UID , PID , PPID , C , STIME , TTY , TIME , CMD
(http://www.linuxidc.com/Linux/2016-07/133515.htm)

- netstat -anpt
> -a, --all
       Show both listening and non-listening (for TCP this means established connections) sockets.  With the --interfaces
--numeric , -n
       Show numerical addresses instead of trying to determine symbolic host, port or user names.
-p, --program
       Show the PID and name of the program to which each socket belongs.
option, show interfaces that are not up
<Socket>={-t|--tcp} {-u|--udp} {-U|--udplite} {-w|--raw} {-x|--unix}
           --ax25 --ipx --netrom


# linux 任务服务
cron.d
``` shell
SHELL=/bin/bash
PATH=/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root
HOME=/

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name command to be executed
00 3 * * 4 root python /home/python/server_check_py/server_check.py
00 5 * * * root rm_9090_catalina.sh
31 5 * * * root rm_9191_catalina.sh
00 6 * * * root rm_9292_catalina.sh
```


## awk 文本和数据进行处理的编程语言
