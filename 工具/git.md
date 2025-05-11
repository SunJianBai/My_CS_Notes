[toc]





---

## Git 简介

Git 是一个分布式版本控制系统，用于跟踪代码的更改、协作开发和管理项目历史。无论你是个人开发者还是团队成员，掌握 Git 都是非常有价值的。以下是关于如何使用 Git 的详细指南，包括安装、基本操作、分支管理、远程仓库以及常用的工作流程。

Git 属于分布式版本控制系统，而 SVN 属于集中式。

![image-20241117151300391](git.assets/image-20241117151300391.png)

集中式版本控制只有中心服务器拥有一份代码，而分布式版本控制每个人的电脑上就有一份完整的代码。

集中式版本控制有安全性问题，当中心服务器挂了所有人都没办法工作了。

集中式版本控制需要连网才能工作，如果网速过慢，那么提交一个文件会慢的无法让人忍受。而分布式版本控制不需要连网就能工作。

分布式版本控制新建分支、合并分支操作速度非常快，而集中式版本控制新建一个分支相当于复制一份完整代码。

它的主要特点包括：

- **分布式**：每个开发者的本地仓库都是完整的，包含整个项目的历史。
- **高效**：适用于大规模项目，操作速度快。
- **支持非线性开发**：通过分支和合并，支持多样化的开发流程。
- **数据完整性**：每个提交都有唯一的哈希值，确保数据的一致性和完整性。

## 安装 Git

### Windows

