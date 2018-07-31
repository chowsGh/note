# spring 集成 mybaits
```
<!-- 数据连接池配置 -->
<bean id="dataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource"  destroy-method="close">
    <property name="driverClass" value="${xxl.job.db.driverClass}" />
    <property name="jdbcUrl" value="${xxl.job.db.url}" />
    <property name="user" value="${xxl.job.db.user}" />
    <property name="password" value="${xxl.job.db.password}" />
    <property name="initialPoolSize" value="3" />  
    <property name="minPoolSize" value="2" />  
    <property name="maxPoolSize" value="10" />  
    <property name="maxIdleTime" value="60" />
    <property name="acquireRetryDelay" value="1000" />
    <property name="acquireRetryAttempts" value="10" />
    <property name="preferredTestQuery" value="SELECT 1" />
</bean>
<!-- sql session factory -->
<bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
    <property name="dataSource" ref="dataSource" />
    <property name="mapperLocations" value="classpath:mybatis-mapper/*.xml"/>
</bean>

<bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    <property name="sqlSessionFactoryBeanName" value="sqlSessionFactory"/>
    <property name="basePackage" value="com.xxl.job.admin.dao" />
</bean>
```

```
<!-- 事务 -->
<bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource" />
</bean>
  
<tx:annotation-driven transaction-manager="transactionManager" proxy-target-class="true"/>

```