import os
import sys
from pathlib import Path
from google.cloud import pubsub_v1

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


if __name__ == "__main__":
    print("Hello World!",project_id )
    topic_name = "newt"
    publisher = get_publisher()
    create_a_topic(publisher, topic_name)

    print("==Hello World!")