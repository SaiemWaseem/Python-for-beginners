#car Game
command = ""
started = False
while command.lower() != "quit ":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car started is already started! ")
        else:
             started = True
             print(" car started...")
    elif command == "stop":
        if not started:
            print("car is already stopped! ")
        else:
            started= False
            print (" car stopped... ")
    elif command == "help":
        print("""
start- to start the car ,
stop- to stop the car,
quit- to exit,           """)
    elif command == "quit":
        break
    else:
        print("Sorry! I don't understand ")
