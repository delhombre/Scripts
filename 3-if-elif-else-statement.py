#!/usr/bin/python3

#### Load external modules
import time

price = int(input("Enter a price: "))

if price > 100:
    print("Price greater than 100")
elif price == 100:
    print("Price is 100")
else:
    print("Price is less than 100")

print("Time for break?")

# A service management example
print()
action = input("satrt|stop|restart : ")
action = action.lower()

if action == "start":
    print("Starting ...", end="\n\n")
elif action == "stop":
    print("Stopping ...", end="\n\n")
elif action == "restart":
    print("Stopping ...", end="\n\n")
    time.sleep(2)
    print("Starting ...", end="\n\n")
else:
    print("Usage: start|stop|restart")
