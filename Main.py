import gpio

print("Hi! We'll try to light a LED!")

try:
    gpio.GPIO(15, 1)

except ValueError:
    print("Choose a port and and a pin that respect the suggested values")