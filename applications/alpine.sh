# 拉取alpine镜像
docker pull alpine

# 运行并进入容器
docker run -itd --name alpine-java alpine

docker exec -it alpine-java sh

# 更换软件源
cp /etc/apk/repositories /etc/apk/repositories.bak
echo -e 'https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.18/main\nhttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.18/community' > /etc/apk/repositories

# 安装OpenJDK等
apk update

apk add openjdk8 busybox tzdata curl

# 修改时间 非必要 如果时间不对 再调整
# 查看时间是否正确
date

# 不正确则修改
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 修改Java时区
echo Asia/Shanghai > /etc/timezone

# 清理软件包和缓存
apk del tzdata

rm -rf /tmp/* /var/cache/apk/*

# 封装镜像
docker commit alpine-java yourname/alpine-java

# 推送到仓库(需要先配置账号)
docker push yourname/alpine-java

