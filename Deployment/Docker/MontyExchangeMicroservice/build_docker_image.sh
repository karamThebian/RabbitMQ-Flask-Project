#!/bin/bash

DOCKER_FILE="$PWD/Deployment/Docker/MontyExchangeMicroservice/Dockerfile"

sudo docker build . -f "$DOCKER_FILE" -t kaytho/monty:montyexchangemicroservice