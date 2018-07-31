# Eclipse 开发配置
## 基础配置
1. 全局编码集 window->perference->General->workspace
Text file encoding 选择UTF-8，New text file line delimiter 选择Unix
1. 显示行号，显示空白字符，使用4个空格替换(关键是不要混用tab 和 空格) tab：window->perference->General->Editors->insert spaces for tabs；show line numbers；show whitespace characters
1. coding style（编码风格）java->code style->clean up|code template|
1. font/color（字体大小颜色）
1. 启动，关闭相关配置 window->perference->General->start up shutdown
## java 开发
### 配置jdk window->perference->java->installed jres，设置本地安装的jdk目录
## 项目构建
### maven
- 常用插件
- 使用
    - 设置安装目录（window->perference->maven->installation）
    - 设置全局配置文件（window->perference->maven->user settings）
- 运行配置
    - run edit configuration
        - 设置goals 即 指定插件。例如：compile，clean，install，package，test...