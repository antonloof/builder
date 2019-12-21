FROM node:13.3

WORKDIR /home/docker/front
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install

ENTRYPOINT ["npm", "run-script", "build_dev"]
# CMD tail -f /dev/null
