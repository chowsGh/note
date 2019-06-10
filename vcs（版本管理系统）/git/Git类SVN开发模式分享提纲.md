# Git 类SVN开发模式分享——提纲

<a name="8s2Gi"></a>
# 背景/使用场景
分布式代码版本管理工具<br />与svn的差别，代码可以分布式管理，也可以集中管理，终端用户可以在本地不联网的情况下开发，需要提交到中央库的时候在联网。
<a name="MFBRb"></a>
# 基础概念
<a name="4aXMK"></a>
## 本地仓库
<a name="D9Jcf"></a>
### Git仓库三个区
工作区；暂存区；版本仓库
<a name="IUyX4"></a>
### Git文件周期
<a name="eeqzX"></a>
#### Git文件状态
<a name="moGod"></a>
#### Git文件存储原理
每个commit 是文件快照索引的集合
<a name="BVAPR"></a>
### Git本地开发基本操作

1. init 
1. add/reset file/checkout file
1. commit
1. log
1. reflog
1. reset 简单介绍 --soft --mix --hard
<a name="Q3ean"></a>
### 文件恢复

1. reset file
1. revert file
1. checkout file
1. reset --hard file
1. reset --hard HEAD~n file
<a name="0pKLA"></a>
## 分支
切换/新建分支，分支提交，分支合并，分支rebase，删除分支<br />git 分支切换比较方便，本地仓库HEAD只能指向一个分支

<a name="Fc8zB"></a>
## 标签
git tag 

<a name="mdtkQ"></a>
# 查看帮助

1. git pro
1. git ${command} --help

<a name="cUmdC"></a>
# 开发实践
<a name="0hRDI"></a>
## 类svn开发
<a name="RfbEu"></a>
### fast-forwarded（快速向前）
如果本地提交是基于远程库最新的版本的修改，则push后，远程库版本快速向前<br />如果本地提交与远程库产生了分歧则不能直接通过 pull 快速向前，需要merge 或者 rebase
<a name="vgy6r"></a>
### merge
<a name="XkD5T"></a>
### Rebase
将指定库所有从最近的共同commit到最新的commit的提交重放到本地库，然后将本地库特有的commit在最新commit的基础上进行merge。这样push到指定库，可以直接fast forward<br /> 
<a name="a4weI"></a>
### 常用命令

1. 使用ssh url 需要配置公钥
1. git clone ${remote url}
1. 本地开发，并本地提交
1. git stash save -u "stash comment" / git stash list / git stash apply ${stashid}
1. 合并代码
  1. git pull --rebase origin master 可以减少代码分支合并，将本地代码以远程库origin master最新提交为基础修改本地提交内容，可能涉及到merge代码，完成后，代码可以直接提交到远程库
  1. 或者 git pull 使用合并，会产生一个merge commit，使历史不太容易查看
6. git push
<a name="9keZx"></a>
### 客户端使用介绍
<a name="j3nRr"></a>
### Eclipse 插件使用介绍
<a name="wHwgr"></a>

# ISource 代码Review 介绍