# Docker


## 介绍

Docker 是一个开源的应用容器引擎，它允许开发者将应用及其依赖打包进一个轻量级、可移植的容器中，然后在任何支持 Docker 的平台上运行。
 它的核心目标是“**一次构建，到处运行**”。

由于不同的机器有不同的操作系统，以及不同的库和组件，在将一个应用部署到多台机器上需要进行大量的环境配置操作。

Docker 主要解决环境配置问题，它是一种虚拟化技术，对进程进行隔离，被隔离的进程独立于宿主操作系统和其它隔离的进程。使用 Docker 可以不修改应用程序代码，不需要开发人员学习特定环境下的技术，就能够将现有的应用程序部署在其它机器上。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/011f3ef6-d824-4d43-8b2c-36dab8eaaa72-1.png" width="400px"/> </div><br>

**核心特点：**

- **镜像（Image）**：是一个只读的模板，包含运行应用所需的代码、库、依赖等。
- **容器（Container）**：镜像的一个运行实例，是一个隔离的环境。
- **Dockerfile**：用于构建镜像的脚本文件。
- **Docker Hub**：一个公共的镜像仓库，也可以使用私有仓库。

### 与虚拟机的比较

虚拟机也是一种虚拟化技术，它与 Docker 最大的区别在于它是通过模拟硬件，并在硬件上安装操作系统来实现。

<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/be608a77-7b7f-4f8e-87cc-f2237270bf69.png" width="500"/> </div><br>

### 启动速度

启动虚拟机需要先启动虚拟机的操作系统，再启动应用，这个过程非常慢；

而启动 Docker 相当于启动宿主操作系统上的一个进程。

### 占用资源

虚拟机是一个完整的操作系统，需要占用大量的磁盘、内存和 CPU 资源，一台机器只能开启几十个的虚拟机。

而 Docker 只是一个进程，只需要将应用以及相关的组件打包，在运行时占用很少的资源，一台机器可以开启成千上万个 Docker。

## 优势

除了启动速度快以及占用资源少之外，Docker 具有以下优势：

### 更容易迁移

提供一致性的运行环境。已经打包好的应用可以在不同的机器上进行迁移，而不用担心环境变化导致无法运行。

### 更容易维护

使用分层技术和镜像，使得应用可以更容易复用重复的部分。复用程度越高，维护工作也越容易。

### 更容易扩展

可以使用基础镜像进一步扩展得到新的镜像，并且官方和开源社区提供了大量的镜像，通过扩展这些镜像可以非常容易得到我们想要的镜像。

## 使用场景

### 持续集成

持续集成指的是频繁地将代码集成到主干上，这样能够更快地发现错误。

Docker 具有轻量级以及隔离性的特点，在将代码集成到一个 Docker 中不会对其它 Docker 产生影响。

### 提供可伸缩的云服务

根据应用的负载情况，可以很容易地增加或者减少 Docker。

### 搭建微服务架构

Docker 轻量级的特点使得它很适合用于部署、维护、组合微服务。

## 镜像与容器

镜像是一种静态的结构，可以看成面向对象里面的类，而容器是镜像的一个实例。

镜像包含着容器运行时所需要的代码以及其它组件，它是一种分层结构，每一层都是只读的（read-only layers）。构建镜像时，会一层一层构建，前一层是后一层的基础。镜像的这种分层存储结构很适合镜像的复用以及定制。

构建容器时，通过在镜像的基础上添加一个可写层（writable layer），用来保存着容器运行过程中的修改。

### 镜像构成（分层结构）

每个镜像是多层构成的，比如：

```
FROM ubuntu:20.04     <- 基础层
RUN apt-get update    <- 新增一层
RUN apt install nginx <- 又新增一层
COPY . /app           <- 又一层
```

这些层具有缓存机制，因此只要上一层没变，Docker 会复用已有层来提高构建效率。

------

### 镜像与容器的区别

| 对象              | 说明                                   |
| ----------------- | -------------------------------------- |
| 镜像（Image）     | 模板：不可变，类似于软件安装包         |
| 容器（Container） | 镜像的运行时实例，可修改状态、产生数据 |



<div align="center"> <img src="https://cs-notes-1256109796.cos.ap-guangzhou.myqcloud.com/docker-filesystems-busyboxrw.png"/> </div><br>



------

## 安装 Docker

参考官网：https://docs.docker.com/get-docker/
 主要支持 Windows、macOS、Linux 等系统，安装后可通过命令 `docker --version` 检查是否安装成功。

------

## 常用命令介绍

### 镜像相关

