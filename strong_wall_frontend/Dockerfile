FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install
RUN npm install http-proxy-middleware --save
RUN npm install react-google-recaptcha

COPY . .

CMD npm start
# CMD sleep 10000