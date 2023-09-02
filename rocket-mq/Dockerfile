FROM ubuntu

WORKDIR /opt

RUN sed -i 's/ports.ubuntu.com/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list

RUN apt update && apt upgrade -y && apt install openjdk-17-jdk/jammy-updates -y && apt install wget -y && apt install unzip -y
RUN apt install wget -y && apt install unzip -y
RUN wget https://dist.apache.org/repos/dist/release/rocketmq/5.1.3/rocketmq-all-5.1.3-bin-release.zip 
RUN unzip rocketmq-all-5.1.3-bin-release.zip

WORKDIR /opt/rocketmq-all-5.1.3-bin-release

ADD rocketmq-dashboard-1.0.1-SNAPSHOT.jar rocketmq-dashboard.jar

RUN echo 'echo 'brokerIP1='${BROKER_IP}'' >> conf/broker.properties' >> start.sh
RUN echo "nohup sh bin/mqnamesrv & " >> start.sh
RUN echo "sleep 3" >> start.sh
RUN echo "nohup sh bin/mqbroker -n localhost:9876 --enable-proxy -c conf/broker.properties &" >> start.sh
RUN echo "java -jar rocketmq-dashboard.jar --server.port=8085" >> start.sh
#RUN echo "sleep 600" >> start.sh


EXPOSE 8080
EXPOSE 10909
EXPOSE 10911
EXPOSE 10912
EXPOSE 9876
CMD [ "/bin/bash", "start.sh" ]