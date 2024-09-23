---
title: 从零开始：使用 Hexo 搭建个人博客
type: hexoblog
abbrlink: 18015
date: 2024-09-10 15:22:23
expires: 2025-09-10 23:59:59
tags:
- 教程
- Hexo
cover: https://image.179.life/images/hexoblog_cover.png
categories:
- - 软件
  - 记录
---

{% note yellow fa-circle-exclamation %}
注意：本教程仅适用于 Windows 系统
{% endnote %}

## 前言
可能不少人都想搭建一个个人博客，但是经常可能不知道用什么框架/方法，或者遇到一些踩坑 / 对于一些步骤不知道怎么做的情况。我就打算做一个整合的教程，用于方便大家从零开始搭建个人博客~（Hexo）

因为我自己使用了 Hexo 搭建个人博客，所以把搭建的教程分享一下吧~

本教程参考[这里](https://blog.csdn.net/yaorongke/article/details/119089190)。
### 什么是 Hexo？
以下使用 [Hexo 官网](https://hexo.io/)的介绍：
Hexo 是一个快速、简洁且高效的博客框架。 Hexo 使用 Markdown（或其他标记语言）解析文章，在几秒内，即可利用靓丽的主题生成静态网页。
### 为什么使用 Hexo ？
使用 Hexo 的博客配置简单，自带主题丰富，而且甚至可以不需要服务器或者个人域名就能够让大家访问。对于个人来讲简单方便，也比较省钱（？）
如果你想的话也可以随意修改 Hexo 源代码或自定义自己的主题。
## 开始
### 准备工作
使用 Hexo 搭建个人博客首先需要一个 Github 账号，以及 Node.js 环境。
#### 注册 Github 账号
如果你没有自己的 Github 账号的话，可以访问 [Github 官网](https://github.com)并注册一个账号。
{% note yellow fa-circle-exclamation %}
Github 官网在国内有软墙，部分情况可能需要 VPN 才能登上。
{% endnote %}
#### 下载安装 Node.js
你可以在终端使用如下指令来查看是否安装了 Node.js 以及版本：
```cmd
node -v
```
{% note yellow fa-circle-exclamation %}
Node.js 版本需要至少高于 10.13, 推荐使用 Node.js 12.0 以上版本
{% endnote %}
**以下是不同方法安装 Node.js 的教程：**
{% tabs testunique %}
<!-- tab 包管理器-->
按 `win` + `r` 键打开运行窗口，输入 `powershell` 打开 Powershell 终端，并将如下代码复制，粘贴进 Powershell 输入框。
也可以一行一行的输入而非复制。
**注意：以 `#` 开头的行是注释行，不需要输入。**
```powershell
# layouts.download.codeBox.installsFnm
winget install Schniz.fnm

# layouts.download.codeBox.fnmEnvSetup
fnm env --use-on-cd | Out-String | Invoke-Expression

# layouts.download.codeBox.downloadAndInstallNodejs
#                             ↓ 大版本号，2024年9月10日最新版本为 v22.8.0
fnm use --install-if-missing 22

# layouts.download.codeBox.verifiesRightNodejsVersion
node -v # layouts.download.codeBox.shouldPrint

# layouts.download.codeBox.verifiesRightNpmVersion
npm -v # layouts.download.codeBox.shouldPrint
```
<!-- endtab -->

<!-- tab 安装程序-->
{% btn regular::Node.js 安装程序::https://nodejs.org/dist/v22.8.0/node-v22.8.0-x64.msi::fa-regular fa-hexagon-check %}

1. 点击上方按钮或[访问官网](https://nodejs.org/zh-cn/download/prebuilt-installer)下载当前（2024年9月10日）最新版本的 Node.js（v22.8.0）
2. 双击打开刚刚下载的安装程序，此时你应该看到如下窗口：![Node.js 安装窗口](https://image.179.life/images/nodejs-install1.png)
3. 点击 `Next` 按钮继续，接下来会让你接受安装协议，勾选 `I accept the terms in the License Agreement` 并且点击 `Next` 继续。
4. 安装程序让你选择程序安装路径，可以随便找一个路径安装。
5. 接下来一路按 `Next` 安装就行。
<!-- endtab -->

<!-- tab 二进制文件-->
{% btn regular::Node.js 二进制文件::https://nodejs.org/dist/v22.8.0/node-v22.8.0-win-x64.zip::fa-regular fa-hexagon-check %}

1. 点击上方按钮或[访问官网](https://nodejs.org/zh-cn/download/prebuilt-binaries)下载当前（2024年9月10日）最新版本的 Node.js（v22.8.0）
2. 将下载到的 .zip 文件解压到一个合适的路径。
3. 按 `win` + `r` 键，输入 `sysdm.cpl` 打开系统属性设置，选择 `高级` > `环境变量`。
4. 在 `系统变量` 栏的 `Path` 环境变量下点击 `编辑`，在列表下添加一个新项，值为你的**Node.js 二进制文件路径**。
![编辑环境变量 Path](https://image.179.life/images/nodejs-install2.png)
{% note yellow fa-circle-exclamation %}
如果你的 `Path` 变量编辑设置不长这样，而是一个输入框的话，在 `变量值` 的最后输入一个**英文分号**，然后复制你的**Node.js 二进制文件路径**。
{% endnote %}
<!-- endtab -->
{% endtabs %}
##### 完成安装
在终端里使用如下代码查看安装情况：
```cmd
node -v
npm -v
```
如果运行没有错误并且输出了 Node.js 和 npm 的版本，说明 Node.js 已经安装成功啦。

{% note yellow fa-circle-exclamation %}
注意：在刚安装好程序后需要新开一个终端窗口才可以正常执行命令，在安装 Node.js 之前的终端窗口执行命令会提示错误。
{% endnote %}

{% folding yellow::输入 npm -v 出现了无法加载文件 [url]，因为在此系统上禁止运行脚本的解决方法 %}
1. 使用管理员身份运行 PowerShell
2. 在 PowerShell 终端输入以下命令：
```PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```
1. 确定。
2. 再次输入 `npm -v`，此时应该输出 npm 的版本。
**如果还是不可以的话，可以去网上搜一搜解决方法。**
{% endfolding %}

#### 安装 Git
在 [Git 官网](https://git-scm.com/)可以安装到最新版的 Git.
{% btn regular::64x Git 安装包::https://github.com/git-for-windows/git/releases/download/v2.46.0.windows.1/Git-2.46.0-64-bit.exe::fa-regular fa-hexagon-check %}
点击上方按钮下载当前（2024年9月10日）最新版本的 Git.

Git 的安装方式类似 Node.js，如果不清楚可以去网上搜教程。我就先不写啦（溜走）

---

### 安装 Hexo
在终端输入以下命令安装 Hexo。
```cmd
npm install -g hexo-cli
```

在文件资源管理器选择一个合适的路径后，右键选择 `在终端中打开` 或者点击路径框，输入 cmd 打开终端窗口，输入以下指令创建一个新项目 `new_project` 并且初始化:
```cmd
hexo init new_project
cd new_project
npm install
```
注：`npm install` 用于安装 hexo 所需的基本模块。

### 本地启动 Hexo 服务
在 Hexo 项目文件夹使用以下命令启动 Hexo 服务
``` powershell
# 生成网页页面
hexo g
# 启动本地服务器
hexo s
```

此时访问 https://localhost:4000 应该能够看到如下画面：
![Hexo 初始页面](https://image.179.life/images/hexo-hello.png)

那么恭喜你已经成功搭建好了 Hexo 个人服务端并且可以在本地访问了！

## 配置 & 发布

### 配置 Hexo
对于 Hexo 的配置。可以查看 [Hexo 官方文档](https://hexo.io/zh-cn/docs/setup) 的 `配置` 页面。

### 创建文章
输入以下命令来创建一个 Hexo 文章：
``` powershell
# hexo new 页面模板 页面标题
# post 意思是发布的文章
hexo new post 文章标题
```
此时会在 Hexo 项目文件夹下的 `source/_pages` 目录生成一个名为 `测试文章.md` 的文件，且里面有如下内容：
```markdown
---
title: 文章标题
date: 2024-09-10 21:49:35
tags:
---
```
你可以在第二个 `---` 外写上文章的主要内容，格式为 [markdown](https://markdown.com.cn/cheat-sheet.html)。

在两个 `---` 中间的内容是文章的 `Front-matter`，可以访问[官方文档](https://hexo.io/zh-cn/docs/front-matter)以及你的主题文档来进行设置。

此时访问 https://localhost:4000 ，应该能够看到你的文章已经显示出来了。

### 切换主题
访问 [Hexo Themes](https://hexo.io/themes/) 来选择想要的主题，并且在主题网页里进行安装。

当选择好主题后，进入你 Hexo 项目文件夹的 `_config.yml` 调整配置
```YAML
theme: theme # 你选择的主题名称
```
将 `theme` 的值修改为你选择的主题的名称。

### 将个人博客发布至 Github Pages

#### 添加你的 github.io 仓库
登录你的 Github 账号，在个人资料页面的 `Respositories` 里点击 `New` 按钮
![新建一个仓库](https://image.179.life/images/githubio1.jpg)
填写 `Repository name` 项为 `你的用户名.github.io`
![填写 Repository name 项](https://image.179.life/images/githubio2.jpg)

{% notel warning fa-circle-exclamation 注意 %}
仓库需要是 public 才可被访问 github pages，除非你是 pro 用户。
{% endnotel %}

此时你应该可以看到如下画面：
![空仓库界面](https://image.179.life/images/githubio4.jpg)
选择红框框起来的 `HTTPS`，在箭头指向的位置点击复制按钮，可以将你的 github.io 项目的地址复制到剪切板。
![复制仓库地址](https://image.179.life/images/githubio3.png)

#### 发布博客至你的 github.io 仓库
在命令行安装 `hexo-deployer-git`:
```powershell
npm install hexo-deployer-git --save
```
如果需要让 Hexo 使用你的 github 项目，需要获取个人 token：
{% folding cyan::获取个人 token 方法 %}
点击右上角的头像，选择 `Settings`。
![设置](https://image.179.life/images/githubio5.jpg)
在设置下方找到 `Developer settings`。
![找到 Developer settings](https://image.179.life/images/githubio6.jpg)
根据图内框选处选择生成新的 token。
![找到 Developer settings](https://image.179.life/images/githubio7.jpg)
设置 token 的名字、期限和适用范围。
![找到 Developer settings](https://image.179.life/images/githubio8.jpg)
点击复制按钮复制 token 的值 （注意： token 只会显示一次）
![复制 token 内容](https://image.179.life/images/githubio9.jpg)
{% note warning fa-circle-exclamation %}
我用的是旧版 token 生成方法，如果你了解新版 token 的生成，也可以去使用新版。
{% endnote %}
{% endfolding %}

在 Hexo 项目文件夹下的 `_config.yml` 配置项里替换或增加如下内容：
```YAML
deploy:
  type: git
  repo: 你的 github.io 项目地址
  branch: main
  token: 你的 github token
```

此时执行以下代码将 Hexo 内容发布
``` powershell
# 清除 public 文件夹缓存
hexo clean
# 生成 hexo 文件
hexo g
# 推送内容至 github.io
hexo d
```

等待 0 ~ 10 分钟 Github pages 加载，访问 https://你的用户名.github.io/，若出现你的网页内容，说明部署成功。
如果等待了 10 分钟还是无法访问，可以看看下面的内容：
{% folding cyan::Github Pages 出现 404 %}
假如你等待了 10 分钟后再访问你的页面依然提示 404 的话，可能是以下原因导致的：
##### 仓库不为 public
可以检查一下你的仓库可见性是否为 Public，也就是中间上方显示的仓库名称右边小框里的内容。
##### Github pages 分支不为 main
前往你 github.io 仓库里的 `Settings` > `Pages` 设置查看 `Build and deployment` 栏位中的 `Branch` 是否为 `main`，如果是 `None`，就调整为 `main`。
![调整分支设置](https://image.179.life/images/githubio10.jpg)
之后再次等待一段时间看看可不可以访问。
如果还是不行的话，可以看看上方图片写的站点文件夹是否为 `/` 或是你在 Hexo 项目文件夹下的 `_config` 设置的 `root` 项值。

还是不行的话，只好建议把详细内容放到网上搜索尝试解决了 xwx。（或者也可以发到评论区里）
{% endfolding %}

### 绑定个人域名

如果你想把你部署在 Github Pages 的 Hexo 个人博客放到自己的域名下，可以看看如下内容：

前往你 github.io 仓库里的 `Settings` > `Pages` 设置查看 `Custom domain` 栏位，填写自定义域名为你的域名并且勾选 `Enforce HTTPS` 用来强制使用 HTTPS 协议。
![修改自定义域名](https://image.179.life/images/githubio11.jpg)

在你的 Hexo 项目文件夹下的 `source` 文件夹下创建一个名为 `CNAME` 的文件（注意，完整文件名就是 `CNAME`），然后在第一行写下你的域名，例如：
```CNAME
blog.xzadudu179.top
```
注意 `CNAME` 里只能写一个域名哦。
之后执行以下代码将新增的内容发布：
```powershell
hexo g
hexo d
```
等待 0 ~ 10 分钟后访问你填写的域名地址，如果成功访问并且出现你的网页内容，说明部署成功。

如果出现了 404 的问题，可以看看上一栏 Github Pages 出现 404 问题的折叠块。

## 完成

现在你应该搭建好了一个个人博客了！可以添加新文章/新功能啦~

如果遇到任何问题，请在评论区发评论或者发邮箱到 terra179@163.com / me@xzadudu179.top 哦。