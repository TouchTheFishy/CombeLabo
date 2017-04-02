import gpio

print("Hi! We'll try to light a LED!")

try:
    gpio.GPIO(15, 1)

except ValueError:
    print("Choose a port and and a pin that respect the suggested values")

## We try to launch Main but not in sudo so we think that the library
    #  didn't have the permission to write so we didn't see the LED light