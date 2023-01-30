import os
import argparse

from example.constants import Operation
from example.core import publisher
from example.core import publish_message, make_subscription, create_topic, read_message
from example.constants import default_message

def get_parser(h):
    parser = argparse.ArgumentParser(add_help=h)
    #parser.add_argument("--send-message", help="Message to be written")
    parser.add_argument("--operation", help="Operation", required=True)
    parser.add_argument("--topic-name", help="Topic Name")
    parser.add_argument("--message", help="Message to be publish")
    parser.add_argument("--subscription-name", help="Subscription Name")
    return parser

def main():
    p = get_parser(h=True)
    args = p.parse_args()

    try:
        print(args.operation)
        assert args.operation in Operation.__members__.keys() 
    except:
        print(f"Error: Operation --'{args.operation}' not in {list(Operation.__members__.keys())}")

    
    if args.operation == Operation.SEND_MESSAGE:
        publish_message(args.topic_name, args.message)
    elif args.operation == Operation.MAKE_SUBSCRIPTION:
        make_subscription(args.topic_name, args.subscription_name)
    elif args.operation == Operation.CREATE_TOPIC:
        create_topic(args.topic_name)
    elif args.operation == Operation.READ_MESSAGE:
        read_message(args.topic_name)
        

if __name__ == "__main__":
    main()
