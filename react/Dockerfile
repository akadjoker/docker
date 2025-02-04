 
FROM node:18-bullseye-slim

 
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

 
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    build-essential \
    openjdk-11-jdk \
    python3 \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


 
RUN npm install -g \
    react-native-cli \
    expo-cli \
    @react-native-community/cli \
    typescript
 
WORKDIR /project

 
EXPOSE 3000 19000-19002

 
CMD ["/bin/bash"]
