#!/bin/bash

# checks if container name is supplied
if [ "$#" -eq 0 ]
then
    echo "Please specify a container name!"
    exit 1
fi

# checks if container exist
if [ "$(docker ps -a -q -f name=$1)" ]
then
    echo "An existing container with the name $1 was found!"
    
    # checks if container is running and stop it if it is
    if [ "$(docker ps -aq -f status=running -f name=$1)" ]
    then
        echo "Stopping container..."
        docker stop $1
	echo "Container stopped."
    fi

    # removes stopped container
    echo "Removing stopped container..."
    docker rm -f $1
    echo "Container removed."
fi

# pull the latest image
docker pull tjtanjin/tele-qr:master

# run new docker container
docker run -d --restart always --name $1 --env-file ./.env tjtanjin/tele-qr:master
