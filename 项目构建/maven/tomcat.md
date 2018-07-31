# 使用tomcat 插件运行web项目
![a](./1.jpg)
0. pom.xml 配置
```
<build>
<plugins>
    <plugin>
        <groupId>org.apache.tomcat.maven</groupId>
        <artifactId>tomcat7-maven-plugin</artifactId>
        <configuration>
            <path>/</path>
            <port>8888</port>
            <uriEncoding>UTF-8</uriEncoding>
        </configuration>
    </plugin>
</plugins>
</build>
```
1. 运行 mvn:tomcat7:run
## 可以用来在eclipse 中调试

# 部署到tomcat
0. 前提：需要已经配置过tomcat manager 的用户 tomcat1/tomcat1
1. maven conf/server.xml 中配置 tomcat 位置以及密码
```
<servers>
<server>  
  <id>localTomcat8080</id>  
  <username>tomcat1</username>  
  <password>tomcat1</password>  
</server>  
</servers>
```
2. pom.xml中配置
```
<build>
<finalName>xmall-search-service</finalName>
<plugins>
   <plugin>
       <groupId>org.apache.tomcat.maven</groupId>
       <artifactId>tomcat7-maven-plugin</artifactId>
       <configuration>
           <path>/${project.build.finalName}</path>
           <server>localTomcat8080</server>
           <!-- 这里是本地tomcat，如果是远程服务器可以改成对应的地址，实现自动部署-->
           <url>http://localhost:8080/manager/text</url>
        </configuration>
   </plugin>
</plugins>
</build>
```
3. 第一次部署mvn:tomcat7:deploy
4. 再次部署mvn:tomcat7:redeploy
