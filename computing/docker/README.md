## Docker Cheat Sheet. By Augusto Damasceno.
> Copyright (c) 2023, 2024, Augusto Damasceno.  
> All rights reserved.  
> SPDX-License-Identifier: CC-BY-4.0  

## Contact
> [augustodamasceno@protonmail.com](mailto:augustodamasceno@protonmail.com)

# Basics
## Install

### Red Hat  
```bash
sudo dnf update -y
sudo dnf install -y dnf-plugins-core
sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo dnf install -y docker-ce docker-ce-cli containerd.io
sudo systemctl enable docker
sudo systemctl start docker
```

### Debian
```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo apt-get update
sudo apt-get install ./docker-desktop-<version>-<arch>.deb
```

### Arch
```bash
pacman -Syu
pacman -S --noconfirm docker
```

### Fedora
```bash
dnf update -y
dnf install -y docker
```

### MacOS
> Install with DMG file: https://docs.docker.com/desktop/install/mac-install/

### For FreeBSD use Jails
> https://docs.freebsd.org/en/books/handbook/jails/

## Start Service

### Debian, Arch, and Fedora 
```bash
sudo systemctl enable docker
sudo systemctl start docker
```
### MacOS
Run the app Docker

## Download Image
```bash
docker pull <IMAGE_NAME>
# Example
docker pull archlinux
```

## Create and run a container
```bash
docker run -it --name <NAME-OF-CONTAINER> archlinux
```

## List all containers
```bash
docker ps -a
```

## Start an existing container  
```bash
docker start <NAME-OF-CONTAINER_OR-ID>
```

## Connect to a running container  
```bash
docker exec -it <NAME-OF-CONTAINER_OR-ID> /bin/bash
```

## Execute a container changing kernel flags  
> This is limited and does not include all kernel parameters  
* IP forwarding  
```bash
docker run --name <NAME-OF-CONTAINER> --sysctl net.ipv4.ip_forward=1 <IMAGE>
```

## Shared Memory (Size of /dev/shm). The default if 64m. 
```bash
docker run --name <NAME-OF-CONTAINER> --shm-size=128m <IMAGE>
```

##  Memory and Swap  
```bash
docker run --name <NAME-OF-CONTAINER> --memory="4g" --memory-swap="4g" <IMAGE>
```
  
## Run a graphical application (host needs a X server)  
```bash
sudo docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --net=host <IMAGE>
<INSTALL A XSERVER LIKE XORG>
export DISPLAY=:0.0
<APPLICATION>
```

## Destroy a container
```bash
docker stop <NAME-OF-CONTAINER_OR-ID>
docker rm <NAME-OF-CONTAINER_OR-ID>
```

## Share volume in a new container
```bash
docker run -it --name <NAME-OF-CONTAINER_OR-ID> -v <HOST-PATH>:<CONTAINER-PATH> <IMAGE_NAME>
```

## Share volume in an existing container
```bash
docker exec -it <NAME-OF-CONTAINER_OR-ID> -v <HOST-PATH>:<CONTAINER-PATH>
```

## Volume synchonization
> Volume synchronization problems can occur between the host and container.  
> To avoid this, you can use rsync to sync files to the volume and use it as read-only inside the docker  
>  or copy from the volume to a container system partition.  

```bash
rsync -a --delete <HOST-PATH> <VOLUME-PATH>
```

## Forward host port to container port
```bash
docker run -p <HOST-PORT>:<CONTAINER-PORT> <IMAGE_NAME>
```

## Save the Docker Image to a File
```bash
docker save -o <image_name>.tar <image_name>:<tag>
```

## Load Docker image from a file
```bash
docker load -i <image_name>.tar
```

## Docker compose samples
* https://github.com/docker/awesome-compose

## Docker compose PostgreSQL database application example
### Write this content in the file postgres_example.yml
```bash
services:
  postgres:
    container_name: postgres
    image: postgres:latest
    environment:
      POSTGRES_DB: db
      POSTGRES_USER: root
      POSTGRES_PASSWORD: 123456
    ports:
      - "5432:5432"
    restart: always
```
### Run
```bash
docker-compose -f postgres_example.yml up -d
```
### Access the container shell  
```bash
docker exec -it postgres  /bin/bash
```
### Run PostgreSQL commands
```bash
psql -d db -U root
```

## References  
* https://docs.docker.com/engine/reference/commandline/cli/  
* https://docs.docker.com/compose/reference/  
* https://linux.die.net/man/1/rsync