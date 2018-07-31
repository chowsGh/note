
# spring framework
是一个ioc 容器，提供注入功能。
# 关键内容
## Web 集成
在 tomcat“web.xml”中加入上下文监听器
```
<!-- 配置上下文 配置文件 -->
<context-param>  
	<param-name>contextConfigLocation</param-name>  
 	<param-value>  
     classpath:applicationContext.xml  
	</param-value>  
</context-param>
<!-- 配置监听器 -->
<listener>    
 <listener-class>org.springframework.web.context.ContextLoaderListener</listener-class>   
</listener>
```

- spring 集成 tomcat
    - listener
    - encode filter
    - url-pattern 配置 / /** /a* /a*.html /*.do /test.*
- spring ioc 配置
- spring mvc 配置
    - 配置DispatchServlet 匹配路径
    - 静态资源路径配置 mvc:resources
    - 拦截器 mvc:interceptors
    - 资源视图配置
    - 异常捕获配置
    - url-pattern 配置 /** /* /test*/**

- spring 配置文件配置
``` xml
<bean id="propertyConfigurer" class="com.zheng.common.plugin.EncryptPropertyPlaceholderConfigurer">
    <property name="locations">
        <list>
            <value>classpath:jdbc.properties</value>
            <value>classpath:redis.properties</value>
        </list>
    </property>
</bean>
<bean id="propertyConfigurer" class="org.springframework.beans.factory.config.PreferencesPlaceholderConfigurer">  
        <property name="location">  
        <value>classpath:config.properties</value>  
        </property>
        <property name="fileEncoding">   
       <value>UTF-8</value>   
     </property>
</bean>
<!-- 多个配置使用“,”隔开-->
    <context:property-placeholder     
           location="classpath:config.properties"    
           file-encoding="UTF-8"    
           ignore-resource-not-found=""   
           ignore-unresolvable=""    
           properties-ref=""    
           local-override=""    
           system-properties-mode=""   
           order=""    
    />  
```
- classpath* 与 classpath 的区别是 classpath* 回去搜索其他jar包中的配置
# 创建 spring MVC 项目基本流程

# spring test maven 集成
1. 引入依赖 junit，spring test，spring基础包 bean context core
``` xml
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>${junit.version}</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```
2. src/test/ 建立test基类
``` java
package com.chows.lab.springmvc.test;

import org.junit.runner.RunWith;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.AbstractJUnit4SpringContextTests;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@ContextConfiguration(locations = { "classpath:spring/applicationContext.xml","classpath:spring/applicationContext-dao.xml","classpath:spring/springMVC.xml" })
@RunWith(SpringJUnit4ClassRunner.class)
public class SpringTestBase extends AbstractJUnit4SpringContextTests{

}
```