```bash
# 搜索镜像（如nginx）
docker search nginx

# 拉取镜像
docker pull nginx

# 查看本地镜像
docker images

# 删除镜像
docker rmi 镜像ID或名称
```

### 容器相关

```bash
# 运行容器
docker run -d -p 8080:80 --name mynginx nginx
# -d 后台运行
# -p 映射端口（宿主机:容器）
# --name 给容器起个名字

# 查看正在运行的容器
docker ps

# 查看所有容器（包含停止的）
docker ps -a

# 停止容器
docker stop 容器名或ID

# 启动容器
docker start 容器名或ID

# 进入容器交互终端
docker exec -it 容器名或ID bash

# 删除容器
docker rm 容器名或ID
```



------

## 实战：从构建到部署一个 Web 应用

下面以构建一个简单 Node.js 应用为例，展示完整流程。

### 示例项目结构：

```
myapp/
│
├── app.js
├── package.json
└── Dockerfile
```

### `app.js`

```js
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => res.send('Hello Docker!'));
app.listen(port, () => console.log(`Server running on port ${port}`));
```

### `package.json`

```json
{
  "name": "myapp",
  "version": "1.0.0",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

### Dockerfile

```dockerfile
# 基础镜像
FROM node:18

# 创建工作目录
WORKDIR /usr/src/app

# 拷贝依赖清单
COPY package*.json ./

# 安装依赖
RUN npm install

# 拷贝应用代码
COPY . .

# 开放端口
EXPOSE 3000

# 启动命令
CMD ["node", "app.js"]
```

### 构建镜像

```bash
docker build -t my-node-app .
```

### 运行容器

```bash
docker run -d -p 3000:3000 --name node-test my-node-app
```

此时访问浏览器 `http://localhost:3000` 即可看到输出。

------

## 使用 Docker Volume 实现持久化

Docker 中容器一旦销毁，其中的数据会丢失，因此常用 volume 保存持久化数据。

### 示例：MySQL 容器挂载本地目录

```bash
docker run -d \
  --name mydb \
  -e MYSQL_ROOT_PASSWORD=root \
  -v /my/local/mysql:/var/lib/mysql \
  mysql:8
```

容器内 `/var/lib/mysql` 的数据将映射到宿主机 `/my/local/mysql`，保证重启后数据不丢。

------

## 多容器部署：Docker Compose 示例

### 项目结构

```
myapp/
├── docker-compose.yml
├── app/
│   ├── app.js
│   ├── package.json
│   └── Dockerfile
└── db/
```

### docker-compose.yml

```yaml
version: '3.8'
services:
  web:
    build: ./app
    ports:
      - "3000:3000"
    depends_on:
      - db

  db:
    image: mysql:8
    environment:
      MYSQL_ROOT_PASSWORD: root
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

### 构建并启动容器组

```bash
docker-compose up -d
```

------

## 容器之间通信

在 Compose 中，各服务默认加入同一网络，可以直接通过服务名访问：

```js
// 在 web 服务代码中
mysql.createConnection({
  host: 'db',   // Compose 中的服务名
  user: 'root',
  password: 'root'
});
```

------

## Docker 常用工具和高级功能

- **Docker Volume**：管理数据持久化
- **Docker Network**：自定义网络让容器之间安全通信
- **Docker Compose**：本地开发和测试的神器
- **Dockerfile 构建优化**：
  - 多阶段构建（multi-stage）
  - 合理利用缓存层
  - 使用 `.dockerignore` 排除无关文件

------

## 清理命令合集

```bash
# 清除所有停止的容器
docker container prune

# 清除未使用的镜像
docker image prune

# 清理所有未使用的数据（包括镜像、容器、卷等）
docker system prune -a
```

------



## 参考资料

- [DOCKER 101: INTRODUCTION TO DOCKER WEBINAR RECAP](https://blog.docker.com/2017/08/docker-101-introduction-docker-webinar-recap/)
- [Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [Docker container vs Virtual machine](http://www.bogotobogo.com/DevOps/Docker/Docker_Container_vs_Virtual_Machine.php)
- [How to Create Docker Container using Dockerfile](https://linoxide.com/linux-how-to/dockerfile-create-docker-container/)
- [理解 Docker（2）：Docker 镜像](http://www.cnblogs.com/sammyliu/p/5877964.html)
- [为什么要使用 Docker？](https://yeasy.gitbooks.io/docker_practice/introduction/why.html)
- [What is Docker](https://www.docker.com/what-docker)
- [持续集成是什么？](http://www.ruanyifeng.com/blog/2015/09/continuous-integration.html)

