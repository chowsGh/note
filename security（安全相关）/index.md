## AES 加密模式，工作模式，初始化向量，密码
- 工作模式
	- 1.2. CBC模式（密码分组链接：Cipher-block chaining）
	- 1.3. CFB模式(密文反馈:Cipher feedback)
	- 1.3.1. CFB8的加密流程
	- 1.3.2. CFB1的加密流程
	- 1.4. OFB模式（输出反馈：Output feedback）)
- 初始化向量
	- IV 在CBC,CFB,OFB工作模式中需要一个初始化数据来进行运算，每次的结果都是***上次运算的结果（or初始化向量）和密码***一起运算得到的


# python 实现
在windows 安装 加密模块需要 安装windows 编译工具
error: Microsoft Visual C++ 9.0 is required. Get it from http://aka.ms/vcpython27

# 小程序 解密用户信息 demo https://mp.weixin.qq.com/debug/wxadoc/dev/demo/aes-sample.zip
