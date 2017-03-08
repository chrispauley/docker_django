# docker-express

This is a bare minimum Django server app that is wrapped in a Docker image.

## Installation
Install Docker
Git clone this repo


## Create the image
docker build -t demoapp .


### Create the Dockerfile
The contents of the Dockerfile build script will start with python 3.4

```
FROM python:3.4

# Set PYTHONUNBUFFERED so output is displayed in the Docker log
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the application's code
COPY . /usr/src/app

# Run the app
RUN chmod +x ./run_app.sh
CMD ["./run_app.sh"]
```

Create and run a container from the image. This will build a container with the tag "demoapp" and the dot indicates the Dockerfile location.
```
docker build -t demoapp .
```

## View the image on your machine
```
docker images
```

## Run and test your image in a container
The -ti for "terminal interactive" allows you to use ^C to kill the process.
The -p 8000:8000 options indicate the exposedPort:internalPort accessiblility.
The express-helloworld option indicates the image name to create a container.
```
docker run -d -p 8000:8000 demoap
```
Switch to your browser and get: [http://127.0.0.1:8000/](http://127.0.0.1:8000)


## Clean up
Kill the running process
```
docker kill <containerId>
```

List container instances to be removed
```
docker ps -a
```

Remove container instances
docker rm <container id>
```
docker rm ea0ea
```

Remove images
```
docker rmi demoapp

```

## Bonus
Add to your github repo
```
git init
git add .
## create your github repo
git remote add origin https://github.com/chrispauley/docker_django.git
git push origin master
```

### Deploy to a Docker Host
Login to your server host. At a terminal window
```
git clone https://github.com/chrispauley/docker_django.git
cd docker-express
docker build -t demoapp .
docker run -ti -p 8000:8000 demoapp
```
Make sure your server host port 8000 is accessible and test it:
 [http://192.168.0.84:8000/](http://192.168.0.84:8000/)
Update a cname record on your domain and your up.

## Clean Up
Remember to clean up your containers and images!


### Deploy to Docker Hub
First tag your image with your hub.docker.com user account name:
```
docker tag a234b052333a chrispauley/guestbook
docker images
```

Next, login and push to Docker hub
```
docker push chrispauley/guestbook
```

Now you can deploy using a docker pull command on a docker host server.
Switch to the docker host machine.
```
docker run -ti -d -p 8000:8000 chrispauley/guestbook
```
Test it from your browser and enjoy.

## Docker Compose
- docker-compose build
- docker-compose up
- docker-compose kill <containerId>
- docker-compose stop <containerId>
- docker-compose rm <containerId>
- docker-compose env

## Docker machine
- docker-machine create <hostId>
  creates a new docker host (like on AWS, Rackspace, etc.)
- docker-machine ls
- docker-machine ssh <hostId>
  connects to the host using ssh
- docker-machine rm <hostId>
  destroys a host

### Supported Providers
- amazonec2
- azure
- digitalocean
- exoscale
- google
- openstack
- rackspace
- softlayer
- virtualbox
- vmwarecloudair
- vmwarevsphere
