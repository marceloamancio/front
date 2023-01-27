import os
import sys
from pathlib import Path

import argparse
from google.cloud import pubsub_v1, pubsub

from enum import auto
from strenum import StrEnum


class Operation(StrEnum):
    CREATE_TOPIC = auto()
    MAKE_SUBSCRIPTION = auto()
    SEND_MESSAGE = auto()
    LISTEN_MESSAGE = auto()



# TODO(developer)
# project_id = "your-project-id"
# topic_id = "your-topic-id"


sys.path.insert(
    0, f"{Path().resolve().parent.parent}/environment/environment"
)

from constants import project_id

def create_a_topic(publisher, topic_name):
    # https://cloud.google.com/pubsub/docs/create-topic?pubsub_create_topic-python&hl=pt-br
    print(f"Creating topic {topic_name}!")

    # Create a topic
    topic_path = get_topic_path(topic_name)
    topic = publisher.create_topic(request={"name": topic_path})
    print(f"Topic created: {topic.name}")


def write_message(publisher, topic_name, message_data):
    topic_path = get_topic_path(topic_name)
    publisher.publish(topic_path, data=message_data.encode())

def make_subscription(topic_name, subscription_name):
    # Create a subscriber client
    subscriber = pubsub_v1.SubscriberClient()
    # Define the subscription path


    topic_name = f"projects/{project_id}/topics/{topic_name}"
    subscription_name = f"projects/{project_id}/subscriptions/{subscription_name}"

    print(f"topic_name={topic_name}; subscription_name={subscription_name}")

    def callback(message):
        print(message.data)
        message.ack()

    with pubsub_v1.SubscriberClient() as subscriber:
        subscriber.create_subscription(
            name=subscription_name, topic=topic_name)
        future = subscriber.subscribe(subscription_name, callback)

    return "==DONE=="

def get_publisher():
    return pubsub_v1.PublisherClient()

def get_topic_path(topic_name):
    return publisher.topic_path(project_id, topic_name)

def get_subscription_path(subscriber, subscription_name):
    return subscriber.subscription_path(project_id, subscription_name)

def get_parser(h):
    parser = argparse.ArgumentParser(add_help=h)
    parser.add_argument("--operation", help="Operation", required=True)
    parser.add_argument("--topic-name", help="Topic Name")
    parser.add_argument("--subscription-name", help="Subscription Name")
    parser.add_argument("--message", help="Message to be written")
    return parser

if __name__ == "__main__":
    p = get_parser(h=True)
    args = p.parse_args()

    try:
        print(args.operation)
        assert args.operation in Operation.__members__.keys() 
    except:
        print(f"Error: Operation --'{args.operation}' not in {list(Operation.__members__.keys())}")

    publisher = get_publisher()
    
    if args.operation == 'CREATE_TOPIC':
        create_a_topic(publisher, args.topic_name )
    elif args.operation == 'SEND_MESSAGE':
        write_message(publisher, args.topic_name, args.message )
    elif args.operation == 'MAKE_SUBSCRIPTION':
        make_subscription(args.topic_name, args.subscription_name)
    #elif args.operation == 'LISTEN_MESSAGE':
        #message_received = get_message(publisher, args.subscription_name)
        #print(f"[subscription] Message received {message_received}")
       # get_message(publisher, args.topic_name, args.subscription_name)
       