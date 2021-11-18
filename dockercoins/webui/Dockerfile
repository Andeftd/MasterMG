FROM node:alpine
LABEL author="anderson.furtado"
RUN apk update && apk upgrade
WORKDIR /usr/app/
ADD files/ .
ADD . .
RUN npm install express ; npm install redis
EXPOSE 80
CMD ["node", "webui.js"]