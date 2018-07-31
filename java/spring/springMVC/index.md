# spring mvc
## tomcat 集成
在web.xml中配置 分发servlet
```
<servlet>
    <servlet-name>spring</servlet-name>
    <!-- spring mvc 分发servlet -->
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
        <param-name>contextConfigLocation</param-name>
        <!-- spring mvc 的配置文件 -->
        <param-value>classpath:springMVC.xml</param-value>
    </init-param>
    <!-- spring mvc servlet 启动顺序 -->
    <load-on-startup>1</load-on-startup>
    <async-supported>true</async-supported>
</servlet>
<servlet-mapping>
    <servlet-name>spring</servlet-name>
    <url-pattern>/</url-pattern>
</servlet-mapping>
```

## springMVC.xml 常见问题
1. 问题：和spring 的配置 重合，多次扫描，spring 加载两次 配置文件。  
解决：spring 和 spring mvc 将会初始化两个ioc容器
spring 主要是提供dao service 等bean
spring mvc 是绑定在 DispatcherServlet 所以主要需要的是 controller
如何避免就是在使用包扫描的时候 分包扫  
**DispatchServlet.xml**        <context:component-scan base-package="xx.xx.xx.controller" />  
**applicationContext.xml**   <context:component-scan base-package="xx.xxx.xx.dao,xx.xx.xxx.service"/>
2. 问题： springmvc中url-pattern /和/\*的区别  
解决： 单个 / 表示路径，不代表确定的资源。例如http://www.baidu.com/。\* 表示除了匹配路径外，还匹配确定的资源，例如http://www.baidu.com/index.php
