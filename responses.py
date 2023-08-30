def response_handler(message) -> str:
    p_message = message.lower()

    if p_message == "hello":
        return "Hello there!"

    if p_message == "!help":
        return "editable help message to explain how to use bot"
