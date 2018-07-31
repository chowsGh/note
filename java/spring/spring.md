# spring framework
是一个ioc 容器，提供注入功能。

## Web 集成
在 tomcat“web.xml”中加入上下文监听器
```
<!-- 配置上下文 配置文件 -->
<context-param>  
    <param-name>contextConfigLocation</param-name>  
    <param-value>  
    classpath:applicationContext.xml, 
    classpath*:app-datasource.xml,  
    classpath*:app-memcached.xml,  
    classpath*:app-ibatis.xml,  
    classpath*:app-rest.xml  
    </param-value>  
</context-param>
<!-- 配置监听器 -->
<listener>    
 <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>   
</listener>
```
注意classpath: 与 classpath*: 的区别
classpath*: 除了类加载路径里面的文件，还会从类加载路径里面的jar包中进行查找
https://www.cnblogs.com/Ant-soldier/p/5474085.html

## tomcat 编码问题
1. tomcat 编码设置
- 获取request的时候设置request.setCharacterEncoding(encoding);
- 返回response的时候设置response.setCharacterEncoding(encoding);
- 在返回客户端的时候设置 contentType 为utf-8
2. spring 编码设置
在tomcat web.xml 设置第一个过滤器
```
<filter>
    <filter-name>encodingFilter</filter-name>
    <filter-class>org.springframework.web.filter.CharacterEncodingFilter</filter-class>
    <init-param>
        <param-name>encoding</param-name>
        <param-value>UTF-8</param-value>
    </init-param>
    <init-param>
        <param-name>forceEncoding</param-name>
        <param-value>true</param-value>
    </init-param>
</filter>
<filter-mapping>
    <filter-name>encodingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

## spring xml 配置文件
1. 键值对配置加载https://blog.csdn.net/blueboz/article/details/54808915，https://blog.csdn.net/ws_blog/article/details/46986051
```
<!-- 方式一 -->
<context:property-placeholder     
        location="属性文件，多个之间逗号分隔"    
        file-encoding="文件编码"    
        ignore-resource-not-found="是否忽略找不到的属性文件"    
        ignore-unresolvable="是否忽略解析不到的属性，如果不忽略，找不到将抛出异常"    
        properties-ref="本地Properties配置"    
        local-override="是否本地覆盖模式，即如果true，那么properties-ref的属性将覆盖location加载的属性，否则相反"    
        system-properties-mode="系统属性模式，默认ENVIRONMENT（表示先找ENVIRONMENT，再找properties-ref/location的），NEVER：表示永远不用ENVIRONMENT的，OVERRIDE类似于ENVIRONMENT"    
        order="顺序"    
        /> 
<!-- 方式一实例 -->
<context:property-placeholder location="classpath:cfg.properties,classpath:cfg2.properties" system-properties-mode="NEVER"/>
        
<!-- 方式二 -->
<bean id="propertyConfigurer" class="org.springframework.beans.factory.config.PropertyPlaceholderConfigurer">
    <property name="fileEncoding" value="utf-8" />
    <property name="locations">
        <list>
            <value>classpath*:xxl-job-executor.properties</value>
        </list>
    </property>
</bean>
```
重要注意
我们知道，不论是使用PropertyPlaceholderConfigurer还是通过context:property-placeholder这种方式进行实现，都需要记住，Spring框架不仅仅会读取我们的配置文件中的键值对，而且还会读取Jvm 初始化的一下系统的信息。有时候，我们需要将配置Key定一套命名规则 ，例如
项目名称.组名.功能名=配置值
org.team.tfunction=0001

# spring 项目代码结构

# 常见问题
url-pattern 中设置 “/” 和 “/*” 的区别“/”表示路径，不表示具体的资源，例如.jpg，.html。而“/*”则可以表示具体的资源以及路径