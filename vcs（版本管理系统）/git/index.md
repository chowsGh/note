# edit history
- 2016 11 17 15:45	3章完结
# [部分常用开源协议](http://blog.csdn.net/jasonding1354/article/details/45641811)
- [http://blog.csdn.net/u012150179/article/details/25490535](http://blog.csdn.net/u012150179/article/details/25490535)

#简介
[Git](https://git-scm.com)
```
1）/mtk/               过滤整个文件夹
2）*.zip                过滤所有.zip文件
3）/mtk/do.c         过滤某个具体文件
```
> Git 是分布式版本控制系统（Distributed Version Control System，简称 DVCS）相较svn 每一个客户端都会保存服务器的所有版本信息。不需要去联网就能进行一些代码的操作。

- 对待数据，直接记录快照，而非差异比较，更像是一个 快照流。
- Git 用以计算校验和的机制叫做 SHA-1 散列（hash，哈希）
- 三种状态
 > 已提交（committed）、已修改（modified）和已暂存（staged|indexed）

- 基本的 Git 工作流程如下：
	1. 在工作目录中修改文件。
	2. 暂存文件，将文件的快照放入暂存区域。
	3. 提交更新，找到暂存区域的文件，将快照永久性存储到 Git 仓库目录。

- 可以实现回滚操作[参考](https://pagespeed.v2ex.com/t/296286)
``` git
方法一
	git checkout ${target(tag|commit|branch)} //会detach HEAD
	git reset --soft ${current(branch)}
	git checkout ${current(branch)} //切换回master
	git commit -m "${commit-message}"
	git push
```

``` git
方法二
	git reset --hard ${target}
	git reset --soft ${current}
	git commit -m "${message}"
```

## 配置git config
- git config --list (查看配置列表)
git config --global user.name "1136141100@qq.com"
git config --global user.email "1136141100@qq.com"
git config --list --global
- 保存https 密码方法
```
https方式每次都要输入密码，按照如下设置即可输入一次就不用再手输入密码的困扰而且又享受https带来的极速
设置记住密码（默认15分钟）：git config --global credential.helper cache      
如果想自己设置时间，可以这样做：git config credential.helper cache --timeout=3600'     这样就设置一个小时之后失效
长期存储密码：git config --global credential.helper store
```
- git config --global user.name "John Doe" | git config --global user.email johndoe@example.com
设置全局属性

## 获取Git仓库
- git init
- git clone ${url} (${localpath}) 可以设置本地仓库名字
- git clone ${url} --config <key>=<value>(-c <key>=<value>)

## 查看当前状态 (git status)
- 状态简览 git status -s

## 跟踪新文件 (git add) 将修该的文件添加到暂存区 statged
- git add --all 可以将所有修改过的文件添加到暂存区。

## 退回 git reset ${--soft --mixed --hard} (${commit|branch|tag} | -- ${file})

```
将index 指向 target
--soft 不修改工作区 到target的所有改变Changes to be committed
--mixed 不修改工作区 到target的所有改变Unstaged changes after reset
--hard  修改工作区 到target的所有改变全部丢弃
```

## 撤销并提交 revert ${HEAD^n|startCommit}...${HEAD|targetCommit}
撤销每个提交的修改并再次提交

## git diff ${origin}/${branch} | ${branch|tag|commit}

## 忽略文件.gitignore
	- cd {{gitpath}}
	- git init
	- touch .gitignore
	- vim .gitigore

## 提交(commit)将暂存区中的文件提交到仓库 git commit (-a) -m ${message}
-a 将所有未添加到暂存区的修改添加到暂存区
-m 添加提交信息，一般为修改的描述，目的，作用
## 修改上次提交 git commit --amend

## 查看提交历史 git log
	- -p -2 最近两次的提交
	- --stat  附带一系列的总结性选项


## 远程仓库 git remote
- -v 查看详细信息
- 添加远程仓库		git remote add <shortname> <url>
- 删除远程仓库		git remote rm <shortname>
- 重命名远程仓库	git remote rename <old> <new>

## 删除 git rm
## 移动 git mv


#**帮助** (help) git ${cmd} --help
git help <verb>

#**标签**tag
- 列出标签				git tag
- 显示以word 开头的标签	git tag -l ${word}*
- 创建标签(某个提交)		git tag -a ${tagname}(${commit}) -m ${tagmessage}
- 删除标签 				git tag -d ${tagname}
- 共享标签				git push origin ${tagname}|--tags

``` git
git tag [-a | -s | -u <keyid>] [-f] [-m <msg> | -F <file>]
	<tagname> [<commit> | <object>]
```

## Git 别名
- git config --global alias.co checkout
- git config --global alias.br branch
- git config --global alias.ci commit 			例如输入 git ci 等效于 输入 git commit
- git config --global alias.st status
- git config --global alias.unstage 'reset HEAD --'
- git config --global alias.visual '!gitk'   你可能想要执行外部命令，而不是一个 Git 子命令

## 分支 branch
1. 创建分支并切换 git checkout -b ${branchname} git推荐创建新分支解决问题
	- git branch ${branchname}
	- git checkout ${branchname}
2. 合并分支
	- 切换到需要merge的分支然后merge
	- git checkout master
	- git merge ${branchname}
3. eclipse merge 可以用merge tool
	- 第一个客户端提交，第二个客户端不更新提交，就会有冲突，sync 后用merge tool
4. 查看本地分支详细信息 	git branch -v
5. 查看所有分支信息			git branch -a

## 变基 rebase
- 格式 ：git rebase [basebranch] [topicbranch]
- 总的原则是，只对尚未推送或分享给别人的本地修改执行变基操作清理历史，从不对已推送至别处的提交执行变基操作，这样，你才能享受到两种方式带来的便利。
- In general the way to get the best of both worlds is to rebase local changes you’ve made but haven’t shared yet before you push them in order to clean up your story, but never rebase anything you’ve pushed somewhere.

##**checkout** 牵出代码{到staged|index的状态}，切换分支
- 切换到tag历史记录会处在**分离头指针**状态，这个时修改是很危险的，在切换回主线时如果没有合并，之前的修改提交基本都会丢失，如果需要修改可以尝试**git checkout -b branch tag**创建一个基于指定tag的分支，例如：git checkout -b tset v0.1.0  这个时候就会在分支上进行开发，之后可以切换到主线合并。

#**拉 \ 推** (push[fetch&merge] \ pull)
- 推送到某个分支:git push origin ${branch}
- 推送一个在远程仓库不存在的分支:git push --set-upstream origin ${branch}
- 删除远程分支:git push origin --delete ${branch}

#**show**
- git show ${tag|branch|commit|HEAD} 显示详细信息

## Git on server
- [生成SSH key](https://www.git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E7%94%9F%E6%88%90-SSH-%E5%85%AC%E9%92%A5)
- [Server上搭建Git](https://www.git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-%E5%9C%A8%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E6%90%AD%E5%BB%BA-Git)
- [服务器上的 Git - GitLab](https://www.git-scm.com/book/zh/v2/%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%B8%8A%E7%9A%84-Git-GitLab)
- [服务器上面部署中央版本管理](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000)
- [GitLab官网](https://gitlab.com/gitlab-org/gitlab-ce/tree/master)。但是只能运行在linux上。



- git server
	- [gitblit](http://blog.csdn.net/hbtflying/article/details/52318691?locationNum=14)
	- gitolite
