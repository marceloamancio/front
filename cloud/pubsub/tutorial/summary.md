

# Gcloud pub/sub [PubSub Made Easy](https://www.youtube.com/watch?v=ML6P1ksHcqo&list=PLIivdWyY5sqKwVLe4BLJ-vlh9r9zCdOse&index=4)
* Microservice based architecture
* Asynchronous messagin
* Allow sending and receive message from independent applications.
* Pub/sub encompasses a Publiser/Subscriber model
* Publisher: Creates and send messages to a Topic (which is a named resource). The message is stored until is acknowledge by all subscribers.
* Subscriber: To receive a message, a Subscriber creates an Subscription to a Topic. Message will get to Subscriber either by pubsub pushing it to the Subscriber or the Subscriber pulling it from pubsub. 
* Message Acknowledge from the Subscriber: When message is received the message is removed from the Subscription backlog to it is not submitted again.
* Communication: One to many (fan out) ; Many to one (fan in); many to many.
* Pub/Sub can be used with Dataflow for enrichment and ordering. 


* Architecture [Architecture](img/model.png) 

# 4 steps 
* Step 1: Create a pubsub topic and subscriptions
* Step 2: Setup a service account and Cloud IAM
* Step 3: Start publisher and subscription apps
* Step 4: Send sample messages

