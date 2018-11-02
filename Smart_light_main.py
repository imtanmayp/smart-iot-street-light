from gpiozero import LightSensor
import RPi.GPIO as GPIO
import time
import subprocess

LED1=26

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

GPIO.setup(18,GPIO.IN) # Infrared

ldr = LightSensor(21) #change LDR pin

                   # Set initial brightness to 1%
def dim(bright):
	bright=bright/2.               # Set brightness to half
	pwm1.ChangeDutyCycle(20)

def brighten(bright):
	bright=bright*2                # Double Brightness
	pwm1.ChangeDutyCycle(100)  # Apply new brightness

		
def infrared():
	if(GPIO.input(18)==False): #object is far away
		brighten(1)
		time.sleep(3)
	if(GPIO.input(18)==True): #object is near
		dim(1)

def button():
        button_state = GPIO.input(23)
        if button_state == False:
            GPIO.output(24, True)
            return 1
        else:
            GPIO.output(24, False)
            return 2
        
def threadInfra():
        t = threading.Thread(target=infrared)
        t.start()
        t.join()

GPIO.setup(26,GPIO.OUT)
pwm1=GPIO.PWM(LED1,1000)  # We need to activate PWM on LED1 so we can dim, use 1000 Hz 
pwm1.start(0)
print("Application Started...")

while 1:
    time.sleep(0.000001)
    if (button() == 1):
	pwm1.start(0)
	brighten(1)
	subprocess.call(["python", "cam.py"])
	subprocess.call(["python3", "boto_v2.py"])
    
    elif (ldr.value < 0.4):
        pwm1.start(0)
    else:
        pwm1.stop(0)
GPIO.cleanup()
