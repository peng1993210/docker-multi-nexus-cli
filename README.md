docker配置nexus-cli教程

1,安装docker，windows或者linux都可以，鉴于使用window，所以用window为例
到 https://www.docker.com/get-started/  去下载window的docker descktop，然后安装

2，安装完成后，可以在C:\Users\Administrator目录建一个.wslconfig文件，内容根据自己的电脑资源配置，也可以不用这个文件（默认配置，内存只有物理内存的50%）：

[wsl2]
memory=56GB  # 最大内存限制，根据电脑自己修改
processors=11  # CPU核心数（其实就是线程数），根据电脑自己修改
swap=28GB  # 交换空间大小自己调整

3，下载docker编译文件和编排文件
    https://github.com/nexus-xyz/nexus-cli到这下载 Dockerfile和docker-compose.yaml 2个文件，
    新建一个文件夹将2个文件放在文件，文件名称最好取英文比如nexus-cli


4，打开docker desktop,在里面打开终端（右下角的+号），然后定位到nexus-cli文件夹，
  执行 docker build --no-cache -t nexus-cli   #这条命令会产生一个叫nexus-cli的镜像，可以在docker desktop的镜像页面看到
  执行 docker up -d   #这条命令会就更加里面的内容创建了一个叫 nexus-cli的容器并运行

  如果只是按照官方的docker-compose.yaml 这个文件编排，只会运行一个节点（node-id 需要自己修改）。


多节点一键运行：

上面的第4步，只需要执行docker build --no-cache -t nexus-cli #这条命令会产生一个叫nexus-cli的镜像，可以在docker desktop的镜像页面看到

然后我们修改docker-compose.yaml 这个编排文件，将多节点加入进去
内容差不多这样子：
version: '3.8'
services:
  nexus-cli-111:
    image: nexus-cli
    command:
    - start
    - --headless
    - --node-id=111
    restart: unless-stopped
  nexus-cli-112:
    image: nexus-cli
    command:
    - start
    - --headless
    - --node-id=112
    restart: unless-stopped

当我们执行docker up -d后，就会启动2个容器nexus-cli-111（节点是111），nexus-cli-112（节点是1112）

手动填写很麻烦，所有写一个python程序canshen_compose.py输出docker-compose.yaml ，只需要提交节点id的数组，将canshen_compose.py中的[111,112]替换成你的nodeid数组，运行这个py程序，会输出docker-compose.yaml文件

如何手动一次性获取所有的node-id，打开网站https://app.nexus.xyz/nodes，打开开发者工具，在控制台中将nodepoint复制出来，里面包含了所有的节点id，然后用vscode编辑快速得到所有的节点id数组。

    
