# 初试 Jenkins & Docker 持续集成 Django 项目

## 1. 搭建私有 docker 仓库

### 1.1 在仓库服务器上拉取 `registry` 镜像并运行

```
sudo docker run -d -p 16000:5000 --name docker-registry --restart=always -v /var/www/docker-registry:/var/lib/registry registry
```

> 容器数据会保存在 `/var/www/docker-registry` 目录下.
> 

### 1.2 在客户端修改 docker 配置

> 修改 docker 配置来允许访问 http 协议的 docker 仓库
> 

1. 在 `/etc/docker` 下新建文件: `daemon.json`:

    ```sh
    # 新建文件
    sudo vi /etc/docker/daemon.json
    ```
    
2. 在 json 文件中添加数据:

    ```json
    {
        "insecure-registries": [
            "176.122.188.100:16000"
        ]
    }
    ```

3. 保存新的配置后重启 docker (如果是在同一台服务器上, 确保私有仓库容器正在运行)

    ```sh
    sudo service docker restart
    ```

### 1.3 测试

1. 测试能否 push

    首先拉取 `alpine`镜像, 重新 `tag` 后 push 到私有仓库.

    ```sh
    # 首先拉取 alpine 镜像
    sudo docker pull alpine
    
    # 重新 tag
    sudo docker tag alpine:latest 176.122.188.100:16000/alpine:0.1
    
    # push 到私有仓库
    sudo docker push 176.122.188.100:16000/alpine:0.1
    
    ```
    
    如果 push 成功表示可用, 也可以访问 `http://176.122.188.100:16000/v2/_catalog` 查看, 或
    
    ```sh
    curl http://176.122.188.100:16000/v2/_catalog
    
    # api: /v2/<image name>/tags/list
    curl http://176.122.188.100:16000/v2/alpine/tags/list
    ```
    
2. 测试能否 pull

    ```sh
    # 首先把本地镜像删除
    sudo docker image rm 176.122.188.100:16000/alpine:0.1
    
    # pull
    sudo docker pull 176.122.188.100:16000/alpine:0.1
    ```
    
## 2. 运行 jenkins

```sh
sudo docker run -it -d -u root -p 16010:8080 -v /var/www/jenkins/data:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins  --restart=always jenkinsci/blueocean
```

查看管理员初始密码:

```sh
sudo docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## 3. 在 jenkins 上新建一个 webhook

_要求_: 
    
    1. Jenkins 需要安装 Git plugin
    2. Jenkins 服务器有公网 IP

### 3.1 配置 Jenkins Hook

1. 在 Jenkins `系统管理/系统设置/GitHub/GitHub Servers` 选项中, 点击高级添加 GitHub 服务器选项, 点击 `Override Hook URL` 来启用 Hook URL. 复制该 URL
2. 在 GitHub 上 项目 `settings/Webhooks/` 页面点击 `Add Webhook`, 添加新的 webhook 并自定义事件.
3. 配置 Jenkins 构建动作








```groovy
    stage('Precheck') {
            agent any 
            environment {
                MY_ENV = 'my_env'
            }
            steps {
                sh 'echo ${BUILD_NUMBER}'
                sh 'printenv'
            }
        }
```



























