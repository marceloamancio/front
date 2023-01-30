import sys
from pathlib import Path

from google.cloud import pubsub_v1

sys.path.insert(
    0, f"{Path().resolve().parent.parent}/environment/environment"
)

from constants import project_id

def get_publisher():
    return pubsub_v1.PublisherClient()

def get_subscriber():
    return pubsub_v1.SubscriberClient()

def get_topic_path(name):
    return f"projects/{project_id}/topics/{name}"

def get_subscription_path(name):
    return f"projects/{project_id}/subscriptions/{name}"

def publish_message(topic_name, message):
    topic_path = get_topic_path(topic_name)
    future = publisher.publish(topic_path, data=message.encode(), nat='eggs', nata='baked')
    #future = publisher.publish(topic_name, b'My first message! 20', nat='eggs', nata='baked')
    print(future.result())

def make_subscription(topic_name, subscription_name):
    subscription_path =  get_subscription_path(subscription_name)
    topic_path = get_topic_path(topic_name)
    future = subscriber.create_subscription(name=subscription_path, topic=topic_path)

    print(future)

def create_topic(topic_name):
    # Create a topic
    topic_path = get_topic_path(topic_name)
    topic = publisher.create_topic(request={"name": topic_path})
    print(f"Topic created: {topic.name}")

def read_message(subscription_name):
    subscription_path = subscriber.subscription_path(project_id, subscription_name)

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        print(f"Received {message.data!r}.")
        if message.attributes:
            print("Attributes:")
            for key in message.attributes:
                value = message.attributes.get(key)
                print(f"{key}: {value}")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)


    with subscriber:
        try:
            streaming_pull_future.result(timeout=2)
        except TimeoutError:
            streaming_pull_future.cancel()  # Trigger the shutdown.
            streaming_pull_future.result()  # Block until the shutdown is complete.


publisher = get_publisher()
subscriber = get_subscriber()