1. 前往 [Git for Windows](https://gitforwindows.org/) 官网下载最新的安装包。
2. 运行安装程序，按照向导完成安装。推荐使用默认设置，除非有特定需求。
3. 安装完成后，可以通过 Git Bash 或者命令提示符（CMD）使用 Git。

### Linux

对于不同的发行版，使用相应的包管理器安装。

- **Debian/Ubuntu**:
  
  ```bash
  sudo apt update
  sudo apt install git
  ```
- **Fedora**:
  
  ```bash
  sudo dnf install git
  ```
- **Arch Linux**:
  
  ```bash
  sudo pacman -S git
  ```

## 配置 Git

安装完成后，需要进行一些基本配置，设置你的用户名和邮箱，这些信息会记录在每一次提交中。

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"
```

你还可以配置一些常用选项：

- **查看当前配置**:
  ```bash
  git config --list
  ```
- **设置默认文本编辑器（例如 VS Code）**:
  ```bash
  git config --global core.editor "code --wait"
  ```
- **设置合并工具（例如 VS Code）**:
  ```bash
  git config --global merge.tool vscode
  ```

## 基本 Git 操作

### 初始化仓库

在一个现有的项目目录中初始化一个 Git 仓库：

```bash
cd /path/to/your/project
git init
```

初始化新建一个仓库之后，当前目录就成为了工作区，工作区下有一个隐藏目录 .git，它属于 Git 的版本库。

Git 的版本库有一个称为 Stage 的暂存区以及最后的 History 版本库，History 存储所有分支信息，使用一个 HEAD 指针指向当前分支。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208195941661.png"/> </div><br>

### 添加更改

将更改添加到暂存区，为下一次提交做准备。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208200014395.png"/> </div><br>

- 添加单个文件：
  ```bash
  git add filename
  ```
- 添加所有更改的文件：
  ```bash
  git add .
  ```
- 添加指定类型的文件，例如所有 `.js` 文件：
  ```bash
  git add *.js
  ```

### 提交更改

将暂存区的更改记录到仓库历史中。

```bash
git commit -m "你的提交信息"
```

**提示**：提交信息应简洁明了，描述所做的更改。

上面这行是简略版的输入,你也可以像下面这样：

```powershell
git commit
```

然后会自动打开vim终端编辑器里来写提交说明（会linux的uu肯定不陌生），想用这种方法的可以去看看vim的使用教程，这里就不多赘述了。



当然，也可以跳过暂存区域直接从分支中取出修改，或者直接提交修改到分支中。

- git commit -a 直接把所有文件的修改添加到暂存区然后执行提交
- git checkout HEAD -- files 取出最后一次修改，可以用来进行回滚操作

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208200543923.png"/> </div><br>



### 查看日志

查看提交日志，了解项目的演变。

- **基本历史**:
  
  ```bash
  git log
  ```
  
  会输出类似下面这样的日志信息，`28198b688941ebe7fb1dd0467f37ea9f999904a5`是这次提交的随机id作为提交的唯一标识，后面两行是提交作者和时间。“第一次提交”则是我这次提交的说明。
  
  ```
  PS D:\Codes\test> git log
  commit 28198b688941ebe7fb1dd0467f37ea9f999904a5 (HEAD -> master)
  Author: sun <2274540432@qq.com>
  Date:   Sun Nov 17 00:31:15 2024 +0800
  
      第一次提交
  ```
  
  
  
- **简洁格式**:
  
  ```bash
  git log --oneline
  ```
  
- **图形化日志**:
  
  ```bash
  git log --graph --oneline --all
  ```



### 查看状态

查看当前工作目录和暂存区的状态，了解哪些文件被修改、哪些文件被暂存等。

```bash
git status
```

###

## 分支管理

分支允许你在不影响主线的情况下进行开发。常用的分支操作包括创建、切换、合并和删除分支。

使用指针将每个提交连接成一条时间线，HEAD 指针指向当前分支指针。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208203219927.png"/> </div><br>

### 创建和切换分支

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208203142527.png"/> </div><br>

每次提交只会让当前分支指针向前移动，而其它分支指针不会移动。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208203112400.png"/> </div><br>

- **创建新分支**:
  
- 新建分支是新建一个指针指向时间线的最后一个节点，并让 HEAD 指针指向新分支，表示新分支成为当前分支。
  
  ```bash
  git branch new-branch
  ```
  
- **切换到新分支**:
  
  ```bash
  git checkout new-branch
  ```
  
- **创建并切换到新分支**（快捷方式）:
  
  ```bash
  git checkout -b new-branch
  ```

### 查看分支

列出所有分支，并显示当前所在的分支。

```bash
git branch
```

### 合并分支

将另一个分支的更改合并到当前分支。

1. 切换到目标分支（例如 `main`）：
   ```bash
   git checkout main
   ```
2. 合并 `new-branch` 到 `main`：
   ```bash
   git merge new-branch
   ```

### 分支冲突

当两个分支修改了同一文件的同一部分时，Git 无法自动合并，需要手动解决冲突。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/image-20191208203034705.png"/> </div><br>

Git 会使用 \<\<\<\<\<\<\< ，======= ，\>\>\>\>\>\>\> 标记出不同分支的内容，只需要把不同分支中冲突部分修改成一样就能解决冲突。

1. 在合并过程中，如果出现冲突，Git 会提示有冲突的文件。
2. 打开冲突文件，手动编辑标记的冲突部分：
   ```diff
   <<<<<<< HEAD
   当前分支的内容
   =======
   被合并分支的内容
   >>>>>>> new-branch
   ```
3. 修改文件以解决冲突，删除冲突标记。
4. 添加解决冲突后的文件到暂存区：
   ```bash
   git add conflicted-file
   ```
5. 完成合并提交：
   ```bash
   git commit
   ```

## .gitignore 文件

忽略以下文件：

- 操作系统自动生成的文件，比如缩略图；
- 编译生成的中间文件，比如 Java 编译产生的 .class 文件；
- 自己的敏感信息，比如存放口令的配置文件。

不需要全部自己编写，可以到 [https://github.com/github/gitignore](https://github.com/github/gitignore) 中进行查询。



## 远程仓库

远程仓库允许你与他人共享代码，常见的远程仓库服务有 GitHub、GitLab 和 Bitbucket。

### SSH 传输设置

Git 仓库和 Github 中心仓库之间的传输是通过 SSH 加密。

如果工作区下没有 .ssh 目录，可以通过以下命令来创建 SSH Key：

1. **生成 SSH 密钥**  
   打开终端，运行以下命令（如果已有密钥，可以跳过这一步）：

   ```bash
   ssh-keygen -t ed25519 -C "你的邮箱@example.com"
   ```

   按提示选择密钥保存路径（默认是 `~/.ssh/id_ed25519`），并设置密码（可选）。

   > ed25519是一种高性能的公钥加密算法，主要用于生成数字签名和密钥交换。当然也可以使用RSA。

2. **添加 SSH 密钥到 SSH 代理**  
   启动 SSH 代理：

   ```bash
   eval "$(ssh-agent -s)"
   ```

   添加密钥到代理：

   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

3. **将公钥添加到 GitHub**  
   复制公钥内容到剪贴板：

   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```

   然后：

   - 打开 GitHub 网站，点击右上角头像 -> **Settings**。
   - 在左侧菜单中选择 **SSH and GPG keys**。
   - 点击 **New SSH key**，粘贴公钥内容并保存。

4. **测试 SSH 连接**  
   测试是否能连接到 GitHub：

   ```bash
   ssh -T git@github.com
   ```

   如果配置成功，会提示类似：

   ```
   Hi username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

5. **将本地仓库链接到远程仓库**  
   复制 SSH 地址（例如：`git@github.com:username/repository.git`），然后运行：

   ```bash
   git remote add origin git@github.com:username/repository.git
   ```

6. **首次推送时设置分支关联**  
   推送本地代码到远程仓库：

   ```bash
   git push -u origin main
   ```

---



### 添加远程仓库

在本地仓库中添加一个远程仓库：

```bash
git remote add origin https://github.com/username/repository.git
```

- `origin` 是默认的远程仓库名称，可以自定义。

### 查看远程仓库

查看当前配置的远程仓库：

```bash
git remote -v
```

### 推送和拉取

- **推送本地分支到远程仓库**:
  ```bash
  git push origin branch-name
  ```
  - **首次推送并设置上游分支**:
    ```bash
    git push -u origin branch-name
    ```

- **拉取远程分支的更改到本地**:
  ```bash
  git pull origin branch-name
  ```

### 分支的远程操作

- **查看所有远程分支**:
  ```bash
  git branch -r
  ```
- **检出远程分支到本地**:
  ```bash
  git checkout -b branch-name origin/branch-name
  ```

### 克隆仓库

从远程仓库克隆一个项目到本地：

```bash
git clone https://github.com/username/repository.git
```

这将下载仓库的所有内容并创建一个新的目录。

仓库链接在github里找

<img src="git.assets/image-20241117152508476.png" alt="image-20241117152508476" style="zoom:67%;" />

**协作开发（Pull Request）**：

- 推送分支后，在 GitHub 上发起 Pull Request，通知其他开发者进行代码审查。
- 代码审查通过后合并到主分支。



###  **常见问题**

1. **Push 或 Pull 时提示需要输入用户名和密码**

   - 如果使用 HTTPS，可以配置 Git 记住密码：

     ```bash
     git config --global credential.helper store
     ```

     之后推送时输入一次用户名和密码，Git 会自动记住。

   - 如果频繁提示认证问题，建议改用 SSH 方式。

2. **SSH 连接失败**

   - 检查是否正确配置 SSH 密钥并添加到 GitHub。

   - 测试 SSH：

     ```bash
     ssh -T git@github.com
     ```

3. **分支名称冲突或不同**

   - 如果本地分支名称和远程默认分支不同（例如本地是 `master`，远程是 `main`），可以重命名本地分支：

     ```bash
     git branch -m master main
     ```

     然后推送：

     ```bash
     git push -u origin main
     ```



## 常用 Git 工作流程

不同的团队和项目可能采用不同的 Git 工作流程，以下是几种常见的工作流程。

### Feature 分支工作流程

1. **创建新功能分支**:
   ```bash
   git checkout -b feature/new-feature
   ```
2. **开发新功能**，多次提交。
3. **推送分支到远程**:
   ```bash
   git push -u origin feature/new-feature
   ```
4. **创建 Pull Request**，请求将新功能合并到主分支。
5. **代码审查**，讨论和修改。
6. **合并 Pull Request** 到主分支，删除功能分支。

### Git Flow

Git Flow 是一种更为复杂的工作流程，适用于发布周期较长的项目。

- **主分支（main/master）**：始终保持可发布状态。
- **开发分支（develop）**：集成所有功能分支的更改。
- **功能分支（feature/*）**：用于开发新功能。
- **发布分支（release/*）**：用于准备新版本的发布。
- **修复分支（hotfix/*）**：用于修复生产环境中的紧急问题。

Git Flow 通过命令行工具 [git-flow](https://github.com/nvie/gitflow) 进行管理，也可以手动操作。

## 使用 Git 与 VS Code 集成

Visual Studio Code（VS Code）与 Git 有良好的集成，方便进行版本控制操作。

### 配置 Git 在 VS Code 中

1. **确保 Git 已安装**，并且 VS Code 能够找到 Git 可执行文件。通常安装 Git 后，VS Code 会自动检测。
2. **打开项目**：在 VS Code 中打开你的 Git 项目文件夹。
3. **查看源代码管理面板**：点击左侧活动栏中的源代码管理图标（通常是一个分支图标）。

### 常用 Git 操作在 VS Code 中

- **查看更改**：在源代码管理面板中，可以看到已修改的文件。
- **暂存更改**：点击文件旁边的加号（+）按钮，将更改添加到暂存区。
- **提交更改**：在提交消息输入框中输入提交信息，然后点击勾号按钮提交。
- **查看历史**：可以安装扩展如 [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) 查看提交历史。
- **分支管理**：点击状态栏中的当前分支名称，可以创建、切换和管理分支。
- **解决冲突**：当有合并冲突时，VS Code 会高亮显示冲突区域，并提供工具来接受当前更改、接受被合并更改或手动编辑。

### 使用内置终端

VS Code 提供内置终端，可以直接在编辑器中运行 Git 命令：

1. 打开终端：`Ctrl + `` 或者通过菜单 `View` > `Terminal`。
2. 在终端中输入 Git 命令，如 `git status`、`git commit` 等。



## 常用 Git 命令总结

以下是一些常用的 Git 命令及其说明：

| 命令                          | 说明                                   |
| ----------------------------- | -------------------------------------- |
| `git init`                    | 初始化一个新的 Git 仓库。              |
| `git clone <repo>`            | 克隆一个远程仓库到本地。               |
| `git status`                  | 查看当前工作目录和暂存区的状态。       |
| `git add <file>`              | 将文件添加到暂存区。                   |
| `git commit -m "message"`     | 提交暂存区的更改。                     |
| `git log`                     | 查看提交历史。                         |
| `git branch`                  | 列出所有本地分支。                     |
| `git branch <branch>`         | 创建一个新分支。                       |
| `git checkout <branch>`       | 切换到指定分支。                       |
| `git checkout -b <branch>`    | 创建并切换到新分支。                   |
| `git merge <branch>`          | 合并指定分支到当前分支。               |
| `git remote add <name> <url>` | 添加一个远程仓库。                     |
| `git push <remote> <branch>`  | 推送本地分支到远程仓库。               |
| `git pull <remote> <branch>`  | 从远程仓库拉取并合并指定分支。         |
| `git fetch <remote>`          | 从远程仓库获取最新的更改，但不合并。   |
| `git stash`                   | 暂存当前工作目录的更改。               |
| `git stash pop`               | 恢复最近一次暂存的更改。               |
| `git reset --hard`            | 重置当前分支到最新提交，丢弃所有更改。 |
| `git tag <tag>`               | 给当前提交打标签。                     |
| `git remote -v`               | 查看远程仓库地址。                     |

---

##  参考资料

- [Git - 简明指南](http://rogerdudler.github.io/git-guide/index.zh.html)
- [图解 Git](http://marklodato.github.io/visual-git-guide/index-zh-cn.html)
- [廖雪峰 : Git 教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)
- [Learn Git Branching](https://learngitbranching.js.org/)
- [本篇文章的图片出处]([CyC2018/CS-Notes: :books: 技术面试必备基础知识、Leetcode、计算机操作系统、计算机网络、系统设计](https://github.com/CyC2018/CS-Notes))