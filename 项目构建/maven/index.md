# introduction 介绍
# install 安装
# configuration 配置
全局配置文件：${installPath}/conf/setting.xml
配置文件结构
- settings 根节点
    - localRepository（本地仓库路径）
    - proxies（网络代理）
    - mirrors（仓库镜像）
    - ...

## 配置本地仓库地址

## [配置高速镜像](https://www.cnblogs.com/zengming/p/7786684.html)
- [阿里云maven首页](http://maven.aliyun.com/)，使用nexus搭建。
- https://blog.csdn.net/cwh056056/article/details/49646111

``` xml
<mirror>
    <id>nexus-aliyun</id>
    <mirrorOf>central</mirrorOf>
    <name>Nexus aliyun</name>
    <url>http://maven.aliyun.com/nexus/content/groups/public</url>
</mirror>
```
# 构建周期
三个类型的声明周期：clean default site
[生命周期](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)
## 生命周期阶段
- default : validate compile test package verify install deploy
- clean : pre-clean clean post-clean
- 如果执行install 阶段的话会顺序执行install之前的生命周期
# 插件
插件是生命周期的具体阶段的实现
# mvn 常见用法（运行的其实是maven的默认插件）
- -v
- clean（清除target文件夹内生成的文件）
- compile（编译 src/main 目录的源文件）
- test（运行src/test 的测试用例）
- package
- install
- 可以使用输入多个命令，mvn 会顺序执行

# 使用原型创建项目结构
- 交互式创建 mvn archetype:generate

# maven 项目坐标
groupId,artifactId,version 组成唯一表示。groupId 使用公司网址反写 + 项目，artifactId 项目-模块 来命名，version 0.0.1-SNAPSHOT（大版本号，分支版本号，小版本号，版本类型SNAPSHOT，ALPHA，BETA，RELEASE，GA）

# 代码结构
root(项目根目录)
- src
    - main
        - java(java 代码路径)
        - resources(资源目录)
    - test
        - java(java 代码路径)
        - resources(资源目录)
- target
    - classes
    - test-classes
- pom.xml

# 仓库
- 本地仓库（在编译获取依赖的时候优先使用本地仓库）
- 远程仓库
    - 中央仓库（可以使用镜像）
# 常见构建框架
# pom.xml 配置文件
- project
    - modelVersion（pom版本）
    - packaging（打包方式默认是jar）
    - groupId
    - artifactId
    - version
    - dependencies
        - dependency
            - groupId
            - artifactId
            - version
            - type
            - scope（依赖范围， test compile run，不同环境设置不同classpath）
            - exclusions
                - exclusion
    - dependencyManagement （父模块 定义依赖版本）
        - dependencies
        - dependency
    - build
        - plugins
            - plugin
    - parent
    - modules（项目模块化，）
        - module
# 依赖范围
- provided (在测试和编译的时候使用)
- test
- compile
- run
# 依赖传递性，排除依赖
# 依赖冲突
1. 最短路径A->B->C->X,A->D->X 选择D依赖的X
2. 同路径，优先声明A->B->X,A->D->X选择B依赖的X

# 聚合和继承
1. 聚合 将packaging 设置成pom，将要聚合进来的项目添加在model里
2. 继承 在parent 项目里面统一管理依赖版本，dependencyManagement build->pluginManagement，配置依赖，以及版本号，然后在子项目中的pom 加入parent标签，除非需要覆盖版本号，剩余情况可以直接省略依赖的版本号。
子项目中的依赖版本号会继承父项目中的依赖版本号。

# jetty，tomcat 插件运行web项目
在build 中配置jetty|tomcat的插件，然后绑定在某一个阶段，例如在package阶段 在pom 的 build 里面配置 plugins->plugin->groupId,artifactId,version,excutions->excution->phase,goals->goal,
```
<plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat7-maven-plugin</artifactId>
    <version>2.2</version>
    <executions>
    <execution>
    <phase>package</phase>
    <goals>
    <goal>
    run
    </goal>
    </goals>
    </execution>
    </executions>
</plugin>
```
如果不绑定 可以使用mvn tomcat7:run 来运行

# 其他用户
生成 报表
##　配置高速镜像
# 常见用法
