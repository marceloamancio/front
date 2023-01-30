
TOPIC_NAME?=test_topic
SUBSCRIPTION_NAME?=test_topic-sub-mar
MESSAGE?=messagehere

hello:
	echo $(hi)

init:
	poetry install

create-topic-cli:
	gcloud pubsub topics create $(TOPIC_NAME)

create-subscription-cli:
	gcloud pubsub subscriptions create $(SUBSCRIPTION_NAME) --topic=$(TOPIC_NAME)

publish-message-cli:
	gcloud pubsub topics publish $(TOPIC_NAME) --message=$(MESSAGE)

receive-message-cli:
	gcloud pubsub subscriptions pull $(SUBSCRIPTION_NAME) --auto-ack

send-message:
	poetry run python example/main.py --operation SEND_MESSAGE --topic-name $(TOPIC_NAME) --message $(MESSAGE)

make-subscription:
	poetry run python example/main.py --operation MAKE_SUBSCRIPTION --topic-name $(TOPIC_NAME) --subscription-name $(SUBSCRIPTION_NAME)

create-topic:
	poetry run python example/main.py --operation CREATE_TOPIC --topic-name $(TOPIC_NAME)

read-message:
	poetry run python example/main.py --operation READ_MESSAGE --topic-name $(SUBSCRIPTION_NAME)





