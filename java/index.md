## [[JAVA 官方文档]](https://docs.oracle.com/javase/9/)
- [jdk8官方教程](https://docs.oracle.com/javase/tutorial/)
- [关键字](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html)

```
Java Language Keywords

Here is a list of keywords in the Java programming language. You cannot use any of the following as identifiers in your programs. The keywords const and goto are reserved, even though they are not currently used. true, false, and null might seem like keywords, but they are actually literals; you cannot use them as identifiers in your programs.
abstract 	continue 	for 	new 	switch
assert*** 	default 	goto* 	package 	synchronized
boolean 	do 	if 	private 	this
break 	double 	implements 	protected 	throw
byte 	else 	import 	public 	throws
case 	enum**** 	instanceof 	return 	transient
catch 	extends 	int 	short 	try
char 	final 	interface 	static 	void
class 	finally 	long 	strictfp** 	volatile
const* 	float 	native 	super 	while
* 	  	not used
** 	  	added in 1.2
*** 	  	added in 1.4
**** 	  	added in 5.0
```

## [[Java Decompile]](https://www.zhihu.com/question/20264247)
- [[JD-GUI(java decompile)]](http://jd.benow.ca/)

## [TDA - Thread Dump Analyzer ](https://github.com/irockel/tda)
- 一个分析java程序的工具，在tomcat挂掉后，先用jstack -l tomcat进程ID > dump.log把tomcat的运行信息dump出来，然后用这个工具打开这个dump.log进行分析。

## [[CAT]](https://github.com/dianping/cat)基于Java开发的实时应用监控平台，包括实时应用监控，业务监控。

## [[JNA（Java Native Access ）]] (http://hao.jobbole.com/jna/)
- AES/CBC/PKCS5Padding

## 静态分析工具
Pmd 它是一个基于静态规则集的Java源码分析器，它可以识别出潜在的如下问题：
- 可能的bug——空的try/catch/finally/switch块。
- 无用代码(Dead code)：无用的本地变量，方法参数和私有方法。
- 空的if/while语句。
- 过度复杂的表达式——不必要的if语句，本来可以用while循环但是却用了for循环。
- 可优化的代码：浪费性能的String/StringBuffer的使用。

FindBugs 它用来查找Java代码中存在的bug。它使用静态分析方法标识出Java程序中上百种潜在的不同类型的错误。

Checkstyle 它定义了一系列可用的模块，每一个模块提供了严格程度(强制的，可选的…)可配置的检查规则。规则可以触发通知(notification)，警告(warning)和错误(error)。

现在有很多查看这些工具的处理结果的方式：

    XML格式：这些工具都可以产生XML文件，这些XML文件能用来产生HTML报表或者是被别的工具用来浏览分析的结果。
    HTML格式：HTML格式是最受欢迎的产生报表和团队间分享的的方式，你也可以用xsl表格创建你自己的报表。
    IDE插件：几乎所有叫得上名字的IDE都给这些工具提供了插件，这使得发现源码中存在的所有问题几乎变成可能。

代码质量工具的一个问题是，它们有时候会给开发者提示很多不是错误的错误-也叫做假阳性(false positives)。当这种情况发生的时候，开发者可以学着忽略工具的输出信息，或者是把这些输出全部抛弃掉。

为了更好的利用这些工具的输出结果，给开发者一个更有用的视图，最好是有一种只关注我们想要的东西的方式。本文中，我们将找出其他有趣的方式来更好的利用所有这些有名的Java静态分析工具的输出结果，然后可以像查询数据库那样查询这些结果。

## 阿里巴巴java 开发手册
以 Java 开发者为中心视角，划分为编程规约、异常日志、单元测试、安全规约、工程结构、MySQL 数据库六个维度
- [eclipse插件] https://github.com/alibaba/p3c/tree/master/eclipse-plugin
## java 远程调试
要让远程服务器运行的代码支持远程调试，则启动的时候必须加上特定的JVM参数，这些参数是：
-Xdebug -Xrunjdwp:transport=dt_socket,suspend=n,server=y,address=${debug_port}
- 参考
  - [idea](http://www.cnblogs.com/wy2325/p/5600232.html)
  - [tomcat](http://blog.csdn.net/afgasdg/article/details/9236877)
- 遇到连接不上的时候可以用telnet 127.0.0.1 5555 来尝试连接, eclipse 可以通过debug 视图查看当前调试情况
