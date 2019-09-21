## 创建版本库
1. `git init`
2.  将文件添加到仓库
    ```
    git add <file>
    git commit -m <message>
    ```
        
## 版本控制
1. 了解工作区状态
    ```
    git status #查看工作区状态
    git diff #查看修改内容
    ```
2. 了解版本变化
    ```
    git log   #查看历史记录
    git log --pretty=oneline #单行格式查看
    git reflog #查看命令历史，以便确认回到未来的分支
    ```
3. 回到过去
    - HEAD      #指向当前版本，
    - HEAD^     #指向上一个版本，
    - HEAD^^    #指向上两个版本;HEAD~100:上100个版本
    ```
    git reset --hard commit_id #回到某一个版本
    ```
4. 工作区和暂存区
    - 工作区：本地电脑可视目录
    - 版本库：工作区中的.Git隐藏目录
        · 暂存区
        · master：git自动创建的分区
        · HEAD指针
5. 管理修改
    - git 跟踪并管理的是修改，而并非文件；
    - git commit 的是git add的内容，而并非文件差异
6. 撤销更改
   ```
    git checkout -- file #让文件回到最近一次 git add 或者git commit的状态
    git reset HEAD <file> #撤销暂存区的修改
    ```
7. 删除文件
    ```
    git rm #从版本库删除文件，包含暂存区或者msater
    ```