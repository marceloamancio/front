import os
import sys
from pathlib import Path

import argparse
from google.cloud import pubsub_v1

from enum import auto
from strenum import StrEnum


class Operation(StrEnum):
    CREATE_TOPIC = auto()
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
    topic_path = publisher.topic_path(project_id, topic_name)
    topic = publisher.create_topic(request={"name": topic_path})
    print(f"Topic created: {topic.name}")

def get_publisher():
    return pubsub_v1.PublisherClient()


def get_parser(h):
    parser = argparse.ArgumentParser(add_help=h)
    parser.add_argument("--operation", help="Operation", required=True)
    parser.add_argument("--topic-name", help="Topic Name")
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
    

    # print("Hello World!",project_id )
    # topic_name = "newt"
    # publisher = get_publisher()
    # create_a_topic(publisher, topic_name)

    # print("==Hello World!")