# MontyExchange

## Introduction

This is a Python-Flask Webserver that communicates with RabbitMQ in order to produce and consume Messages via Restful Apis.

## Getting Started:

### PreRequisites:
* Docker
* docker-compose
* python-3.8 (Optional)

### Installation:
We can either run our monty exchange server locally via:
#### 1. Python
1.  First we need to install the requirements by executing : 
```commandline
pip install -r Microservices/ExchangeMicroservice/requirements.txt
```
2. Run the application via executing: 
```commandline
python3.8 Microservices/ExchangeMicroservice/app.py
```

Or we can Build the application on:

#### 2. Docker
1. We can either :
   * Build the image locally by executing the build docker image script and then execute our docker compose command:
   ```commandline
    ./Deployment/Docker/MontyExchangeMicroservice/build_docker_image.sh
    sudo docker-compose -f ./Deployment/Docker/MontyExchangeMicroservice/docker-compose.yml up -d

    ```
   
   * Or we can pull the immediately executing the docker compose file which automatically pulls from docker-hub and runs our montyExchange Server:
```commandline
sudo docker-compose -f ./Deployment/Docker/MontyExchangeMicroservice/docker-compose.yml up -d   
```


#### 3. RabbitMQ Server
   
2. In order to run the application, a Rabbit-MQ docker-container needs to be running, we can pull an image from docker hub by executing the following command:
```commandline
sudo docker run -it --rm --network my-network --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```
This command pulls and builds the RabbitMQ Image, and the --network argument links it to my-network so that the two docker containers can communicate.


#### Usage:

After the successful installation and execution, our monty exchange server should be running on http://localhost:9047/, where as the rabbitmq will be running on http://localhost:15672/
As requested in the requirements of the Assignment, the webserver has two main endpoints:

1. /Message:
* This route accepts a POST method with any json body, then it opens a connection with rabbitMQ server, declares an exchange called "monty.exchange" and a queue called "monty-queue" and binds them together via routing key "message" if not created before.
* After that, it published the message received to that exchange via the same routing key, and then closes the connection.

2. /Consume:
* This route accepts a GET method, and then opens up a connection with rabbitMQ server
* After that our monty-queue is checked for messages, if a message is found, it will consume and acknowledge it, removing it from the queue, and return it to the client. If not it will return: "There are no Available Messages to Consume." 
* The channel and connection are then closed.


### Future Additional Features
As you might see, this is a fairly simple application with small features as requested.

However, many layers can be added to it such as:

* A UserMicroservice to Manage Users
* An Authentication Microservice to Login Users and grant them an Encrypted token, adding a layer security to the application allowing only authenticated users to produce and/or consume messages.
* Another queue that stores the produced messages in a Database to be retrieved later
* A database such as mongo database to store all user credentials and stored data
* Hashed Password Encryption for User's Credential Storage
* Validation on the body of the Post Request to restrain users to send only specific fields, which can be done by adding Connexion and an OpenAPi Specification.


For any additional information, please dont hesitate to contact me at karam.thebian@hotmail.com