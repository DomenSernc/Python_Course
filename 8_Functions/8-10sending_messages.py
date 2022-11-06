messages = ["Hey, are you at home?", "Wanna grab a lunch?", "Call me ASAP!"]
sent_messages = []

def send_messages():
     while messages:
         printed_message = messages.pop()
         print(printed_message)
         sent_messages.append(printed_message)

send_messages()

print(messages)
print(sent_messages)
    