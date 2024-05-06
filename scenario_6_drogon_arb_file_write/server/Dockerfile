FROM ubuntu:18.04

# Update and install necessary packages
RUN apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends software-properties-common \
    sudo curl wget cmake pkg-config locales git gcc-8 g++-8 \
    openssl libssl-dev libjsoncpp-dev uuid-dev zlib1g-dev libc-ares-dev \
    postgresql-server-dev-all libmariadbclient-dev libsqlite3-dev \
    libboost-all-dev \
    && rm -rf /var/lib/apt/lists/* \
    && locale-gen en_US.UTF-8

# Install Boost manually if necessary
RUN apt-get update && apt-get install -y libboost-system-dev libboost-thread-dev libboost-coroutine-dev libboost-filesystem-dev libboost-date-time-dev libboost-chrono-dev

# Set environment variables
ENV LANG=en_US.UTF-8 \
    LANGUAGE=en_US:en \
    LC_ALL=en_US.UTF-8 \
    CC=gcc-8 \
    CXX=g++-8 \
    AR=gcc-ar-8 \
    RANLIB=gcc-ranlib-8 \
    IROOT=/install

# Define Drogon root directory
ENV DROGON_ROOT="$IROOT/drogon"

# Clone Drogon repository and checkout the specific tag
RUN git clone https://github.com/an-tao/drogon $DROGON_ROOT \
    && cd $DROGON_ROOT \
    && git checkout v1.7.0

# Build Drogon
WORKDIR $DROGON_ROOT
RUN ./build.sh

# Copy the application source code into the container
COPY app/ /app

# Compile the application
WORKDIR /app
RUN mkdir build && cd build && cmake .. && make

# Expose port 8848 for the application
EXPOSE 8848

# Command to run your application
CMD ["/app/build/myapp"]

