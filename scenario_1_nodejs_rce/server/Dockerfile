FROM node:18-slim

# Ensure bash is installed
RUN apt-get update && \
    apt-get install -y bash netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN npm install

CMD ["npm", "start"]

