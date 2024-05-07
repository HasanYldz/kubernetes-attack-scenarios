# Use an updated JDK base image that supports Java 11, for example
FROM openjdk:11-jdk-slim

# Install Maven
RUN apt-get update && apt-get install -y maven

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the working directory
COPY . .

# Build the application using Maven
RUN mvn clean install spring-boot:repackage

# Expose the port the app runs on
EXPOSE 8090

# Run the application
CMD ["java", "-jar", "-Dserver.port=8090", "target/SpringBreakVulnerableApp-1.0.jar", "--debug"]

