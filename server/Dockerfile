FROM node

RUN mkdir -p /home/server-health
RUN mkdir -p /home/server-health/server

COPY . /home/server-health/server

WORKDIR /home/server-health/server

RUN npm install

CMD ["node","/home/server-health/server/server"]