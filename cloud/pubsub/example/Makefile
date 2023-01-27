
TOPIC_NAME?=test_topic
SUBSCRIPTION_NAME?=test_topic-sub
MESSAGE?=messagehere

m:
	echo "hello world"

run: 
	poetry run python example/main.py

make-subscription:
	poetry run python example/main.py --operation MAKE_SUBSCRIPTION --topic-name $(TOPIC_NAME) --subscription-name $(SUBSCRIPTION_NAME)

create-topic:
	poetry run python example/main.py --operation CREATE_TOPIC --topic-name $(TOPIC_NAME)

send-message:
	poetry run python example/main.py --operation SEND_MESSAGE --topic-name $(TOPIC_NAME) --message $(MESSAGE)

