FROM node:slim

MAINTAINER Seel 459745355@qq.com

RUN npm install gitbook-cli -g
RUN gitbook -V

EXPOSE 4000

RUN mkdir /work
COPY book.json /root/
RUN cd /root/ && \
    gitbook install
COPY init.sh /root/
COPY copyPluginAssets.js /root/.gitbook/versions/3.2.3/lib/output/website/
RUN chmod 777 /root/init.sh

WORKDIR "/work"
CMD ["/bin/bash", "-c", "/root/init.sh"]
