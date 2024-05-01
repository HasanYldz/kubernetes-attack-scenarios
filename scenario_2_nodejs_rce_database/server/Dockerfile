# Use the official Node.js 18 image from Docker Hub as the base image
FROM node:18-slim

# Install necessary packages
RUN apt-get update && \
    apt-get install -y bash netcat-openbsd && \
    # Install MySQL client
    apt-get install -y default-mysql-client && \
    rm -rf /var/lib/apt/lists/*

# Copy all files from the project directory to the Docker image
COPY . .

# Install Node.js dependencies defined in package.json
RUN npm install

# Expose the port the app runs on
EXPOSE 4242

# Define the command to run the app
CMD ["npm", "start"]

