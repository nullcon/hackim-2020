FROM node:8.12.0

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
#RUN npm install --only=production

# Bundle app source
COPY . .

RUN groupadd -r nodejs && useradd -m -r -g nodejs nodejs
# now run as new user nodejs from group nodejs
USER nodejs


EXPOSE 8080
CMD [ "npm", "start" ]

