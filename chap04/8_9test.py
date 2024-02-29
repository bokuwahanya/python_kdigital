
def send_messages(first_messages, sent_messages) :

    while first_messages:
        current_message = first_messages.pop()
        sent_messages.append(current_message)

def show_messages(sent_messages):
    print("\n--sent_message--")
    for sent_message in sent_messages:
        print(sent_message)
 
first_messages=['hello','bye','see you']
sent_messages=[]

send_messages(first_messages[:], sent_messages)
show_messages(sent_messages)

print("\n--first messages--")

for first_message in first_messages:
    print(first_message)

