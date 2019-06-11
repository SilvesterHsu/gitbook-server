FROM node:slim

MAINTAINER Seel 459745355@qq.com
# install gitbook
RUN npm install gitbook-cli -g
RUN gitbook -V

RUN mkdir /work
COPY book.json /srv/
RUN cd /srv/ && \
    gitbook install
COPY copyPluginAssets.js /root/.gitbook/versions/3.2.3/lib/output/website/
COPY init.sh /root/
RUN chmod 777 /root/init.sh

WORKDIR "/work"
EXPOSE 4000
CMD ["/bin/bash", "-c", "/root/init.sh"]
