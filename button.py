from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

def print_thing():
    print("button pressed")

def on_press():
    led.on()
    print_thing()

def on_release():
    led.off()

button.when_pressed = on_press
button.when_released = on_release

pause()
