number_of_msgs = int(input())

for i in range(number_of_msgs):
    msg_code = int(input())
    if msg_code == 88:
        print("Hello")
    elif msg_code == 86:
        print("How are you?")
    elif msg_code < 88:
        print("GREAT!")
    elif msg_code > 88:
        print("Bye,Bye.")

#comment