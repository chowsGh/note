# 部署发布java web项目
步骤1：
conf/tomcat-users.xml,设置manager 用户
步骤2：
访问 manager 的页面即可
```
For example, to add the manager-gui role to a user named tomcat with a password of s3cret, add the following to the config file listed above.
<role rolename="manager-gui"/>
<user username="tomcat" password="s3cret" roles="manager-gui"/>
Note that for Tomcat 7 onwards, the roles required to use the manager application were changed from the single manager role to the following four roles. You will need to assign the role(s) required for the functionality you wish to access.
manager-gui - allows access to the HTML GUI and the status pages
manager-script - allows access to the text interface and the status pages
manager-jmx - allows access to the JMX proxy and the status pages
manager-status - allows access to the status pages only
```
