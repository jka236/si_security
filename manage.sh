#!/bin/sh

argument=$1
KALI_ID=$(docker ps -aqf "name=kali-docker")
DVWA_ID=$(docker ps -aqf "name=dvwa-docker")
if [ $argument = "build" ]; then
    echo "Building infrastructure. This might take up to 30 mins..."
    echo "Building and starting DVWA"
    docker build --no-cache -t dvwa-docker ./dvwa
    docker run --rm -it -d -p 80:80 --name dvwa-docker dvwa-docker


    echo "Building and starting Kali"
    docker build --no-cache -t kali-docker ./kali
    docker run --tty --interactive --name kali-docker kali-docker


elif [ $argument = "up" ]; then
    echo "starting DVWA"
    docker run --rm -it -d -p 80:80 --name dvwa-docker dvwa-docker
    sleep 5

    echo "Starting Kali"
    docker start $KALI_ID    
    sleep 2
    docker attach $KALI_ID


elif [ $argument = "stop" ]; then
    echo "Stopping infrastructure..."
    if [ -z "$KALI_ID" ]; then
        echo "Kali is already stopped"
    else
        docker stop $KALI_ID
        echo "Kali is successfully stopped"
    fi
    
    if [ -z "$DVWA_ID" ]; then
        echo "DVWA is already stopped"
    else
        docker stop $DVWA_ID
        echo "DVWA is successfully stopped"
    fi
    
else
  echo "Unknown argumnet! Options: build, up, stop"
fi