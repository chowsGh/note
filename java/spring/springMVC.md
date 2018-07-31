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
## 配置拦截器，“/**” 形式表示可以拦截/mydo 以及 /mydo/test。而“/*” 只能拦截 /mydo
```
<mvc:interceptors>
    <mvc:interceptor>
        <mvc:mapping path="/**"/>
        <bean class="com.xxl.job.admin.controller.interceptor.PermissionInterceptor"/>
    </mvc:interceptor>
    <mvc:interceptor>
        <mvc:mapping path="/**"/>
        <bean class="com.xxl.job.admin.controller.interceptor.CookieInterceptor"/>
    </mvc:interceptor>
</mvc:interceptors>

<mvc:interceptors>  
    <!-- 局部拦截器 -->  
    <mvc:interceptor>  
        <mvc:mapping path="/**" />                      
        <mvc:exclude-mapping path="/user_login" />  
        <mvc:exclude-mapping path="/user_logout" />  
        <bean class="com.itcast.oa.interceptor.MyInterceptor" />  
    </mvc:interceptor>  
</mvc:interceptors>  
```

## 配置资源路径
```
<mvc:resources mapping="/favicon.ico" location="/favicon.ico" />
<mvc:resources mapping="/static/**" location="/static/" />
<mvc:resources mapping="/**/*.html" location="/" />
```

## 配置异常处理
<bean id="exceptionResolver" class="com.xxl.job.admin.controller.resolver.WebExceptionResolver" />处理类继承自HandlerExceptionResolver

## spring mvc 视图配置
```
<!-- spring freemarker集成 配置 -->
<bean id="freemarkerConfig" class="org.springframework.web.servlet.view.freemarker.FreeMarkerConfigurer">
    <property name="templateLoaderPath" value="/WEB-INF/template/" />
    <property name="freemarkerSettings">
        <bean class="org.springframework.beans.factory.config.PropertiesFactoryBean">
            <property name="location" value="classpath:freemarker.properties" />
        </bean>
    </property>
</bean>
<!-- freemarker 视图解析器 -->
<bean id="viewResolver"	class="org.springframework.web.servlet.view.freemarker.FreeMarkerViewResolver">
    <property name="viewClass" value="org.springframework.web.servlet.view.freemarker.FreeMarkerView" />
    <property name="prefix" value="" />
    <property name="suffix" value=".ftl" />
    <property name="contentType" value="text/html;charset=UTF-8" />
    <property name="exposeSpringMacroHelpers" value="true" />
    <property name="exposeRequestAttributes" value="true" />
    <property name="exposeSessionAttributes" value="true" />
    <property name="requestContextAttribute" value="request" />
    <property name="cache" value="true" />
    <property name="order" value="0" />
</bean>
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
