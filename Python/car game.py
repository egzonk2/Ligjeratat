command = ""
Started = False
Stopped = True
while True:
    command = input("> ").lower()
    if command == "start":
        if Started:
            print("Car has already started?")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        print("Car stopped...")
    elif command == "help":
        print("""
    start - to start car
    stop - to stop car
    quit - to quit
""")
    elif command == "quit":
        print("Cya next time!")
        break
    else:
        print("Sorry i don't understand that...")