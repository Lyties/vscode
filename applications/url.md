## ubuntu

https://cdimage.ubuntu.com/daily-live/current/

## deepin

https://ci.deepin.com/repo/deepin/deepin-ports/deepin-arm64/



## 修改镜像

```shell
FROM alpine

WORKDIR /opt

RUN cp /etc/apk/repositories /etc/apk/repositories.bak
RUN echo -e 'https://mirrors.tuna.tsinghua.edu.cn/alpine/v3.18/main\nhttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.18/community' > /etc/apk/repositories
RUN apk update && apk upgrade
RUN apk add openjdk8
RUN apk add wget
```

## rocket-mq

Dockfiler

```markdown
FROM ubuntu

WORKDIR /opt

RUN sed -i 's/ports.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list

RUN apt update && apt upgrade -y && apt install openjdk-17-jdk/jammy-updates -y && apt install wget -y && apt install unzip -y
RUN apt install wget -y && apt install unzip -y
RUN wget https://dist.apache.org/repos/dist/release/rocketmq/5.1.3/rocketmq-all-5.1.3-bin-release.zip 
RUN unzip rocketmq-all-5.1.3-bin-release.zip

WORKDIR /opt/rocketmq-all-5.1.3-bin-release
RUN echo 'echo 'brokerIP1=${BROKER_IP}' >> conf/broker.properties' >> start.sh

RUN echo "nohup sh bin/mqnamesrv & " >> start.sh
RUN echo "sleep 3" >> start.sh
RUN echo "nohup sh bin/mqbroker -n localhost:9876 --enable-proxy -c conf/broker.properties &" >> start.sh
RUN echo "sleep 600" >> start.sh

EXPOSE 8080
EXPOSE 10909
EXPOSE 10911
EXPOSE 10912
EXPOSE 9876
CMD [ "/bin/bash", "start.sh" ]
```

docker-compose.yml

```yml
version: '3'
services:
  rocket-mq:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: rocket-mq
    tty: true
    environment:
      - BROKER_IP=192.168.2.194
    ports:
      - 8080:8080
      - 10909:10909
      - 10911:10911
      - 10912:10912
      - 9876:9876
  
```
