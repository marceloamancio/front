# What is pubsub? [reference](https://www.bmc.com/blogs/pub-sub-publish-subscribe/)

Pub/sub stands for "publish/subscribe." It is a messaging pattern where publishers send messages to a central message queue, and subscribers receive and process those messages. The publisher and subscriber do not need to know about each other, and new subscribers can join or leave at any time without affecting the publisher or other subscribers. This pattern is often used in distributed systems, event-driven architectures, and microservices.

* Publisher: Sends the message.
* Subscriber: Receives the message (get from a message broker)
* Message broker: Intermediates publisher and subscriber.
* Topic: Facilitates the asynchronous message passing.
* Policies: User-created policies will allow for subscribers to filter out messages.

# Idea
* Isolate publishers from subscribers. It improves overall security.

# Benefits
* Decoupling software
* More modularized, rubust and secure software components
* Improve code quality
* Have a better view of the information flow.



